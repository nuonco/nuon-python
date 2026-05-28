from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_runbook import AppInstallRunbook
from ...types import Response


def _get_kwargs(
    install_id: str,
    runbook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/runbooks/{runbook_id}".format(
            install_id=quote(str(install_id), safe=""),
            runbook_id=quote(str(runbook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppInstallRunbook | None:
    if response.status_code == 200:
        response_200 = AppInstallRunbook.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppInstallRunbook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppInstallRunbook]:
    """get an install runbook

    Args:
        install_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallRunbook]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        runbook_id=runbook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> AppInstallRunbook | None:
    """get an install runbook

    Args:
        install_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallRunbook
    """

    return sync_detailed(
        install_id=install_id,
        runbook_id=runbook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppInstallRunbook]:
    """get an install runbook

    Args:
        install_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallRunbook]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        runbook_id=runbook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
) -> AppInstallRunbook | None:
    """get an install runbook

    Args:
        install_id (str):
        runbook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallRunbook
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            runbook_id=runbook_id,
            client=client,
        )
    ).parsed
