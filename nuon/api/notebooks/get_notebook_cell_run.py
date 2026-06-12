from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_notebook_cell_run import AppNotebookCellRun
from ...types import Response


def _get_kwargs(
    install_id: str,
    notebook_id: str,
    run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/notebooks/{notebook_id}/runs/{run_id}".format(
            install_id=quote(str(install_id), safe=""),
            notebook_id=quote(str(notebook_id), safe=""),
            run_id=quote(str(run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppNotebookCellRun | None:
    if response.status_code == 200:
        response_200 = AppNotebookCellRun.from_dict(response.json())

        return response_200

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
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppNotebookCellRun]:
    """get a single cell run (includes log_stream_id for tailing)

    Args:
        install_id (str):
        notebook_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebookCellRun]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
        run_id=run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    notebook_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> AppNotebookCellRun | None:
    """get a single cell run (includes log_stream_id for tailing)

    Args:
        install_id (str):
        notebook_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppNotebookCellRun
    """

    return sync_detailed(
        install_id=install_id,
        notebook_id=notebook_id,
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    notebook_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppNotebookCellRun]:
    """get a single cell run (includes log_stream_id for tailing)

    Args:
        install_id (str):
        notebook_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppNotebookCellRun]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        notebook_id=notebook_id,
        run_id=run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    notebook_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> AppNotebookCellRun | None:
    """get a single cell run (includes log_stream_id for tailing)

    Args:
        install_id (str):
        notebook_id (str):
        run_id (str):

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
            run_id=run_id,
            client=client,
        )
    ).parsed
