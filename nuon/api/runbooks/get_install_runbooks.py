from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_runbook import AppInstallRunbook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/runbooks".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[AppInstallRunbook] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppInstallRunbook.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AppInstallRunbook]]:
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
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[list[AppInstallRunbook]]:
    """get runbooks for an install

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppInstallRunbook]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> list[AppInstallRunbook] | None:
    """get runbooks for an install

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppInstallRunbook]
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[list[AppInstallRunbook]]:
    """get runbooks for an install

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppInstallRunbook]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> list[AppInstallRunbook] | None:
    """get runbooks for an install

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppInstallRunbook]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
