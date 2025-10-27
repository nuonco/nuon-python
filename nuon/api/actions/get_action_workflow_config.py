from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_action_workflow_config import AppActionWorkflowConfig
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    action_workflow_config_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/action-workflows/configs/{action_workflow_config_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppActionWorkflowConfig, StderrErrResponse]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AppActionWorkflowConfig, StderrErrResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_workflow_config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AppActionWorkflowConfig, StderrErrResponse]]:
    """get an app action workflow config

    Args:
        action_workflow_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppActionWorkflowConfig, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        action_workflow_config_id=action_workflow_config_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_workflow_config_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AppActionWorkflowConfig, StderrErrResponse]]:
    """get an app action workflow config

    Args:
        action_workflow_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppActionWorkflowConfig, StderrErrResponse]
    """

    return sync_detailed(
        action_workflow_config_id=action_workflow_config_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    action_workflow_config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AppActionWorkflowConfig, StderrErrResponse]]:
    """get an app action workflow config

    Args:
        action_workflow_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppActionWorkflowConfig, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        action_workflow_config_id=action_workflow_config_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_workflow_config_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AppActionWorkflowConfig, StderrErrResponse]]:
    """get an app action workflow config

    Args:
        action_workflow_config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppActionWorkflowConfig, StderrErrResponse]
    """

    return (
        await asyncio_detailed(
            action_workflow_config_id=action_workflow_config_id,
            client=client,
        )
    ).parsed
