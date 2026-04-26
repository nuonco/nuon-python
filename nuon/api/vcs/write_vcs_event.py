from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_vcs_event import AppVCSEvent
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    vcs_connection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/vcs/{vcs_connection_id}/events".format(
            vcs_connection_id=quote(str(vcs_connection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppVCSEvent | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppVCSEvent.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

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
) -> Response[AppVCSEvent | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vcs_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppVCSEvent | StderrErrResponse]:
    """Write a VCS webhook event

     Writes incoming webhook events for a VCS connection

    Args:
        vcs_connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVCSEvent | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        vcs_connection_id=vcs_connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vcs_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppVCSEvent | StderrErrResponse | None:
    """Write a VCS webhook event

     Writes incoming webhook events for a VCS connection

    Args:
        vcs_connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVCSEvent | StderrErrResponse
    """

    return sync_detailed(
        vcs_connection_id=vcs_connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vcs_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppVCSEvent | StderrErrResponse]:
    """Write a VCS webhook event

     Writes incoming webhook events for a VCS connection

    Args:
        vcs_connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVCSEvent | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        vcs_connection_id=vcs_connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vcs_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppVCSEvent | StderrErrResponse | None:
    """Write a VCS webhook event

     Writes incoming webhook events for a VCS connection

    Args:
        vcs_connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVCSEvent | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            vcs_connection_id=vcs_connection_id,
            client=client,
        )
    ).parsed
