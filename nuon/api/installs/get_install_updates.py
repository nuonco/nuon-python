from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_install_updates_response import ServiceInstallUpdatesResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/updates".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceInstallUpdatesResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallUpdatesResponse.from_dict(response.json())

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
) -> Response[ServiceInstallUpdatesResponse | StderrErrResponse]:
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
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[ServiceInstallUpdatesResponse | StderrErrResponse]:
    """get typed updates for an install

     Returns app config, input, stack, and install config updates in reverse chronological order.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallUpdatesResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
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
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> ServiceInstallUpdatesResponse | StderrErrResponse | None:
    """get typed updates for an install

     Returns app config, input, stack, and install config updates in reverse chronological order.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallUpdatesResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        page=page,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[ServiceInstallUpdatesResponse | StderrErrResponse]:
    """get typed updates for an install

     Returns app config, input, stack, and install config updates in reverse chronological order.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallUpdatesResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> ServiceInstallUpdatesResponse | StderrErrResponse | None:
    """get typed updates for an install

     Returns app config, input, stack, and install config updates in reverse chronological order.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallUpdatesResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            page=page,
            offset=offset,
            limit=limit,
        )
    ).parsed
