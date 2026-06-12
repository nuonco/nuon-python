from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_notebook_cell import AppNotebookCell
from ...models.service_update_cell_request import ServiceUpdateCellRequest
from ...types import Response


def _get_kwargs(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    body: ServiceUpdateCellRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/installs/{install_id}/notebooks/{notebook_id}/cells/{cell_id}".format(
            install_id=quote(str(install_id), safe=""),
            notebook_id=quote(str(notebook_id), safe=""),
            cell_id=quote(str(cell_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppNotebookCell | None:
    if response.status_code == 200:
        response_200 = AppNotebookCell.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppNotebookCell]:
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
    body: ServiceUpdateCellRequest,
) -> Response[AppNotebookCell]:
    """edit a cell (bumps its revision)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceUpdateCellRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebookCell]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
        cell_id=cell_id,
        body=body,
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
    body: ServiceUpdateCellRequest,
) -> AppNotebookCell | None:
    """edit a cell (bumps its revision)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceUpdateCellRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebookCell
    """

    return sync_detailed(
        install_id=install_id,
        notebook_id=notebook_id,
        cell_id=cell_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateCellRequest,
) -> Response[AppNotebookCell]:
    """edit a cell (bumps its revision)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceUpdateCellRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebookCell]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
        cell_id=cell_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateCellRequest,
) -> AppNotebookCell | None:
    """edit a cell (bumps its revision)

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceUpdateCellRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebookCell
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            notebook_id=notebook_id,
            cell_id=cell_id,
            client=client,
            body=body,
        )
    ).parsed
