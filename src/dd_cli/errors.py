"""Typed exception hierarchy for dd-cli.

Each exception maps to a stable CLI exit code documented in PLAN.md §5. The
top-level CLI catches `DDCliError` and exits with `error.exit_code`; anything
else propagates as exit code 1.
"""

from __future__ import annotations


class ExitCode:
    """Stable CLI exit codes. See PLAN.md §5."""

    SUCCESS = 0
    GENERIC_ERROR = 1
    USAGE_ERROR = 2
    AUTH_ERROR = 3
    AUTHZ_ERROR = 4
    NOT_FOUND = 5
    VALIDATION_ERROR = 6
    API_ERROR = 7
    NETWORK_ERROR = 8
    CONFIG_ERROR = 9


class DDCliError(Exception):
    """Base class for all dd-cli runtime errors with a stable exit code."""

    exit_code: int = ExitCode.GENERIC_ERROR

    def __init__(self, message: str, *, hint: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.hint = hint


class AuthError(DDCliError):
    """401 from DefectDojo, missing or invalid API token."""

    exit_code = ExitCode.AUTH_ERROR


class AuthorizationError(DDCliError):
    """403 from DefectDojo, valid token but insufficient permissions."""

    exit_code = ExitCode.AUTHZ_ERROR


class NotFoundError(DDCliError):
    """404 from DefectDojo, resource does not exist."""

    exit_code = ExitCode.NOT_FOUND


class ValidationError(DDCliError):
    """400 from DefectDojo or local input validation failure."""

    exit_code = ExitCode.VALIDATION_ERROR


class APIError(DDCliError):
    """5xx from DefectDojo after retries exhausted, or unexpected status."""

    exit_code = ExitCode.API_ERROR


class NetworkError(DDCliError):
    """Connection refused, timeout, DNS failure, etc."""

    exit_code = ExitCode.NETWORK_ERROR


class ConfigError(DDCliError):
    """Missing/invalid dd-cli configuration (profile, URL, API key)."""

    exit_code = ExitCode.CONFIG_ERROR


def from_status_code(status_code: int, message: str, *, hint: str | None = None) -> DDCliError:
    """Map an HTTP status code to a typed dd-cli error."""
    if status_code == 400:
        return ValidationError(message, hint=hint)
    if status_code == 401:
        return AuthError(message, hint=hint)
    if status_code == 403:
        return AuthorizationError(message, hint=hint)
    if status_code == 404:
        return NotFoundError(message, hint=hint)
    return APIError(message, hint=hint)
