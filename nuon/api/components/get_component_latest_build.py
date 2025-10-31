from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_component_build import AppComponentBuild
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    component_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/components/{component_id}/builds/latest",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppComponentBuild | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppComponentBuild.from_dict(response.json())

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
) -> Response[AppComponentBuild | StderrErrResponse]:
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
) -> Response[AppComponentBuild | StderrErrResponse]:
    """get latest build for a component

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppComponentBuild | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> AppComponentBuild | StderrErrResponse | None:
    """get latest build for a component

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppComponentBuild | StderrErrResponse
    """

    return sync_detailed(
        component_id=component_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppComponentBuild | StderrErrResponse]:
    """get latest build for a component

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppComponentBuild | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> AppComponentBuild | StderrErrResponse | None:
    """get latest build for a component

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppComponentBuild | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            component_id=component_id,
            client=client,
        )
    ).parsed
