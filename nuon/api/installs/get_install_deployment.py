from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_install_deployment import ServiceInstallDeployment
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    workflow_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/deployments/{workflow_id}".format(
            install_id=quote(str(install_id), safe=""),
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceInstallDeployment | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallDeployment.from_dict(response.json())

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
) -> Response[ServiceInstallDeployment | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceInstallDeployment | StderrErrResponse]:
    """get a single normalized deployment for an install

     Returns one normalized deployment record for an install, identified by its backing workflow ID.

    The record includes the `app_branch` reference, image changes, `affected_resources`, and
    `change_groups` derived from the install's app config diff. Use the deployments feed for lightweight
    overview rows.

    Args:
        install_id (str):
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallDeployment | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        workflow_id=workflow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceInstallDeployment | StderrErrResponse | None:
    """get a single normalized deployment for an install

     Returns one normalized deployment record for an install, identified by its backing workflow ID.

    The record includes the `app_branch` reference, image changes, `affected_resources`, and
    `change_groups` derived from the install's app config diff. Use the deployments feed for lightweight
    overview rows.

    Args:
        install_id (str):
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallDeployment | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceInstallDeployment | StderrErrResponse]:
    """get a single normalized deployment for an install

     Returns one normalized deployment record for an install, identified by its backing workflow ID.

    The record includes the `app_branch` reference, image changes, `affected_resources`, and
    `change_groups` derived from the install's app config diff. Use the deployments feed for lightweight
    overview rows.

    Args:
        install_id (str):
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallDeployment | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        workflow_id=workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceInstallDeployment | StderrErrResponse | None:
    """get a single normalized deployment for an install

     Returns one normalized deployment record for an install, identified by its backing workflow ID.

    The record includes the `app_branch` reference, image changes, `affected_resources`, and
    `change_groups` derived from the install's app config diff. Use the deployments feed for lightweight
    overview rows.

    Args:
        install_id (str):
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallDeployment | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
