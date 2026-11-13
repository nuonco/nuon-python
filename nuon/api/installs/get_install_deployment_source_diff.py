from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_install_deployment_source_diff_kind import GetInstallDeploymentSourceDiffKind
from ...models.service_install_deployment_source_diff import ServiceInstallDeploymentSourceDiff
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response


def _get_kwargs(
    install_id: str,
    workflow_id: str,
    *,
    kind: GetInstallDeploymentSourceDiffKind,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_kind = kind.value
    params["kind"] = json_kind

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/deployments/{workflow_id}/source-diff".format(
            install_id=quote(str(install_id), safe=""),
            workflow_id=quote(str(workflow_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ServiceInstallDeploymentSourceDiff | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallDeploymentSourceDiff.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ServiceInstallDeploymentSourceDiff | StderrErrResponse]:
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
    kind: GetInstallDeploymentSourceDiffKind,
    name: str,
) -> Response[ServiceInstallDeploymentSourceDiff | StderrErrResponse]:
    """get the GitHub compare link for a deployment resource

     Returns a GitHub compare URL between the commits of the resource's build for the install's pinned
    app config and its build for this deployment's app config. The URL is empty when the builds are not
    in the same GitHub repository, use the same commit, or have the same source digest. Nuon does not
    read the repository for this response.

    Args:
        install_id (str):
        workflow_id (str):
        kind (GetInstallDeploymentSourceDiffKind):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallDeploymentSourceDiff | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        workflow_id=workflow_id,
        kind=kind,
        name=name,
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
    kind: GetInstallDeploymentSourceDiffKind,
    name: str,
) -> ServiceInstallDeploymentSourceDiff | StderrErrResponse | None:
    """get the GitHub compare link for a deployment resource

     Returns a GitHub compare URL between the commits of the resource's build for the install's pinned
    app config and its build for this deployment's app config. The URL is empty when the builds are not
    in the same GitHub repository, use the same commit, or have the same source digest. Nuon does not
    read the repository for this response.

    Args:
        install_id (str):
        workflow_id (str):
        kind (GetInstallDeploymentSourceDiffKind):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallDeploymentSourceDiff | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        workflow_id=workflow_id,
        client=client,
        kind=kind,
        name=name,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    kind: GetInstallDeploymentSourceDiffKind,
    name: str,
) -> Response[ServiceInstallDeploymentSourceDiff | StderrErrResponse]:
    """get the GitHub compare link for a deployment resource

     Returns a GitHub compare URL between the commits of the resource's build for the install's pinned
    app config and its build for this deployment's app config. The URL is empty when the builds are not
    in the same GitHub repository, use the same commit, or have the same source digest. Nuon does not
    read the repository for this response.

    Args:
        install_id (str):
        workflow_id (str):
        kind (GetInstallDeploymentSourceDiffKind):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallDeploymentSourceDiff | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        workflow_id=workflow_id,
        kind=kind,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    kind: GetInstallDeploymentSourceDiffKind,
    name: str,
) -> ServiceInstallDeploymentSourceDiff | StderrErrResponse | None:
    """get the GitHub compare link for a deployment resource

     Returns a GitHub compare URL between the commits of the resource's build for the install's pinned
    app config and its build for this deployment's app config. The URL is empty when the builds are not
    in the same GitHub repository, use the same commit, or have the same source digest. Nuon does not
    read the repository for this response.

    Args:
        install_id (str):
        workflow_id (str):
        kind (GetInstallDeploymentSourceDiffKind):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallDeploymentSourceDiff | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            workflow_id=workflow_id,
            client=client,
            kind=kind,
            name=name,
        )
    ).parsed
