from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_install_health_timeline_response import ServiceInstallHealthTimelineResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    days: int | Unset = 90,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/health/timeline".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceInstallHealthTimelineResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallHealthTimelineResponse.from_dict(response.json())

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
) -> Response[ServiceInstallHealthTimelineResponse | StderrErrResponse]:
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
    days: int | Unset = 90,
) -> Response[ServiceInstallHealthTimelineResponse | StderrErrResponse]:
    """install health timeline

     Returns the install's health history aggregated across its components: uptime_percent and
    observed_seconds are the worst component's, daily[].health is the worst verdict across components
    for that day, and components lists each component's own current health and uptime. Requires the
    component-health feature.

    Args:
        install_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallHealthTimelineResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 90,
) -> ServiceInstallHealthTimelineResponse | StderrErrResponse | None:
    """install health timeline

     Returns the install's health history aggregated across its components: uptime_percent and
    observed_seconds are the worst component's, daily[].health is the worst verdict across components
    for that day, and components lists each component's own current health and uptime. Requires the
    component-health feature.

    Args:
        install_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallHealthTimelineResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 90,
) -> Response[ServiceInstallHealthTimelineResponse | StderrErrResponse]:
    """install health timeline

     Returns the install's health history aggregated across its components: uptime_percent and
    observed_seconds are the worst component's, daily[].health is the worst verdict across components
    for that day, and components lists each component's own current health and uptime. Requires the
    component-health feature.

    Args:
        install_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallHealthTimelineResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 90,
) -> ServiceInstallHealthTimelineResponse | StderrErrResponse | None:
    """install health timeline

     Returns the install's health history aggregated across its components: uptime_percent and
    observed_seconds are the worst component's, daily[].health is the worst verdict across components
    for that day, and components lists each component's own current health and uptime. Requires the
    component-health feature.

    Args:
        install_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallHealthTimelineResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            days=days,
        )
    ).parsed
