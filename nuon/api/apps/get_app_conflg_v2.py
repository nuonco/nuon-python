from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_app_config import AppAppConfig
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    config_id: str,
    *,
    recurse: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["recurse"] = recurse

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/configs/{config_id}".format(
            app_id=quote(str(app_id), safe=""),
            config_id=quote(str(config_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAppConfig | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAppConfig.from_dict(response.json())

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
) -> Response[AppAppConfig | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
    recurse: bool | Unset = False,
) -> Response[AppAppConfig | StderrErrResponse]:
    """get an app config

     Fetch an app config by id.

    Args:
        app_id (str):
        config_id (str):
        recurse (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        config_id=config_id,
        recurse=recurse,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
    recurse: bool | Unset = False,
) -> AppAppConfig | StderrErrResponse | None:
    """get an app config

     Fetch an app config by id.

    Args:
        app_id (str):
        config_id (str):
        recurse (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppConfig | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        config_id=config_id,
        client=client,
        recurse=recurse,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
    recurse: bool | Unset = False,
) -> Response[AppAppConfig | StderrErrResponse]:
    """get an app config

     Fetch an app config by id.

    Args:
        app_id (str):
        config_id (str):
        recurse (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        config_id=config_id,
        recurse=recurse,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
    recurse: bool | Unset = False,
) -> AppAppConfig | StderrErrResponse | None:
    """get an app config

     Fetch an app config by id.

    Args:
        app_id (str):
        config_id (str):
        recurse (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppConfig | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            config_id=config_id,
            client=client,
            recurse=recurse,
        )
    ).parsed
