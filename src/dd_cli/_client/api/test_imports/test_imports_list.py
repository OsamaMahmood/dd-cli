import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_test_import_list import PaginatedTestImportList
from ...models.test_imports_list_o_item import TestImportsListOItem
from ...models.test_imports_list_test_import_finding_action_action import (
    TestImportsListTestImportFindingActionAction,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    findings_affected: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[TestImportsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    test: int | Unset = UNSET,
    test_import_finding_action_action: TestImportsListTestImportFindingActionAction | Unset = UNSET,
    test_import_finding_action_created: datetime.datetime | Unset = UNSET,
    test_import_finding_action_finding: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["branch_tag"] = branch_tag

    params["build_id"] = build_id

    params["commit_hash"] = commit_hash

    json_findings_affected: list[int] | Unset = UNSET
    if not isinstance(findings_affected, Unset):
        json_findings_affected = findings_affected

    params["findings_affected"] = json_findings_affected

    params["limit"] = limit

    json_o: list[str] | Unset = UNSET
    if not isinstance(o, Unset):
        json_o = []
        for o_item_data in o:
            o_item = o_item_data.value
            json_o.append(o_item)

    params["o"] = json_o

    params["offset"] = offset

    params["test"] = test

    json_test_import_finding_action_action: str | Unset = UNSET
    if not isinstance(test_import_finding_action_action, Unset):
        json_test_import_finding_action_action = test_import_finding_action_action.value

    params["test_import_finding_action__action"] = json_test_import_finding_action_action

    json_test_import_finding_action_created: str | Unset = UNSET
    if not isinstance(test_import_finding_action_created, Unset):
        json_test_import_finding_action_created = test_import_finding_action_created.isoformat()
    params["test_import_finding_action__created"] = json_test_import_finding_action_created

    params["test_import_finding_action__finding"] = test_import_finding_action_finding

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/test_imports/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedTestImportList | None:
    if response.status_code == 200:
        response_200 = PaginatedTestImportList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedTestImportList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    findings_affected: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[TestImportsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    test: int | Unset = UNSET,
    test_import_finding_action_action: TestImportsListTestImportFindingActionAction | Unset = UNSET,
    test_import_finding_action_created: datetime.datetime | Unset = UNSET,
    test_import_finding_action_finding: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedTestImportList]:
    """
    Args:
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        findings_affected (list[int] | Unset):
        limit (int | Unset):
        o (list[TestImportsListOItem] | Unset):
        offset (int | Unset):
        test (int | Unset):
        test_import_finding_action_action (TestImportsListTestImportFindingActionAction | Unset):
        test_import_finding_action_created (datetime.datetime | Unset):
        test_import_finding_action_finding (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTestImportList]
    """

    kwargs = _get_kwargs(
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        findings_affected=findings_affected,
        limit=limit,
        o=o,
        offset=offset,
        test=test,
        test_import_finding_action_action=test_import_finding_action_action,
        test_import_finding_action_created=test_import_finding_action_created,
        test_import_finding_action_finding=test_import_finding_action_finding,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    findings_affected: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[TestImportsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    test: int | Unset = UNSET,
    test_import_finding_action_action: TestImportsListTestImportFindingActionAction | Unset = UNSET,
    test_import_finding_action_created: datetime.datetime | Unset = UNSET,
    test_import_finding_action_finding: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedTestImportList | None:
    """
    Args:
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        findings_affected (list[int] | Unset):
        limit (int | Unset):
        o (list[TestImportsListOItem] | Unset):
        offset (int | Unset):
        test (int | Unset):
        test_import_finding_action_action (TestImportsListTestImportFindingActionAction | Unset):
        test_import_finding_action_created (datetime.datetime | Unset):
        test_import_finding_action_finding (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTestImportList
    """

    return sync_detailed(
        client=client,
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        findings_affected=findings_affected,
        limit=limit,
        o=o,
        offset=offset,
        test=test,
        test_import_finding_action_action=test_import_finding_action_action,
        test_import_finding_action_created=test_import_finding_action_created,
        test_import_finding_action_finding=test_import_finding_action_finding,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    findings_affected: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[TestImportsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    test: int | Unset = UNSET,
    test_import_finding_action_action: TestImportsListTestImportFindingActionAction | Unset = UNSET,
    test_import_finding_action_created: datetime.datetime | Unset = UNSET,
    test_import_finding_action_finding: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedTestImportList]:
    """
    Args:
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        findings_affected (list[int] | Unset):
        limit (int | Unset):
        o (list[TestImportsListOItem] | Unset):
        offset (int | Unset):
        test (int | Unset):
        test_import_finding_action_action (TestImportsListTestImportFindingActionAction | Unset):
        test_import_finding_action_created (datetime.datetime | Unset):
        test_import_finding_action_finding (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTestImportList]
    """

    kwargs = _get_kwargs(
        branch_tag=branch_tag,
        build_id=build_id,
        commit_hash=commit_hash,
        findings_affected=findings_affected,
        limit=limit,
        o=o,
        offset=offset,
        test=test,
        test_import_finding_action_action=test_import_finding_action_action,
        test_import_finding_action_created=test_import_finding_action_created,
        test_import_finding_action_finding=test_import_finding_action_finding,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    branch_tag: str | Unset = UNSET,
    build_id: str | Unset = UNSET,
    commit_hash: str | Unset = UNSET,
    findings_affected: list[int] | Unset = UNSET,
    limit: int | Unset = UNSET,
    o: list[TestImportsListOItem] | Unset = UNSET,
    offset: int | Unset = UNSET,
    test: int | Unset = UNSET,
    test_import_finding_action_action: TestImportsListTestImportFindingActionAction | Unset = UNSET,
    test_import_finding_action_created: datetime.datetime | Unset = UNSET,
    test_import_finding_action_finding: int | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedTestImportList | None:
    """
    Args:
        branch_tag (str | Unset):
        build_id (str | Unset):
        commit_hash (str | Unset):
        findings_affected (list[int] | Unset):
        limit (int | Unset):
        o (list[TestImportsListOItem] | Unset):
        offset (int | Unset):
        test (int | Unset):
        test_import_finding_action_action (TestImportsListTestImportFindingActionAction | Unset):
        test_import_finding_action_created (datetime.datetime | Unset):
        test_import_finding_action_finding (int | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTestImportList
    """

    return (
        await asyncio_detailed(
            client=client,
            branch_tag=branch_tag,
            build_id=build_id,
            commit_hash=commit_hash,
            findings_affected=findings_affected,
            limit=limit,
            o=o,
            offset=offset,
            test=test,
            test_import_finding_action_action=test_import_finding_action_action,
            test_import_finding_action_created=test_import_finding_action_created,
            test_import_finding_action_finding=test_import_finding_action_finding,
            version=version,
        )
    ).parsed
