from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_terraform_state_resource import AppTerraformStateResource
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    state_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/runners/terraform-workspace/{workspace_id}/states/{state_id}/resources",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppTerraformStateResource] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppTerraformStateResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[StderrErrResponse | list[AppTerraformStateResource]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StderrErrResponse | list[AppTerraformStateResource]]:
    """get terraform state resources

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppTerraformStateResource]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        state_id=state_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | list[AppTerraformStateResource] | None:
    """get terraform state resources

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppTerraformStateResource]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        state_id=state_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StderrErrResponse | list[AppTerraformStateResource]]:
    """get terraform state resources

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppTerraformStateResource]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        state_id=state_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | list[AppTerraformStateResource] | None:
    """get terraform state resources

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppTerraformStateResource]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            state_id=state_id,
            client=client,
        )
    ).parsed
