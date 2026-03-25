from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_install_action_workflow_outputs_response_200 import GetInstallActionWorkflowOutputsResponse200
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    action_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/actions/{action_id}/outputs".format(
            install_id=quote(str(install_id), safe=""),
            action_id=quote(str(action_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = GetInstallActionWorkflowOutputsResponse200.from_dict(response.json())

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
) -> Response[GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse]:
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
) -> Response[GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse]:
    """get an install action workflow outputs

     Return the latest outputs for an action workflow.

    The action_id parameter accepts either an action workflow ID or name.

    **NOTE** requires a valid install.

    Args:
        install_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        action_id=action_id,
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
) -> GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse | None:
    """get an install action workflow outputs

     Return the latest outputs for an action workflow.

    The action_id parameter accepts either an action workflow ID or name.

    **NOTE** requires a valid install.

    Args:
        install_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        action_id=action_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse]:
    """get an install action workflow outputs

     Return the latest outputs for an action workflow.

    The action_id parameter accepts either an action workflow ID or name.

    **NOTE** requires a valid install.

    Args:
        install_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        action_id=action_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
) -> GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse | None:
    """get an install action workflow outputs

     Return the latest outputs for an action workflow.

    The action_id parameter accepts either an action workflow ID or name.

    **NOTE** requires a valid install.

    Args:
        install_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInstallActionWorkflowOutputsResponse200 | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            action_id=action_id,
            client=client,
        )
    ).parsed
