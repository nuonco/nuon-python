from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_component_release import AppComponentRelease
from ...models.service_create_component_release_request import ServiceCreateComponentReleaseRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    component_id: str,
    *,
    body: ServiceCreateComponentReleaseRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/components/{component_id}/releases",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppComponentRelease | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppComponentRelease.from_dict(response.json())

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
) -> Response[AppComponentRelease | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateComponentReleaseRequest,
) -> Response[AppComponentRelease | StderrErrResponse]:
    """create a release

    Args:
        component_id (str):
        body (ServiceCreateComponentReleaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppComponentRelease | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateComponentReleaseRequest,
) -> AppComponentRelease | StderrErrResponse | None:
    """create a release

    Args:
        component_id (str):
        body (ServiceCreateComponentReleaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppComponentRelease | StderrErrResponse
    """

    return sync_detailed(
        component_id=component_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateComponentReleaseRequest,
) -> Response[AppComponentRelease | StderrErrResponse]:
    """create a release

    Args:
        component_id (str):
        body (ServiceCreateComponentReleaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppComponentRelease | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateComponentReleaseRequest,
) -> AppComponentRelease | StderrErrResponse | None:
    """create a release

    Args:
        component_id (str):
        body (ServiceCreateComponentReleaseRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppComponentRelease | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            component_id=component_id,
            client=client,
            body=body,
        )
    ).parsed
