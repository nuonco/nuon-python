from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_workflow_step_approval import AppWorkflowStepApproval
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    step_id: str,
    approval_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/{workflow_id}/steps/{step_id}/approvals/{approval_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
            step_id=quote(str(step_id), safe=""),
            approval_id=quote(str(approval_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppWorkflowStepApproval | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppWorkflowStepApproval.from_dict(response.json())

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
) -> Response[AppWorkflowStepApproval | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppWorkflowStepApproval | StderrErrResponse]:
    """get an workflow step approval

     Return a workflow step approval by id.

    Args:
        workflow_id (str):
        step_id (str):
        approval_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppWorkflowStepApproval | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        step_id=step_id,
        approval_id=approval_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
) -> AppWorkflowStepApproval | StderrErrResponse | None:
    """get an workflow step approval

     Return a workflow step approval by id.

    Args:
        workflow_id (str):
        step_id (str):
        approval_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppWorkflowStepApproval | StderrErrResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        step_id=step_id,
        approval_id=approval_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppWorkflowStepApproval | StderrErrResponse]:
    """get an workflow step approval

     Return a workflow step approval by id.

    Args:
        workflow_id (str):
        step_id (str):
        approval_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppWorkflowStepApproval | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        step_id=step_id,
        approval_id=approval_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    step_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
) -> AppWorkflowStepApproval | StderrErrResponse | None:
    """get an workflow step approval

     Return a workflow step approval by id.

    Args:
        workflow_id (str):
        step_id (str):
        approval_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppWorkflowStepApproval | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            step_id=step_id,
            approval_id=approval_id,
            client=client,
        )
    ).parsed
