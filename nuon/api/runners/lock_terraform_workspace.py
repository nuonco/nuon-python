from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_terraform_workspace_state import AppTerraformWorkspaceState
from ...models.lock_terraform_workspace_body import LockTerraformWorkspaceBody
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    body: LockTerraformWorkspaceBody,
    job_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["job_id"] = job_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/terraform-workspaces/{workspace_id}/lock",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppTerraformWorkspaceState | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppTerraformWorkspaceState.from_dict(response.json())

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
) -> Response[AppTerraformWorkspaceState | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: LockTerraformWorkspaceBody,
    job_id: str | Unset = UNSET,
) -> Response[AppTerraformWorkspaceState | StderrErrResponse]:
    """lock terraform state

    Args:
        workspace_id (str):
        job_id (str | Unset):
        body (LockTerraformWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppTerraformWorkspaceState | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: LockTerraformWorkspaceBody,
    job_id: str | Unset = UNSET,
) -> AppTerraformWorkspaceState | StderrErrResponse | None:
    """lock terraform state

    Args:
        workspace_id (str):
        job_id (str | Unset):
        body (LockTerraformWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppTerraformWorkspaceState | StderrErrResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        job_id=job_id,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: LockTerraformWorkspaceBody,
    job_id: str | Unset = UNSET,
) -> Response[AppTerraformWorkspaceState | StderrErrResponse]:
    """lock terraform state

    Args:
        workspace_id (str):
        job_id (str | Unset):
        body (LockTerraformWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppTerraformWorkspaceState | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: LockTerraformWorkspaceBody,
    job_id: str | Unset = UNSET,
) -> AppTerraformWorkspaceState | StderrErrResponse | None:
    """lock terraform state

    Args:
        workspace_id (str):
        job_id (str | Unset):
        body (LockTerraformWorkspaceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppTerraformWorkspaceState | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            job_id=job_id,
        )
    ).parsed
