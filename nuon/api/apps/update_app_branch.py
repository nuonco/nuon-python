from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_app_branch import AppAppBranch
from ...models.service_update_app_branch_request import ServiceUpdateAppBranchRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    app_branch_id: str,
    *,
    body: ServiceUpdateAppBranchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/apps/{app_id}/branches/{app_branch_id}".format(
            app_id=quote(str(app_id), safe=""),
            app_branch_id=quote(str(app_branch_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAppBranch | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAppBranch.from_dict(response.json())

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
) -> Response[AppAppBranch | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateAppBranchRequest,
) -> Response[AppAppBranch | StderrErrResponse]:
    """update app branch metadata

     Updates app branch metadata (name only). To update configuration, create a new AppBranchConfig via
    POST /branches/:id/configs

    Args:
        app_id (str):
        app_branch_id (str):
        body (ServiceUpdateAppBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppBranch | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateAppBranchRequest,
) -> AppAppBranch | StderrErrResponse | None:
    """update app branch metadata

     Updates app branch metadata (name only). To update configuration, create a new AppBranchConfig via
    POST /branches/:id/configs

    Args:
        app_id (str):
        app_branch_id (str):
        body (ServiceUpdateAppBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppBranch | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        app_branch_id=app_branch_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateAppBranchRequest,
) -> Response[AppAppBranch | StderrErrResponse]:
    """update app branch metadata

     Updates app branch metadata (name only). To update configuration, create a new AppBranchConfig via
    POST /branches/:id/configs

    Args:
        app_id (str):
        app_branch_id (str):
        body (ServiceUpdateAppBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppBranch | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    app_branch_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateAppBranchRequest,
) -> AppAppBranch | StderrErrResponse | None:
    """update app branch metadata

     Updates app branch metadata (name only). To update configuration, create a new AppBranchConfig via
    POST /branches/:id/configs

    Args:
        app_id (str):
        app_branch_id (str):
        body (ServiceUpdateAppBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppBranch | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            app_branch_id=app_branch_id,
            client=client,
            body=body,
        )
    ).parsed
