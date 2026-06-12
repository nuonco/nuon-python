from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_notebook_cell_run import AppNotebookCellRun
from ...models.service_run_cell_request import ServiceRunCellRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    notebook_id: str,
    cell_id: str,
    *,
    body: ServiceRunCellRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/installs/{install_id}/notebooks/{notebook_id}/cells/{cell_id}/runs".format(
            install_id=quote(str(install_id), safe=""),
            notebook_id=quote(str(notebook_id), safe=""),
            cell_id=quote(str(cell_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppNotebookCellRun | None:
    if response.status_code == 202:
        response_202 = AppNotebookCellRun.from_dict(response.json())

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppNotebookCellRun]:
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
    body: ServiceRunCellRequest | Unset = UNSET,
) -> Response[AppNotebookCellRun]:
    """run a notebook cell on the install's runner

     dispatches the cell to the notebook's warm Temporal workflow and records a NotebookCellRun linking
    to the underlying execution + log stream. Returns once the run is queued, not when it finishes.

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceRunCellRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebookCellRun]
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
    body: ServiceRunCellRequest | Unset = UNSET,
) -> AppNotebookCellRun | None:
    """run a notebook cell on the install's runner

     dispatches the cell to the notebook's warm Temporal workflow and records a NotebookCellRun linking
    to the underlying execution + log stream. Returns once the run is queued, not when it finishes.

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceRunCellRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebookCellRun
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
    body: ServiceRunCellRequest | Unset = UNSET,
) -> Response[AppNotebookCellRun]:
    """run a notebook cell on the install's runner

     dispatches the cell to the notebook's warm Temporal workflow and records a NotebookCellRun linking
    to the underlying execution + log stream. Returns once the run is queued, not when it finishes.

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceRunCellRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebookCellRun]
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
    body: ServiceRunCellRequest | Unset = UNSET,
) -> AppNotebookCellRun | None:
    """run a notebook cell on the install's runner

     dispatches the cell to the notebook's warm Temporal workflow and records a NotebookCellRun linking
    to the underlying execution + log stream. Returns once the run is queued, not when it finishes.

    Args:
        install_id (str):
        notebook_id (str):
        cell_id (str):
        body (ServiceRunCellRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebookCellRun
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
