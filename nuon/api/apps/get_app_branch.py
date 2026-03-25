from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_app_branch import AppAppBranch
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    app_branch_id: str,
    *,
    latest_config: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["latest_config"] = latest_config

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/branches/{app_branch_id}".format(
            app_id=quote(str(app_id), safe=""),
            app_branch_id=quote(str(app_branch_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAppBranch | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAppBranch.from_dict(response.json())

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
) -> Response[AppAppBranch | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    latest_config: bool | Unset = False,
) -> Response[AppAppBranch | StderrErrResponse]:
    """get an app branch

     Get an app branch by ID. Use `latest_config=true` query parameter to include only the most recent
    config with its VCS settings and install groups.

    Args:
        app_id (str):
        app_branch_id (str):
        latest_config (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppBranch | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
        latest_config=latest_config,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    latest_config: bool | Unset = False,
) -> AppAppBranch | StderrErrResponse | None:
    """get an app branch

     Get an app branch by ID. Use `latest_config=true` query parameter to include only the most recent
    config with its VCS settings and install groups.

    Args:
        app_id (str):
        app_branch_id (str):
        latest_config (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppBranch | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        app_branch_id=app_branch_id,
        client=client,
        latest_config=latest_config,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    latest_config: bool | Unset = False,
) -> Response[AppAppBranch | StderrErrResponse]:
    """get an app branch

     Get an app branch by ID. Use `latest_config=true` query parameter to include only the most recent
    config with its VCS settings and install groups.

    Args:
        app_id (str):
        app_branch_id (str):
        latest_config (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppBranch | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
        latest_config=latest_config,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    latest_config: bool | Unset = False,
) -> AppAppBranch | StderrErrResponse | None:
    """get an app branch

     Get an app branch by ID. Use `latest_config=true` query parameter to include only the most recent
    config with its VCS settings and install groups.

    Args:
        app_id (str):
        app_branch_id (str):
        latest_config (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppBranch | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            app_branch_id=app_branch_id,
            client=client,
            latest_config=latest_config,
        )
    ).parsed
