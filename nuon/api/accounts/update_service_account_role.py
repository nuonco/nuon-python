from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_account import AppAccount
from ...models.service_update_service_account_role_request import ServiceUpdateServiceAccountRoleRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ServiceUpdateServiceAccountRoleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/service-accounts/{account_id}/role".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAccount | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAccount.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppAccount | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateServiceAccountRoleRequest,
) -> Response[AppAccount | StderrErrResponse]:
    """Update the role of a service account for the current org

     Update the role assigned to a service account in the current org.

    The service account's existing roles in this org are removed and replaced
    with the requested role. Allowed roles are `org_admin`, `installer`, and
    `runner`.

    Args:
        account_id (str):
        body (ServiceUpdateServiceAccountRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAccount | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateServiceAccountRoleRequest,
) -> AppAccount | StderrErrResponse | None:
    """Update the role of a service account for the current org

     Update the role assigned to a service account in the current org.

    The service account's existing roles in this org are removed and replaced
    with the requested role. Allowed roles are `org_admin`, `installer`, and
    `runner`.

    Args:
        account_id (str):
        body (ServiceUpdateServiceAccountRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAccount | StderrErrResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateServiceAccountRoleRequest,
) -> Response[AppAccount | StderrErrResponse]:
    """Update the role of a service account for the current org

     Update the role assigned to a service account in the current org.

    The service account's existing roles in this org are removed and replaced
    with the requested role. Allowed roles are `org_admin`, `installer`, and
    `runner`.

    Args:
        account_id (str):
        body (ServiceUpdateServiceAccountRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAccount | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateServiceAccountRoleRequest,
) -> AppAccount | StderrErrResponse | None:
    """Update the role of a service account for the current org

     Update the role assigned to a service account in the current org.

    The service account's existing roles in this org are removed and replaced
    with the requested role. Allowed roles are `org_admin`, `installer`, and
    `runner`.

    Args:
        account_id (str):
        body (ServiceUpdateServiceAccountRoleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAccount | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
