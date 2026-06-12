from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_notebook import AppNotebook
from ...types import Response


def _get_kwargs(
    install_id: str,
    notebook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/notebooks/{notebook_id}".format(
            install_id=quote(str(install_id), safe=""),
            notebook_id=quote(str(notebook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppNotebook | None:
    if response.status_code == 200:
        response_200 = AppNotebook.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppNotebook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    notebook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppNotebook]:
    """get a notebook with its ordered cells and each cell's latest run

    Args:
        install_id (str):
        notebook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebook]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    notebook_id: str,
    *,
    client: AuthenticatedClient,
) -> AppNotebook | None:
    """get a notebook with its ordered cells and each cell's latest run

    Args:
        install_id (str):
        notebook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebook
    """

    return sync_detailed(
        install_id=install_id,
        notebook_id=notebook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    notebook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppNotebook]:
    """get a notebook with its ordered cells and each cell's latest run

    Args:
        install_id (str):
        notebook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebook]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    notebook_id: str,
    *,
    client: AuthenticatedClient,
) -> AppNotebook | None:
    """get a notebook with its ordered cells and each cell's latest run

    Args:
        install_id (str):
        notebook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebook
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            notebook_id=notebook_id,
            client=client,
        )
    ).parsed
