from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_component_resource_state import AppInstallComponentResourceState
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    component_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/components/{component_id}/health/checks".format(
            install_id=quote(str(install_id), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppInstallComponentResourceState] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppInstallComponentResourceState.from_dict(response_200_item_data)

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
) -> Response[StderrErrResponse | list[AppInstallComponentResourceState]]:
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
) -> Response[StderrErrResponse | list[AppInstallComponentResourceState]]:
    r"""list custom component health checks

     Returns the latest reported state of every custom health check for the component (provider
    \"custom\"), keyed by check name. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppInstallComponentResourceState]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
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
) -> StderrErrResponse | list[AppInstallComponentResourceState] | None:
    r"""list custom component health checks

     Returns the latest reported state of every custom health check for the component (provider
    \"custom\"), keyed by check name. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppInstallComponentResourceState]
    """

    return sync_detailed(
        install_id=install_id,
        component_id=component_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StderrErrResponse | list[AppInstallComponentResourceState]]:
    r"""list custom component health checks

     Returns the latest reported state of every custom health check for the component (provider
    \"custom\"), keyed by check name. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppInstallComponentResourceState]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | list[AppInstallComponentResourceState] | None:
    r"""list custom component health checks

     Returns the latest reported state of every custom health check for the component (provider
    \"custom\"), keyed by check name. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppInstallComponentResourceState]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            component_id=component_id,
            client=client,
        )
    ).parsed
