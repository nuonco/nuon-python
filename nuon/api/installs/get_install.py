from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install import AppInstall
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    include_drifted_objects: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_drifted_objects"] = include_drifted_objects

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppInstall | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppInstall.from_dict(response.json())

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
) -> Response[AppInstall | StderrErrResponse]:
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
    include_drifted_objects: bool | Unset = False,
) -> Response[AppInstall | StderrErrResponse]:
    """get an install

     Return an install by id.

    Args:
        install_id (str):
        include_drifted_objects (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstall | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        include_drifted_objects=include_drifted_objects,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    include_drifted_objects: bool | Unset = False,
) -> AppInstall | StderrErrResponse | None:
    """get an install

     Return an install by id.

    Args:
        install_id (str):
        include_drifted_objects (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstall | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        include_drifted_objects=include_drifted_objects,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    include_drifted_objects: bool | Unset = False,
) -> Response[AppInstall | StderrErrResponse]:
    """get an install

     Return an install by id.

    Args:
        install_id (str):
        include_drifted_objects (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstall | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        include_drifted_objects=include_drifted_objects,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    include_drifted_objects: bool | Unset = False,
) -> AppInstall | StderrErrResponse | None:
    """get an install

     Return an install by id.

    Args:
        install_id (str):
        include_drifted_objects (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstall | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            include_drifted_objects=include_drifted_objects,
        )
    ).parsed
