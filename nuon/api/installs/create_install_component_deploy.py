from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_deploy import AppInstallDeploy
from ...models.service_create_install_component_deploy_request import ServiceCreateInstallComponentDeployRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    component_id: str,
    *,
    body: ServiceCreateInstallComponentDeployRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/installs/{install_id}/components/{component_id}/deploys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppInstallDeploy | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppInstallDeploy.from_dict(response.json())

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
) -> Response[AppInstallDeploy | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateInstallComponentDeployRequest,
) -> Response[AppInstallDeploy | StderrErrResponse]:
    """deploy a build to an install

    Args:
        install_id (str):
        component_id (str):
        body (ServiceCreateInstallComponentDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallDeploy | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateInstallComponentDeployRequest,
) -> AppInstallDeploy | StderrErrResponse | None:
    """deploy a build to an install

    Args:
        install_id (str):
        component_id (str):
        body (ServiceCreateInstallComponentDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallDeploy | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        component_id=component_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateInstallComponentDeployRequest,
) -> Response[AppInstallDeploy | StderrErrResponse]:
    """deploy a build to an install

    Args:
        install_id (str):
        component_id (str):
        body (ServiceCreateInstallComponentDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallDeploy | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateInstallComponentDeployRequest,
) -> AppInstallDeploy | StderrErrResponse | None:
    """deploy a build to an install

    Args:
        install_id (str):
        component_id (str):
        body (ServiceCreateInstallComponentDeployRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallDeploy | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            component_id=component_id,
            client=client,
            body=body,
        )
    ).parsed
