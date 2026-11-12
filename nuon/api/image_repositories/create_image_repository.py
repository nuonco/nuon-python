from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_image_repository import AppImageRepository
from ...models.service_create_image_repository_request import ServiceCreateImageRepositoryRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceCreateImageRepositoryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/image-repositories",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AppImageRepository | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppImageRepository.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = StderrErrResponse.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AppImageRepository | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateImageRepositoryRequest,
) -> Response[AppImageRepository | StderrErrResponse]:
    """register an image repository

     Save an exact ECR ARN, GAR repository resource, or ACR repository path against an existing org-owned
    image connection. Pending connections are allowed; image use requires verification. Does not change
    cloud permissions.

    Args:
        body (ServiceCreateImageRepositoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppImageRepository | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateImageRepositoryRequest,
) -> AppImageRepository | StderrErrResponse | None:
    """register an image repository

     Save an exact ECR ARN, GAR repository resource, or ACR repository path against an existing org-owned
    image connection. Pending connections are allowed; image use requires verification. Does not change
    cloud permissions.

    Args:
        body (ServiceCreateImageRepositoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppImageRepository | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateImageRepositoryRequest,
) -> Response[AppImageRepository | StderrErrResponse]:
    """register an image repository

     Save an exact ECR ARN, GAR repository resource, or ACR repository path against an existing org-owned
    image connection. Pending connections are allowed; image use requires verification. Does not change
    cloud permissions.

    Args:
        body (ServiceCreateImageRepositoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppImageRepository | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateImageRepositoryRequest,
) -> AppImageRepository | StderrErrResponse | None:
    """register an image repository

     Save an exact ECR ARN, GAR repository resource, or ACR repository path against an existing org-owned
    image connection. Pending connections are allowed; image use requires verification. Does not change
    cloud permissions.

    Args:
        body (ServiceCreateImageRepositoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppImageRepository | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
