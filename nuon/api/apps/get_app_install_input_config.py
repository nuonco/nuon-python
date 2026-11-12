from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_app_input_config import AppAppInputConfig
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    app_branch_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["app_branch_id"] = app_branch_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/install-input-config".format(
            app_id=quote(str(app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AppAppInputConfig | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAppInputConfig.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AppAppInputConfig | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    app_branch_id: str | Unset = UNSET,
) -> Response[AppAppInputConfig | StderrErrResponse]:
    """get the input config a new install would be created with

     Returns the input config that a new install would be created with for this app, optionally pinned to
    an app branch. Unlike `input-latest-config`, which always returns the newest input config of any
    kind, this endpoint mirrors the server's install-creation rules: without an `app_branch_id` it
    returns the latest config from `nuon apps sync`, and with one it returns the branch's latest
    deployable config.

    Args:
        app_id (str):
        app_branch_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppInputConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    app_branch_id: str | Unset = UNSET,
) -> AppAppInputConfig | StderrErrResponse | None:
    """get the input config a new install would be created with

     Returns the input config that a new install would be created with for this app, optionally pinned to
    an app branch. Unlike `input-latest-config`, which always returns the newest input config of any
    kind, this endpoint mirrors the server's install-creation rules: without an `app_branch_id` it
    returns the latest config from `nuon apps sync`, and with one it returns the branch's latest
    deployable config.

    Args:
        app_id (str):
        app_branch_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppInputConfig | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        app_branch_id=app_branch_id,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    app_branch_id: str | Unset = UNSET,
) -> Response[AppAppInputConfig | StderrErrResponse]:
    """get the input config a new install would be created with

     Returns the input config that a new install would be created with for this app, optionally pinned to
    an app branch. Unlike `input-latest-config`, which always returns the newest input config of any
    kind, this endpoint mirrors the server's install-creation rules: without an `app_branch_id` it
    returns the latest config from `nuon apps sync`, and with one it returns the branch's latest
    deployable config.

    Args:
        app_id (str):
        app_branch_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppInputConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    app_branch_id: str | Unset = UNSET,
) -> AppAppInputConfig | StderrErrResponse | None:
    """get the input config a new install would be created with

     Returns the input config that a new install would be created with for this app, optionally pinned to
    an app branch. Unlike `input-latest-config`, which always returns the newest input config of any
    kind, this endpoint mirrors the server's install-creation rules: without an `app_branch_id` it
    returns the latest config from `nuon apps sync`, and with one it returns the branch's latest
    deployable config.

    Args:
        app_id (str):
        app_branch_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppInputConfig | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            app_branch_id=app_branch_id,
        )
    ).parsed
