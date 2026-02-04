from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_workflow_step import AppWorkflowStep
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_workflow_id: str,
    install_workflow_step_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/install-workflows/{install_workflow_id}/steps/{install_workflow_step_id}".format(
            install_workflow_id=quote(str(install_workflow_id), safe=""),
            install_workflow_step_id=quote(str(install_workflow_step_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppWorkflowStep | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppWorkflowStep.from_dict(response.json())

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
) -> Response[AppWorkflowStep | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_workflow_id: str,
    install_workflow_step_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppWorkflowStep | StderrErrResponse]:
    """get an install workflow step

     Return a single workflow step.

    Args:
        install_workflow_id (str):
        install_workflow_step_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppWorkflowStep | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_workflow_id=install_workflow_id,
        install_workflow_step_id=install_workflow_step_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_workflow_id: str,
    install_workflow_step_id: str,
    *,
    client: AuthenticatedClient,
) -> AppWorkflowStep | StderrErrResponse | None:
    """get an install workflow step

     Return a single workflow step.

    Args:
        install_workflow_id (str):
        install_workflow_step_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppWorkflowStep | StderrErrResponse
    """

    return sync_detailed(
        install_workflow_id=install_workflow_id,
        install_workflow_step_id=install_workflow_step_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_workflow_id: str,
    install_workflow_step_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppWorkflowStep | StderrErrResponse]:
    """get an install workflow step

     Return a single workflow step.

    Args:
        install_workflow_id (str):
        install_workflow_step_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppWorkflowStep | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_workflow_id=install_workflow_id,
        install_workflow_step_id=install_workflow_step_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_workflow_id: str,
    install_workflow_step_id: str,
    *,
    client: AuthenticatedClient,
) -> AppWorkflowStep | StderrErrResponse | None:
    """get an install workflow step

     Return a single workflow step.

    Args:
        install_workflow_id (str):
        install_workflow_step_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppWorkflowStep | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_workflow_id=install_workflow_id,
            install_workflow_step_id=install_workflow_step_id,
            client=client,
        )
    ).parsed
