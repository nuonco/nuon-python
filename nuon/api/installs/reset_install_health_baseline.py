from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_reset_install_health_baseline_response import ServiceResetInstallHealthBaselineResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/installs/{install_id}/health/baseline".format(
            install_id=quote(str(install_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceResetInstallHealthBaselineResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceResetInstallHealthBaselineResponse.from_dict(response.json())

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
) -> Response[ServiceResetInstallHealthBaselineResponse | StderrErrResponse]:
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
) -> Response[ServiceResetInstallHealthBaselineResponse | StderrErrResponse]:
    """reset the install's health window

     Sets the install's health baseline to now: uptime and the health timeline start counting from this
    moment. Past observations stay recorded but no longer count toward uptime. Requires the component-
    health feature.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceResetInstallHealthBaselineResponse | StderrErrResponse]
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
) -> ServiceResetInstallHealthBaselineResponse | StderrErrResponse | None:
    """reset the install's health window

     Sets the install's health baseline to now: uptime and the health timeline start counting from this
    moment. Past observations stay recorded but no longer count toward uptime. Requires the component-
    health feature.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceResetInstallHealthBaselineResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceResetInstallHealthBaselineResponse | StderrErrResponse]:
    """reset the install's health window

     Sets the install's health baseline to now: uptime and the health timeline start counting from this
    moment. Past observations stay recorded but no longer count toward uptime. Requires the component-
    health feature.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceResetInstallHealthBaselineResponse | StderrErrResponse]
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
) -> ServiceResetInstallHealthBaselineResponse | StderrErrResponse | None:
    """reset the install's health window

     Sets the install's health baseline to now: uptime and the health timeline start counting from this
    moment. Past observations stay recorded but no longer count toward uptime. Requires the component-
    health feature.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceResetInstallHealthBaselineResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
        )
    ).parsed
