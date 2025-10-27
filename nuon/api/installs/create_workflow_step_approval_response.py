from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_create_workflow_step_approval_response_request import (
    ServiceCreateWorkflowStepApprovalResponseRequest,
)
from ...models.service_create_workflow_step_approval_response_response import (
    ServiceCreateWorkflowStepApprovalResponseResponse,
)
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    workflow_step_id: str,
    approval_id: str,
    *,
    body: ServiceCreateWorkflowStepApprovalResponseRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/workflows/{workflow_id}/steps/{workflow_step_id}/approvals/{approval_id}/response",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]:
    if response.status_code == 201:
        response_201 = ServiceCreateWorkflowStepApprovalResponseResponse.from_dict(response.json())

        return response_201
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
) -> Response[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    workflow_step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateWorkflowStepApprovalResponseRequest,
) -> Response[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]:
    """Create an approval response for a workflow step.

     Create a response for an approval for an action workflow step.

    Args:
        workflow_id (str):
        workflow_step_id (str):
        approval_id (str):
        body (ServiceCreateWorkflowStepApprovalResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        workflow_step_id=workflow_step_id,
        approval_id=approval_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    workflow_step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateWorkflowStepApprovalResponseRequest,
) -> Optional[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]:
    """Create an approval response for a workflow step.

     Create a response for an approval for an action workflow step.

    Args:
        workflow_id (str):
        workflow_step_id (str):
        approval_id (str):
        body (ServiceCreateWorkflowStepApprovalResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        workflow_step_id=workflow_step_id,
        approval_id=approval_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    workflow_step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateWorkflowStepApprovalResponseRequest,
) -> Response[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]:
    """Create an approval response for a workflow step.

     Create a response for an approval for an action workflow step.

    Args:
        workflow_id (str):
        workflow_step_id (str):
        approval_id (str):
        body (ServiceCreateWorkflowStepApprovalResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        workflow_step_id=workflow_step_id,
        approval_id=approval_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    workflow_step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateWorkflowStepApprovalResponseRequest,
) -> Optional[Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]]:
    """Create an approval response for a workflow step.

     Create a response for an approval for an action workflow step.

    Args:
        workflow_id (str):
        workflow_step_id (str):
        approval_id (str):
        body (ServiceCreateWorkflowStepApprovalResponseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ServiceCreateWorkflowStepApprovalResponseResponse, StderrErrResponse]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            workflow_step_id=workflow_step_id,
            approval_id=approval_id,
            client=client,
            body=body,
        )
    ).parsed
