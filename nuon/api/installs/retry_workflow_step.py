from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_retry_workflow_by_id_response import ServiceRetryWorkflowByIDResponse
from ...models.service_retry_workflow_step_request import ServiceRetryWorkflowStepRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    step_id: str,
    *,
    body: ServiceRetryWorkflowStepRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{workflow_id}/steps/{step_id}/retry".format(
            workflow_id=quote(str(workflow_id), safe=""),
            step_id=quote(str(step_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceRetryWorkflowByIDResponse | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = ServiceRetryWorkflowByIDResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceRetryWorkflowByIDResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    step_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRetryWorkflowStepRequest,
) -> Response[ServiceRetryWorkflowByIDResponse | StderrErrResponse]:
    """rerun the workflow steps starting from input step id, can be used to retry a failed step

     Retry a workflow execution by id.

    Args:
        workflow_id (str):
        step_id (str):
        body (ServiceRetryWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceRetryWorkflowByIDResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        step_id=step_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    step_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRetryWorkflowStepRequest,
) -> ServiceRetryWorkflowByIDResponse | StderrErrResponse | None:
    """rerun the workflow steps starting from input step id, can be used to retry a failed step

     Retry a workflow execution by id.

    Args:
        workflow_id (str):
        step_id (str):
        body (ServiceRetryWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceRetryWorkflowByIDResponse | StderrErrResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        step_id=step_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    step_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRetryWorkflowStepRequest,
) -> Response[ServiceRetryWorkflowByIDResponse | StderrErrResponse]:
    """rerun the workflow steps starting from input step id, can be used to retry a failed step

     Retry a workflow execution by id.

    Args:
        workflow_id (str):
        step_id (str):
        body (ServiceRetryWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceRetryWorkflowByIDResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        step_id=step_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    step_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRetryWorkflowStepRequest,
) -> ServiceRetryWorkflowByIDResponse | StderrErrResponse | None:
    """rerun the workflow steps starting from input step id, can be used to retry a failed step

     Retry a workflow execution by id.

    Args:
        workflow_id (str):
        step_id (str):
        body (ServiceRetryWorkflowStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceRetryWorkflowByIDResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            step_id=step_id,
            client=client,
            body=body,
        )
    ).parsed
