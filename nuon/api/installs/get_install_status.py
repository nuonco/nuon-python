from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_install_status_response import ServiceInstallStatusResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/status".format(
            install_id=quote(str(install_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceInstallStatusResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallStatusResponse.from_dict(response.json())

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
) -> Response[ServiceInstallStatusResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceInstallStatusResponse | StderrErrResponse]:
    """install status

     Returns deployment, resource, and health-check status for an install. Each axis is a composite
    status with counts in metadata. Deployment state stays on the component lifecycle, so a failed
    deploy remains failed after the workload is repaired. Resources and health checks are the latest
    observations.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallStatusResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceInstallStatusResponse | StderrErrResponse | None:
    """install status

     Returns deployment, resource, and health-check status for an install. Each axis is a composite
    status with counts in metadata. Deployment state stays on the component lifecycle, so a failed
    deploy remains failed after the workload is repaired. Resources and health checks are the latest
    observations.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallStatusResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceInstallStatusResponse | StderrErrResponse]:
    """install status

     Returns deployment, resource, and health-check status for an install. Each axis is a composite
    status with counts in metadata. Deployment state stays on the component lifecycle, so a failed
    deploy remains failed after the workload is repaired. Resources and health checks are the latest
    observations.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallStatusResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceInstallStatusResponse | StderrErrResponse | None:
    """install status

     Returns deployment, resource, and health-check status for an install. Each axis is a composite
    status with counts in metadata. Deployment state stays on the component lifecycle, so a failed
    deploy remains failed after the workload is repaired. Resources and health checks are the latest
    observations.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallStatusResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
        )
    ).parsed
