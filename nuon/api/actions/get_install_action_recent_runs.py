from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_action_workflow import AppInstallActionWorkflow
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    action_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/installs/{install_id}/actions/{action_id}/recent-runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppInstallActionWorkflow | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppInstallActionWorkflow.from_dict(response.json())

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
) -> Response[AppInstallActionWorkflow | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> Response[AppInstallActionWorkflow | StderrErrResponse]:
    """get recent runs for an action workflow by install id

    Args:
        install_id (str):
        action_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallActionWorkflow | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        action_id=action_id,
        offset=offset,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> AppInstallActionWorkflow | StderrErrResponse | None:
    """get recent runs for an action workflow by install id

    Args:
        install_id (str):
        action_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallActionWorkflow | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        action_id=action_id,
        client=client,
        offset=offset,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> Response[AppInstallActionWorkflow | StderrErrResponse]:
    """get recent runs for an action workflow by install id

    Args:
        install_id (str):
        action_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallActionWorkflow | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        action_id=action_id,
        offset=offset,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> AppInstallActionWorkflow | StderrErrResponse | None:
    """get recent runs for an action workflow by install id

    Args:
        install_id (str):
        action_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallActionWorkflow | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            action_id=action_id,
            client=client,
            offset=offset,
            limit=limit,
            page=page,
        )
    ).parsed
