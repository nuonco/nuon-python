from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_install_component_health_timeline_response import ServiceInstallComponentHealthTimelineResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    component_id: str,
    *,
    days: int | Unset = 90,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/components/{component_id}/health/timeline".format(
            install_id=quote(str(install_id), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceInstallComponentHealthTimelineResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallComponentHealthTimelineResponse.from_dict(response.json())

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
) -> Response[ServiceInstallComponentHealthTimelineResponse | StderrErrResponse]:
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
    days: int | Unset = 90,
) -> Response[ServiceInstallComponentHealthTimelineResponse | StderrErrResponse]:
    """component health timeline

     Returns a component's health history over a window: recorded verdict transitions (newest first),
    daily worst-verdict buckets covering every day in the window, and an uptime percentage that excludes
    unknown time from both the numerator and denominator. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallComponentHealthTimelineResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        days=days,
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
    days: int | Unset = 90,
) -> ServiceInstallComponentHealthTimelineResponse | StderrErrResponse | None:
    """component health timeline

     Returns a component's health history over a window: recorded verdict transitions (newest first),
    daily worst-verdict buckets covering every day in the window, and an uptime percentage that excludes
    unknown time from both the numerator and denominator. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallComponentHealthTimelineResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        component_id=component_id,
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 90,
) -> Response[ServiceInstallComponentHealthTimelineResponse | StderrErrResponse]:
    """component health timeline

     Returns a component's health history over a window: recorded verdict transitions (newest first),
    daily worst-verdict buckets covering every day in the window, and an uptime percentage that excludes
    unknown time from both the numerator and denominator. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallComponentHealthTimelineResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 90,
) -> ServiceInstallComponentHealthTimelineResponse | StderrErrResponse | None:
    """component health timeline

     Returns a component's health history over a window: recorded verdict transitions (newest first),
    daily worst-verdict buckets covering every day in the window, and an uptime percentage that excludes
    unknown time from both the numerator and denominator. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        days (int | Unset):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallComponentHealthTimelineResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            component_id=component_id,
            client=client,
            days=days,
        )
    ).parsed
