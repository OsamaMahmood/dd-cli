from __future__ import annotations

import httpx
import pytest
from pytest_httpx import HTTPXMock

from dd_cli.client import DefectDojoClient
from dd_cli.config import Profile
from dd_cli.errors import APIError, AuthError, NetworkError, NotFoundError, ValidationError


@pytest.fixture
def profile() -> Profile:
    return Profile(
        url="https://dd.example",
        api_key="the-token",  # type: ignore[arg-type]
        ssl_verify=True,
        extra_headers={"X-Tenant": "main"},
    )


@pytest.fixture
def no_sleep() -> list[float]:
    """List that records "sleep" calls; pass `.append` as the sleep callable."""
    return []


@pytest.fixture
def client(profile: Profile, no_sleep: list[float]) -> DefectDojoClient:
    return DefectDojoClient(profile, sleep=no_sleep.append)


# ---------------------------- whoami / auth header ----------------------- #


def test_whoami_returns_parsed_body(client: DefectDojoClient, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"user": {"id": 1, "username": "tester"}},
    )
    body = client.whoami()
    assert body == {"user": {"id": 1, "username": "tester"}}


def test_whoami_sends_token_auth_header(
    client: DefectDojoClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"user": {"id": 1}},
    )
    client.whoami()
    request = httpx_mock.get_request()
    assert request is not None
    assert request.headers["Authorization"] == "Token the-token"


def test_extra_headers_are_attached(
    profile: Profile, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={},
    )
    client = DefectDojoClient(profile, sleep=lambda _: None)
    client.whoami()
    request = httpx_mock.get_request()
    assert request is not None
    assert request.headers["X-Tenant"] == "main"


# ---------------------------- error mapping ------------------------------- #


def test_401_maps_to_auth_error(client: DefectDojoClient, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=401,
        json={"detail": "Invalid token."},
    )
    with pytest.raises(AuthError):
        client.whoami()


def test_404_maps_to_not_found(client: DefectDojoClient, httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=404,
        json={"detail": "Not found."},
    )
    with pytest.raises(NotFoundError):
        client.whoami()


def test_400_includes_detail_in_message(
    client: DefectDojoClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=400,
        json={"detail": "Bad request"},
    )
    with pytest.raises(ValidationError) as excinfo:
        client.whoami()
    assert "Bad request" in str(excinfo.value)


# ---------------------------- retry behaviour ----------------------------- #


def test_retries_on_503_then_succeeds(
    profile: Profile, httpx_mock: HTTPXMock, no_sleep: list[float]
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=503,
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=503,
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"user": {"id": 1}},
    )

    client = DefectDojoClient(profile, sleep=no_sleep.append, backoff_factor=0.01)
    body = client.whoami()
    assert body == {"user": {"id": 1}}
    assert len(no_sleep) == 2  # slept after the two 503s


def test_retries_on_429(profile: Profile, httpx_mock: HTTPXMock, no_sleep: list[float]) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=429,
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        json={"user": {"id": 1}},
    )

    client = DefectDojoClient(profile, sleep=no_sleep.append)
    client.whoami()
    assert len(no_sleep) == 1


def test_returns_last_response_after_max_retries(
    profile: Profile, httpx_mock: HTTPXMock, no_sleep: list[float]
) -> None:
    for _ in range(4):  # max_retries=3 + initial = 4 calls
        httpx_mock.add_response(
            url="https://dd.example/api/v2/user_profile/",
            status_code=503,
        )

    client = DefectDojoClient(profile, sleep=no_sleep.append, max_retries=3)
    with pytest.raises(APIError):
        client.whoami()


def test_400_is_not_retried(
    profile: Profile, httpx_mock: HTTPXMock, no_sleep: list[float]
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/user_profile/",
        status_code=400,
        json={"detail": "bad"},
    )
    client = DefectDojoClient(profile, sleep=no_sleep.append)
    with pytest.raises(ValidationError):
        client.whoami()
    assert no_sleep == []  # never slept


def test_network_error_after_retries(
    profile: Profile, httpx_mock: HTTPXMock, no_sleep: list[float]
) -> None:
    for _ in range(4):
        httpx_mock.add_exception(httpx.ConnectError("boom"))

    client = DefectDojoClient(profile, sleep=no_sleep.append, max_retries=3)
    with pytest.raises(NetworkError):
        client.whoami()


def test_timeout_after_retries(
    profile: Profile, httpx_mock: HTTPXMock, no_sleep: list[float]
) -> None:
    for _ in range(4):
        httpx_mock.add_exception(httpx.ReadTimeout("slow"))

    client = DefectDojoClient(profile, sleep=no_sleep.append, max_retries=3)
    with pytest.raises(NetworkError) as excinfo:
        client.whoami()
    assert "timed out" in str(excinfo.value)


# ---------------------------- pagination ---------------------------------- #


def test_paginate_walks_next_links(
    client: DefectDojoClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={
            "next": "https://dd.example/api/v2/products/?page=2",
            "previous": None,
            "results": [{"id": 1, "name": "alpha"}, {"id": 2, "name": "beta"}],
        },
    )
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/?page=2",
        json={
            "next": None,
            "previous": "...",
            "results": [{"id": 3, "name": "gamma"}],
        },
    )

    items = list(client.paginate("/api/v2/products/"))
    assert [it["id"] for it in items] == [1, 2, 3]


def test_paginate_with_filters(
    client: DefectDojoClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/findings/?severity=High",
        json={"next": None, "results": [{"id": 1, "severity": "High"}]},
    )
    items = list(client.paginate("/api/v2/findings/", params={"severity": "High"}))
    assert items == [{"id": 1, "severity": "High"}]


def test_paginate_empty_results(
    client: DefectDojoClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(
        url="https://dd.example/api/v2/products/",
        json={"next": None, "results": []},
    )
    assert list(client.paginate("/api/v2/products/")) == []


# ---------------------------- profile validation -------------------------- #


def test_incomplete_profile_rejected() -> None:
    with pytest.raises(APIError):
        DefectDojoClient(Profile())  # no url, no api_key
