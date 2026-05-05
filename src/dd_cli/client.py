"""High-level wrapper around the generated DefectDojo API client.

`DefectDojoClient` adds the cross-cutting behavior that callers need but the
generated client deliberately leaves out: retry-with-backoff on transient
failures, pagination iteration for list endpoints, error mapping from
HTTP status codes to typed `dd_cli.errors`, and auth header injection.

The generated `AuthenticatedClient` is exposed via `client.raw` for callers
that need to call generated endpoints directly.
"""

from __future__ import annotations

import time
from collections.abc import Callable, Iterator, Mapping
from typing import Any, TypeVar

import httpx

from dd_cli._client.client import AuthenticatedClient
from dd_cli._client.errors import UnexpectedStatus
from dd_cli.config import Profile
from dd_cli.errors import (
    APIError,
    AuthError,
    NetworkError,
    NotFoundError,
    from_status_code,
)

DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_BACKOFF_FACTOR = 0.5
RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})

T = TypeVar("T")


class DefectDojoClient:
    """High-level dd-cli wrapper around the generated DefectDojo API client."""

    def __init__(
        self,
        profile: Profile,
        *,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        max_retries: int = DEFAULT_MAX_RETRIES,
        backoff_factor: float = DEFAULT_BACKOFF_FACTOR,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        if not profile.is_complete():
            raise APIError(
                "Profile is missing url or api_key.",
                hint="Run `dd configure` to set them.",
            )
        assert profile.url is not None  # narrowed by is_complete()
        assert profile.api_key is not None
        self._profile = profile
        self._max_retries = max_retries
        self._backoff_factor = backoff_factor
        self._sleep = sleep
        self._raw = AuthenticatedClient(
            base_url=profile.url,
            token=profile.api_key.get_secret_value(),
            prefix="Token",
            auth_header_name="Authorization",
            verify_ssl=profile.ssl_verify,
            headers=dict(profile.extra_headers),
            timeout=httpx.Timeout(timeout),
        )

    @property
    def raw(self) -> AuthenticatedClient:
        """The underlying generated `AuthenticatedClient`."""
        return self._raw

    def __enter__(self) -> DefectDojoClient:
        self._raw.__enter__()
        return self

    def __exit__(self, *args: object, **kwargs: object) -> None:
        self._raw.__exit__()

    # ------------------------------------------------------------------ #
    #  Endpoint helpers                                                  #
    # ------------------------------------------------------------------ #

    def whoami(self) -> dict[str, Any]:
        """Hit `/api/v2/user_profile/` to verify connectivity + auth."""
        return self.get("/api/v2/user_profile/")

    def get(self, path: str, *, params: Mapping[str, Any] | None = None) -> dict[str, Any]:
        """GET a single resource and return the parsed JSON body.

        Raises a typed `DDCliError` on failure. For paginated list endpoints
        prefer `paginate()`, which streams results across pages.
        """
        query = dict(params) if params else None

        def _call() -> httpx.Response:
            return self._raw.get_httpx_client().get(path, params=query)

        response = self._with_retry(_call)
        body = self._parse_response(response)
        if not isinstance(body, Mapping):
            raise APIError(f"Unexpected response shape from {path}")
        return dict(body)

    def paginate(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        page_size: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Yield items from a DefectDojo paginated list endpoint.

        Walks pages by following the `next` URL each response returns.
        """
        next_url: str = path
        query: dict[str, Any] = dict(params or {})
        if page_size is not None:
            query["limit"] = page_size

        while True:
            current_url = next_url
            current_query = query

            def _call(
                url: str = current_url, q: Mapping[str, Any] = current_query
            ) -> httpx.Response:
                return self._raw.get_httpx_client().get(url, params=q if q else None)

            response = self._with_retry(_call)
            body = self._parse_response(response)
            if not isinstance(body, Mapping):
                raise APIError(f"Unexpected paginated response shape from {path}")
            results = body.get("results", [])
            if not isinstance(results, list):
                raise APIError(f"Expected list `results` from {path}")
            for item in results:
                if isinstance(item, Mapping):
                    yield dict(item)
            next_link = body.get("next")
            if not isinstance(next_link, str):
                break
            next_url = next_link
            # Subsequent pages embed all params in `next`, so clear our explicit query.
            query = {}

    # ------------------------------------------------------------------ #
    #  Internals                                                         #
    # ------------------------------------------------------------------ #

    def _with_retry(self, fn: Callable[[], httpx.Response]) -> httpx.Response:
        """Call `fn` with retry on transient errors. Returns the final response."""
        last_response: httpx.Response | None = None
        for attempt in range(self._max_retries + 1):
            try:
                response = fn()
            except httpx.TimeoutException as exc:
                if attempt == self._max_retries:
                    raise NetworkError(
                        f"Request to {self._profile.url} timed out: {exc}",
                        hint="Check network connectivity or raise the timeout.",
                    ) from exc
                self._sleep(self._delay(attempt))
                continue
            except httpx.RequestError as exc:
                if attempt == self._max_retries:
                    raise NetworkError(f"Network error calling {self._profile.url}: {exc}") from exc
                self._sleep(self._delay(attempt))
                continue

            if response.status_code not in RETRYABLE_STATUS_CODES:
                return response

            last_response = response
            if attempt == self._max_retries:
                return response
            self._sleep(self._delay(attempt))

        # unreachable in practice — last-iteration return covers it.
        assert last_response is not None
        return last_response

    def _delay(self, attempt: int) -> float:
        return float(self._backoff_factor * (2**attempt))

    def _parse_response(self, response: httpx.Response) -> Any:
        if 200 <= response.status_code < 300:
            try:
                return response.json()
            except ValueError as exc:
                raise APIError(f"Invalid JSON in response: {exc}") from exc

        message = self._extract_error_message(response)
        if response.status_code == 401:
            raise AuthError(
                message,
                hint="Check that DD_API_KEY (or `dd config set api_key`) is correct.",
            )
        if response.status_code == 404:
            raise NotFoundError(message)
        raise from_status_code(response.status_code, message)

    @staticmethod
    def _extract_error_message(response: httpx.Response) -> str:
        try:
            body = response.json()
        except ValueError:
            return f"HTTP {response.status_code}: {response.text[:200]}"
        if isinstance(body, dict) and "detail" in body:
            return f"HTTP {response.status_code}: {body['detail']}"
        return f"HTTP {response.status_code}: {body}"


def _ensure_unexpected_status_imported() -> type[UnexpectedStatus]:
    """Re-export the generated client's exception so callers don't need to dig into _client/."""
    return UnexpectedStatus
