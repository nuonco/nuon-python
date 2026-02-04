from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_vcs_connection_status_response import ServiceVCSConnectionStatusResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    connection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/vcs/connections/{connection_id}/check-status".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceVCSConnectionStatusResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceVCSConnectionStatusResponse.from_dict(response.json())

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
) -> Response[ServiceVCSConnectionStatusResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceVCSConnectionStatusResponse | StderrErrResponse]:
    """check the real-time status of a VCS connection

     Check the real-time status of a VCS (GitHub App) connection.

    This endpoint queries GitHub's API directly to fetch the current installation status, including:
    - Active/Suspended state
    - Account information
    - Permissions
    - Suspension details (if applicable)

    **Important**: This endpoint always fetches fresh data from GitHub (no caching) to ensure accurate
    status information.

    ## Response Status Values

    - `active`: The GitHub App installation is active and functioning
    - `suspended`: The installation has been suspended (see `suspended_at` and `suspended_by` for
    details)
    - `unknown`: Unable to determine status (GitHub API error - see `error` field)

    ## Use Cases

    - Troubleshooting connection issues
    - Monitoring installation health
    - Detecting suspended or revoked installations
    - Validating permissions before operations

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceVCSConnectionStatusResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceVCSConnectionStatusResponse | StderrErrResponse | None:
    """check the real-time status of a VCS connection

     Check the real-time status of a VCS (GitHub App) connection.

    This endpoint queries GitHub's API directly to fetch the current installation status, including:
    - Active/Suspended state
    - Account information
    - Permissions
    - Suspension details (if applicable)

    **Important**: This endpoint always fetches fresh data from GitHub (no caching) to ensure accurate
    status information.

    ## Response Status Values

    - `active`: The GitHub App installation is active and functioning
    - `suspended`: The installation has been suspended (see `suspended_at` and `suspended_by` for
    details)
    - `unknown`: Unable to determine status (GitHub API error - see `error` field)

    ## Use Cases

    - Troubleshooting connection issues
    - Monitoring installation health
    - Detecting suspended or revoked installations
    - Validating permissions before operations

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceVCSConnectionStatusResponse | StderrErrResponse
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceVCSConnectionStatusResponse | StderrErrResponse]:
    """check the real-time status of a VCS connection

     Check the real-time status of a VCS (GitHub App) connection.

    This endpoint queries GitHub's API directly to fetch the current installation status, including:
    - Active/Suspended state
    - Account information
    - Permissions
    - Suspension details (if applicable)

    **Important**: This endpoint always fetches fresh data from GitHub (no caching) to ensure accurate
    status information.

    ## Response Status Values

    - `active`: The GitHub App installation is active and functioning
    - `suspended`: The installation has been suspended (see `suspended_at` and `suspended_by` for
    details)
    - `unknown`: Unable to determine status (GitHub API error - see `error` field)

    ## Use Cases

    - Troubleshooting connection issues
    - Monitoring installation health
    - Detecting suspended or revoked installations
    - Validating permissions before operations

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceVCSConnectionStatusResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceVCSConnectionStatusResponse | StderrErrResponse | None:
    """check the real-time status of a VCS connection

     Check the real-time status of a VCS (GitHub App) connection.

    This endpoint queries GitHub's API directly to fetch the current installation status, including:
    - Active/Suspended state
    - Account information
    - Permissions
    - Suspension details (if applicable)

    **Important**: This endpoint always fetches fresh data from GitHub (no caching) to ensure accurate
    status information.

    ## Response Status Values

    - `active`: The GitHub App installation is active and functioning
    - `suspended`: The installation has been suspended (see `suspended_at` and `suspended_by` for
    details)
    - `unknown`: Unable to determine status (GitHub API error - see `error` field)

    ## Use Cases

    - Troubleshooting connection issues
    - Monitoring installation health
    - Detecting suspended or revoked installations
    - Validating permissions before operations

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceVCSConnectionStatusResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
