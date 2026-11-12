from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_setup_response import ServiceSetupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_id: str,
    *,
    repository: list[str] | Unset = UNSET,
    existing_principal: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_repository: list[str] | Unset = UNSET
    if not isinstance(repository, Unset):
        json_repository = repository

    params["repository"] = json_repository

    params["existing_principal"] = existing_principal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cloud-connections/{connection_id}/setup".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> ServiceSetupResponse | None:
    if response.status_code == 200:
        response_200 = ServiceSetupResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ServiceSetupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    repository: list[str] | Unset = UNSET,
    existing_principal: bool | Unset = False,
) -> Response[ServiceSetupResponse]:
    """get cloud connection setup material

    Args:
        connection_id (str):
        repository (list[str] | Unset):
        existing_principal (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceSetupResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        repository=repository,
        existing_principal=existing_principal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    repository: list[str] | Unset = UNSET,
    existing_principal: bool | Unset = False,
) -> ServiceSetupResponse | None:
    """get cloud connection setup material

    Args:
        connection_id (str):
        repository (list[str] | Unset):
        existing_principal (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceSetupResponse
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        repository=repository,
        existing_principal=existing_principal,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    repository: list[str] | Unset = UNSET,
    existing_principal: bool | Unset = False,
) -> Response[ServiceSetupResponse]:
    """get cloud connection setup material

    Args:
        connection_id (str):
        repository (list[str] | Unset):
        existing_principal (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceSetupResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        repository=repository,
        existing_principal=existing_principal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    repository: list[str] | Unset = UNSET,
    existing_principal: bool | Unset = False,
) -> ServiceSetupResponse | None:
    """get cloud connection setup material

    Args:
        connection_id (str):
        repository (list[str] | Unset):
        existing_principal (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceSetupResponse
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            repository=repository,
            existing_principal=existing_principal,
        )
    ).parsed
