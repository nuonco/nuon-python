from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_queue_signal_graph_response_200 import GetQueueSignalGraphResponse200
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    signal_id: str,
    *,
    depth: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["depth"] = depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/queues/{queue_id}/signals/{signal_id}/graph".format(
            queue_id=quote(str(queue_id), safe=""),
            signal_id=quote(str(signal_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetQueueSignalGraphResponse200 | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = GetQueueSignalGraphResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetQueueSignalGraphResponse200 | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    signal_id: str,
    *,
    client: AuthenticatedClient,
    depth: int | Unset = UNSET,
) -> Response[GetQueueSignalGraphResponse200 | StderrErrResponse]:
    """Get signal execution graph

     Returns a recursive tree of a signal and all its awaited/enqueued child signals.

    Args:
        queue_id (str):
        signal_id (str):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueueSignalGraphResponse200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        signal_id=signal_id,
        depth=depth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    signal_id: str,
    *,
    client: AuthenticatedClient,
    depth: int | Unset = UNSET,
) -> GetQueueSignalGraphResponse200 | StderrErrResponse | None:
    """Get signal execution graph

     Returns a recursive tree of a signal and all its awaited/enqueued child signals.

    Args:
        queue_id (str):
        signal_id (str):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueueSignalGraphResponse200 | StderrErrResponse
    """

    return sync_detailed(
        queue_id=queue_id,
        signal_id=signal_id,
        client=client,
        depth=depth,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    signal_id: str,
    *,
    client: AuthenticatedClient,
    depth: int | Unset = UNSET,
) -> Response[GetQueueSignalGraphResponse200 | StderrErrResponse]:
    """Get signal execution graph

     Returns a recursive tree of a signal and all its awaited/enqueued child signals.

    Args:
        queue_id (str):
        signal_id (str):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueueSignalGraphResponse200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        signal_id=signal_id,
        depth=depth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    signal_id: str,
    *,
    client: AuthenticatedClient,
    depth: int | Unset = UNSET,
) -> GetQueueSignalGraphResponse200 | StderrErrResponse | None:
    """Get signal execution graph

     Returns a recursive tree of a signal and all its awaited/enqueued child signals.

    Args:
        queue_id (str):
        signal_id (str):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueueSignalGraphResponse200 | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            signal_id=signal_id,
            client=client,
            depth=depth,
        )
    ).parsed
