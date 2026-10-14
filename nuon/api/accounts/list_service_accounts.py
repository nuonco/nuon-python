from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_service_accounts_management import ListServiceAccountsManagement
from ...models.service_service_account import ServiceServiceAccount
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    include_runners: bool | Unset = UNSET,
    include_stacks: bool | Unset = UNSET,
    management: ListServiceAccountsManagement | Unset = UNSET,
    purpose: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params["include_runners"] = include_runners

    params["include_stacks"] = include_stacks

    json_management: str | Unset = UNSET
    if not isinstance(management, Unset):
        json_management = management.value

    params["management"] = json_management

    params["purpose"] = purpose

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/service-accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[ServiceServiceAccount] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceServiceAccount.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StderrErrResponse | list[ServiceServiceAccount]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    include_runners: bool | Unset = UNSET,
    include_stacks: bool | Unset = UNSET,
    management: ListServiceAccountsManagement | Unset = UNSET,
    purpose: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[ServiceServiceAccount]]:
    """List service accounts for the current org

     List the service accounts that belong to the current organization, along with
    their roles. Supports offset-based pagination.

    Each account reports whether it is a system account, its purposes, and, for
    accounts managed by a resource, the owning resource.

    - `management` filters to `user` accounts, `system` accounts, or `all`. When set,
      it replaces `include_runners` and `include_stacks`.
    - `purpose` filters to accounts with that exact purpose.
    - `q` matches a case-insensitive substring of the account name, email, or ID, or
      of the owning resource's name or ID.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        include_runners (bool | Unset):
        include_stacks (bool | Unset):
        management (ListServiceAccountsManagement | Unset):
        purpose (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[ServiceServiceAccount]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
        include_runners=include_runners,
        include_stacks=include_stacks,
        management=management,
        purpose=purpose,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    include_runners: bool | Unset = UNSET,
    include_stacks: bool | Unset = UNSET,
    management: ListServiceAccountsManagement | Unset = UNSET,
    purpose: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> StderrErrResponse | list[ServiceServiceAccount] | None:
    """List service accounts for the current org

     List the service accounts that belong to the current organization, along with
    their roles. Supports offset-based pagination.

    Each account reports whether it is a system account, its purposes, and, for
    accounts managed by a resource, the owning resource.

    - `management` filters to `user` accounts, `system` accounts, or `all`. When set,
      it replaces `include_runners` and `include_stacks`.
    - `purpose` filters to accounts with that exact purpose.
    - `q` matches a case-insensitive substring of the account name, email, or ID, or
      of the owning resource's name or ID.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        include_runners (bool | Unset):
        include_stacks (bool | Unset):
        management (ListServiceAccountsManagement | Unset):
        purpose (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[ServiceServiceAccount]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        page=page,
        include_runners=include_runners,
        include_stacks=include_stacks,
        management=management,
        purpose=purpose,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    include_runners: bool | Unset = UNSET,
    include_stacks: bool | Unset = UNSET,
    management: ListServiceAccountsManagement | Unset = UNSET,
    purpose: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[ServiceServiceAccount]]:
    """List service accounts for the current org

     List the service accounts that belong to the current organization, along with
    their roles. Supports offset-based pagination.

    Each account reports whether it is a system account, its purposes, and, for
    accounts managed by a resource, the owning resource.

    - `management` filters to `user` accounts, `system` accounts, or `all`. When set,
      it replaces `include_runners` and `include_stacks`.
    - `purpose` filters to accounts with that exact purpose.
    - `q` matches a case-insensitive substring of the account name, email, or ID, or
      of the owning resource's name or ID.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        include_runners (bool | Unset):
        include_stacks (bool | Unset):
        management (ListServiceAccountsManagement | Unset):
        purpose (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[ServiceServiceAccount]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
        include_runners=include_runners,
        include_stacks=include_stacks,
        management=management,
        purpose=purpose,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    include_runners: bool | Unset = UNSET,
    include_stacks: bool | Unset = UNSET,
    management: ListServiceAccountsManagement | Unset = UNSET,
    purpose: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> StderrErrResponse | list[ServiceServiceAccount] | None:
    """List service accounts for the current org

     List the service accounts that belong to the current organization, along with
    their roles. Supports offset-based pagination.

    Each account reports whether it is a system account, its purposes, and, for
    accounts managed by a resource, the owning resource.

    - `management` filters to `user` accounts, `system` accounts, or `all`. When set,
      it replaces `include_runners` and `include_stacks`.
    - `purpose` filters to accounts with that exact purpose.
    - `q` matches a case-insensitive substring of the account name, email, or ID, or
      of the owning resource's name or ID.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        include_runners (bool | Unset):
        include_stacks (bool | Unset):
        management (ListServiceAccountsManagement | Unset):
        purpose (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[ServiceServiceAccount]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            page=page,
            include_runners=include_runners,
            include_stacks=include_stacks,
            management=management,
            purpose=purpose,
            q=q,
        )
    ).parsed
