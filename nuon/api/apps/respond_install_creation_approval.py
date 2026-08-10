from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.respond_install_creation_approval_response_202 import RespondInstallCreationApprovalResponse202
from ...models.service_respond_install_creation_approval_request import ServiceRespondInstallCreationApprovalRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    sync_id: str,
    approval_id: str,
    *,
    body: ServiceRespondInstallCreationApprovalRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_id}/install-syncs/{sync_id}/approvals/{approval_id}/response".format(
            app_id=quote(str(app_id), safe=""),
            sync_id=quote(str(sync_id), safe=""),
            approval_id=quote(str(approval_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RespondInstallCreationApprovalResponse202 | StderrErrResponse | None:
    if response.status_code == 202:
        response_202 = RespondInstallCreationApprovalResponse202.from_dict(response.json())

        return response_202

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
) -> Response[RespondInstallCreationApprovalResponse202 | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    sync_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRespondInstallCreationApprovalRequest,
) -> Response[RespondInstallCreationApprovalResponse202 | StderrErrResponse]:
    """respond to an install creation approval

     Approves or denies an install creation approval. On approve, creates the missing installs and re-
    triggers the sync. On deny, marks the approval as denied.

    Args:
        app_id (str):
        sync_id (str):
        approval_id (str):
        body (ServiceRespondInstallCreationApprovalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RespondInstallCreationApprovalResponse202 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        sync_id=sync_id,
        approval_id=approval_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    sync_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRespondInstallCreationApprovalRequest,
) -> RespondInstallCreationApprovalResponse202 | StderrErrResponse | None:
    """respond to an install creation approval

     Approves or denies an install creation approval. On approve, creates the missing installs and re-
    triggers the sync. On deny, marks the approval as denied.

    Args:
        app_id (str):
        sync_id (str):
        approval_id (str):
        body (ServiceRespondInstallCreationApprovalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RespondInstallCreationApprovalResponse202 | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        sync_id=sync_id,
        approval_id=approval_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    sync_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRespondInstallCreationApprovalRequest,
) -> Response[RespondInstallCreationApprovalResponse202 | StderrErrResponse]:
    """respond to an install creation approval

     Approves or denies an install creation approval. On approve, creates the missing installs and re-
    triggers the sync. On deny, marks the approval as denied.

    Args:
        app_id (str):
        sync_id (str):
        approval_id (str):
        body (ServiceRespondInstallCreationApprovalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RespondInstallCreationApprovalResponse202 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        sync_id=sync_id,
        approval_id=approval_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    sync_id: str,
    approval_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRespondInstallCreationApprovalRequest,
) -> RespondInstallCreationApprovalResponse202 | StderrErrResponse | None:
    """respond to an install creation approval

     Approves or denies an install creation approval. On approve, creates the missing installs and re-
    triggers the sync. On deny, marks the approval as denied.

    Args:
        app_id (str):
        sync_id (str):
        approval_id (str):
        body (ServiceRespondInstallCreationApprovalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RespondInstallCreationApprovalResponse202 | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            sync_id=sync_id,
            approval_id=approval_id,
            client=client,
            body=body,
        )
    ).parsed
