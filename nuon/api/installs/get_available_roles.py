from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_available_roles_operation_type import GetAvailableRolesOperationType
from ...models.get_available_roles_principal_type import GetAvailableRolesPrincipalType
from ...models.service_available_roles_response import ServiceAvailableRolesResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    principal_type: GetAvailableRolesPrincipalType | Unset = UNSET,
    operation_type: GetAvailableRolesOperationType | Unset = UNSET,
    principal_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_principal_type: str | Unset = UNSET
    if not isinstance(principal_type, Unset):
        json_principal_type = principal_type.value

    params["principal_type"] = json_principal_type

    json_operation_type: str | Unset = UNSET
    if not isinstance(operation_type, Unset):
        json_operation_type = operation_type.value

    params["operation_type"] = json_operation_type

    params["principal_id"] = principal_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/available-roles".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceAvailableRolesResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceAvailableRolesResponse.from_dict(response.json())

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
) -> Response[ServiceAvailableRolesResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    principal_type: GetAvailableRolesPrincipalType | Unset = UNSET,
    operation_type: GetAvailableRolesOperationType | Unset = UNSET,
    principal_id: str | Unset = UNSET,
) -> Response[ServiceAvailableRolesResponse | StderrErrResponse]:
    """get available IAM roles for a specific operation

     Returns a list of available IAM roles that can be used for a specific operation on an install.

    The endpoint filters roles based on the operation type:
    - **provision/reprovision**: Custom roles, break glass roles, provision IAM role
    - **deprovision/teardown**: Custom roles, break glass roles, deprovision IAM role
    - **deploy**: Custom roles, break glass roles, maintenance IAM role
    - **trigger** (actions): Custom roles, break glass roles, provision + maintenance IAM roles

    Roles are sourced from the install's stack outputs.

    Args:
        install_id (str):
        principal_type (GetAvailableRolesPrincipalType | Unset):
        operation_type (GetAvailableRolesOperationType | Unset):
        principal_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceAvailableRolesResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        principal_type=principal_type,
        operation_type=operation_type,
        principal_id=principal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    principal_type: GetAvailableRolesPrincipalType | Unset = UNSET,
    operation_type: GetAvailableRolesOperationType | Unset = UNSET,
    principal_id: str | Unset = UNSET,
) -> ServiceAvailableRolesResponse | StderrErrResponse | None:
    """get available IAM roles for a specific operation

     Returns a list of available IAM roles that can be used for a specific operation on an install.

    The endpoint filters roles based on the operation type:
    - **provision/reprovision**: Custom roles, break glass roles, provision IAM role
    - **deprovision/teardown**: Custom roles, break glass roles, deprovision IAM role
    - **deploy**: Custom roles, break glass roles, maintenance IAM role
    - **trigger** (actions): Custom roles, break glass roles, provision + maintenance IAM roles

    Roles are sourced from the install's stack outputs.

    Args:
        install_id (str):
        principal_type (GetAvailableRolesPrincipalType | Unset):
        operation_type (GetAvailableRolesOperationType | Unset):
        principal_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceAvailableRolesResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        principal_type=principal_type,
        operation_type=operation_type,
        principal_id=principal_id,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    principal_type: GetAvailableRolesPrincipalType | Unset = UNSET,
    operation_type: GetAvailableRolesOperationType | Unset = UNSET,
    principal_id: str | Unset = UNSET,
) -> Response[ServiceAvailableRolesResponse | StderrErrResponse]:
    """get available IAM roles for a specific operation

     Returns a list of available IAM roles that can be used for a specific operation on an install.

    The endpoint filters roles based on the operation type:
    - **provision/reprovision**: Custom roles, break glass roles, provision IAM role
    - **deprovision/teardown**: Custom roles, break glass roles, deprovision IAM role
    - **deploy**: Custom roles, break glass roles, maintenance IAM role
    - **trigger** (actions): Custom roles, break glass roles, provision + maintenance IAM roles

    Roles are sourced from the install's stack outputs.

    Args:
        install_id (str):
        principal_type (GetAvailableRolesPrincipalType | Unset):
        operation_type (GetAvailableRolesOperationType | Unset):
        principal_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceAvailableRolesResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        principal_type=principal_type,
        operation_type=operation_type,
        principal_id=principal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    principal_type: GetAvailableRolesPrincipalType | Unset = UNSET,
    operation_type: GetAvailableRolesOperationType | Unset = UNSET,
    principal_id: str | Unset = UNSET,
) -> ServiceAvailableRolesResponse | StderrErrResponse | None:
    """get available IAM roles for a specific operation

     Returns a list of available IAM roles that can be used for a specific operation on an install.

    The endpoint filters roles based on the operation type:
    - **provision/reprovision**: Custom roles, break glass roles, provision IAM role
    - **deprovision/teardown**: Custom roles, break glass roles, deprovision IAM role
    - **deploy**: Custom roles, break glass roles, maintenance IAM role
    - **trigger** (actions): Custom roles, break glass roles, provision + maintenance IAM roles

    Roles are sourced from the install's stack outputs.

    Args:
        install_id (str):
        principal_type (GetAvailableRolesPrincipalType | Unset):
        operation_type (GetAvailableRolesOperationType | Unset):
        principal_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceAvailableRolesResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            principal_type=principal_type,
            operation_type=operation_type,
            principal_id=principal_id,
        )
    ).parsed
