from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_workflow import AppWorkflow
from ...models.service_update_workflow_request import ServiceUpdateWorkflowRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_workflow_id: str,
    *,
    body: ServiceUpdateWorkflowRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/install-workflows/{install_workflow_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppWorkflow, StderrErrResponse]]:
    if response.status_code == 200:
        response_200 = AppWorkflow.from_dict(response.json())

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
) -> Response[Union[AppWorkflow, StderrErrResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateWorkflowRequest,
) -> Response[Union[AppWorkflow, StderrErrResponse]]:
    """update an install workflow

    Args:
        install_workflow_id (str):
        body (ServiceUpdateWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppWorkflow, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        install_workflow_id=install_workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateWorkflowRequest,
) -> Optional[Union[AppWorkflow, StderrErrResponse]]:
    """update an install workflow

    Args:
        install_workflow_id (str):
        body (ServiceUpdateWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppWorkflow, StderrErrResponse]
    """

    return sync_detailed(
        install_workflow_id=install_workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateWorkflowRequest,
) -> Response[Union[AppWorkflow, StderrErrResponse]]:
    """update an install workflow

    Args:
        install_workflow_id (str):
        body (ServiceUpdateWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppWorkflow, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        install_workflow_id=install_workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateWorkflowRequest,
) -> Optional[Union[AppWorkflow, StderrErrResponse]]:
    """update an install workflow

    Args:
        install_workflow_id (str):
        body (ServiceUpdateWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppWorkflow, StderrErrResponse]
    """

    return (
        await asyncio_detailed(
            install_workflow_id=install_workflow_id,
            client=client,
            body=body,
        )
    ).parsed
