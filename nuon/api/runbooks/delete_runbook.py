from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    app_id: str,
    runbook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_id}/runbooks/{runbook_id}".format(
            app_id=quote(str(app_id), safe=""),
            runbook_id=quote(str(runbook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[bool]:
    """delete a runbook

    Args:
        app_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        runbook_id=runbook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> bool | None:
    """delete a runbook

    Args:
        app_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        bool
    """

    return sync_detailed(
        app_id=app_id,
        runbook_id=runbook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[bool]:
    """delete a runbook

    Args:
        app_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        runbook_id=runbook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> bool | None:
    """delete a runbook

    Args:
        app_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        bool
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            runbook_id=runbook_id,
            client=client,
        )
    ).parsed
