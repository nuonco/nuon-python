from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_notebook_cell_run import AppNotebookCellRun
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/notebooks/{notebook_id}/cells/{cell_id}/runs".format(
            install_id=quote(str(install_id), safe=""),
            notebook_id=quote(str(notebook_id), safe=""),
            cell_id=quote(str(cell_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[AppNotebookCellRun] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppNotebookCellRun.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AppNotebookCellRun]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[list[AppNotebookCellRun]]:
    """list a cell's run history (newest first)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppNotebookCellRun]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
        cell_id=cell_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> list[AppNotebookCellRun] | None:
    """list a cell's run history (newest first)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppNotebookCellRun]
    """

    return sync_detailed(
        install_id=install_id,
        notebook_id=notebook_id,
        cell_id=cell_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[list[AppNotebookCellRun]]:
    """list a cell's run history (newest first)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppNotebookCellRun]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
        cell_id=cell_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> list[AppNotebookCellRun] | None:
    """list a cell's run history (newest first)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppNotebookCellRun]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            notebook_id=notebook_id,
            cell_id=cell_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
