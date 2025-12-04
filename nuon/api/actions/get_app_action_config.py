from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_action_workflow_config import AppActionWorkflowConfig
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    action_id: str,
    action_config_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/actions/{action_id}/configs/{action_config_id}".format(
            app_id=quote(str(app_id), safe=""),
            action_id=quote(str(action_id), safe=""),
            action_config_id=quote(str(action_config_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppActionWorkflowConfig | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppActionWorkflowConfig.from_dict(response.json())

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
) -> Response[AppActionWorkflowConfig | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    action_id: str,
    action_config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppActionWorkflowConfig | StderrErrResponse]:
    """get an app action config

    Args:
        app_id (str):
        action_id (str):
        action_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppActionWorkflowConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        action_id=action_id,
        action_config_id=action_config_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    action_id: str,
    action_config_id: str,
    *,
    client: AuthenticatedClient,
) -> AppActionWorkflowConfig | StderrErrResponse | None:
    """get an app action config

    Args:
        app_id (str):
        action_id (str):
        action_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppActionWorkflowConfig | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        action_id=action_id,
        action_config_id=action_config_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    action_id: str,
    action_config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppActionWorkflowConfig | StderrErrResponse]:
    """get an app action config

    Args:
        app_id (str):
        action_id (str):
        action_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppActionWorkflowConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        action_id=action_id,
        action_config_id=action_config_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    action_id: str,
    action_config_id: str,
    *,
    client: AuthenticatedClient,
) -> AppActionWorkflowConfig | StderrErrResponse | None:
    """get an app action config

    Args:
        app_id (str):
        action_id (str):
        action_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppActionWorkflowConfig | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            action_id=action_id,
            action_config_id=action_config_id,
            client=client,
        )
    ).parsed
