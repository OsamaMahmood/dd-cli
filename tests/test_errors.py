from __future__ import annotations

import pytest

from dd_cli.errors import (
    APIError,
    AuthError,
    AuthorizationError,
    ConfigError,
    DDCliError,
    ExitCode,
    NetworkError,
    NotFoundError,
    ValidationError,
    from_status_code,
)


def test_base_error_carries_message_and_hint() -> None:
    err = DDCliError("boom", hint="try X")
    assert err.message == "boom"
    assert err.hint == "try X"
    assert str(err) == "boom"
    assert err.exit_code == ExitCode.GENERIC_ERROR


@pytest.mark.parametrize(
    ("cls", "expected"),
    [
        (AuthError, ExitCode.AUTH_ERROR),
        (AuthorizationError, ExitCode.AUTHZ_ERROR),
        (NotFoundError, ExitCode.NOT_FOUND),
        (ValidationError, ExitCode.VALIDATION_ERROR),
        (APIError, ExitCode.API_ERROR),
        (NetworkError, ExitCode.NETWORK_ERROR),
        (ConfigError, ExitCode.CONFIG_ERROR),
    ],
)
def test_each_error_has_stable_exit_code(cls: type[DDCliError], expected: int) -> None:
    assert cls("x").exit_code == expected


@pytest.mark.parametrize(
    ("status", "cls"),
    [
        (400, ValidationError),
        (401, AuthError),
        (403, AuthorizationError),
        (404, NotFoundError),
        (500, APIError),
        (502, APIError),
        (503, APIError),
    ],
)
def test_from_status_code_maps_correctly(status: int, cls: type[DDCliError]) -> None:
    err = from_status_code(status, "msg")
    assert isinstance(err, cls)
    assert err.message == "msg"


def test_from_status_code_passes_hint() -> None:
    err = from_status_code(401, "unauthorized", hint="check DD_API_KEY")
    assert err.hint == "check DD_API_KEY"


def test_exit_codes_are_distinct() -> None:
    codes = [
        ExitCode.SUCCESS,
        ExitCode.GENERIC_ERROR,
        ExitCode.USAGE_ERROR,
        ExitCode.AUTH_ERROR,
        ExitCode.AUTHZ_ERROR,
        ExitCode.NOT_FOUND,
        ExitCode.VALIDATION_ERROR,
        ExitCode.API_ERROR,
        ExitCode.NETWORK_ERROR,
        ExitCode.CONFIG_ERROR,
    ]
    assert len(codes) == len(set(codes))
