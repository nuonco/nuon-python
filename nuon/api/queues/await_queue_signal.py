from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_queue_signal import AppQueueSignal
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    queue_id: str,
    signal_id: str,
    *,
    timeout: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/queues/{queue_id}/signals/{signal_id}/await".format(
            queue_id=quote(str(queue_id), safe=""),
            signal_id=quote(str(signal_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppQueueSignal | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppQueueSignal.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if response.status_code == 408:
        response_408 = StderrErrResponse.from_dict(response.json())

        return response_408

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppQueueSignal | StderrErrResponse]:
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
    timeout: int | Unset = UNSET,
) -> Response[AppQueueSignal | StderrErrResponse]:
    """Long-poll for queue signal completion

     Blocks until the queue signal finishes or the timeout is reached

    Args:
        queue_id (str):
        signal_id (str):
        timeout (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppQueueSignal | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        signal_id=signal_id,
        timeout=timeout,
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
    timeout: int | Unset = UNSET,
) -> AppQueueSignal | StderrErrResponse | None:
    """Long-poll for queue signal completion

     Blocks until the queue signal finishes or the timeout is reached

    Args:
        queue_id (str):
        signal_id (str):
        timeout (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppQueueSignal | StderrErrResponse
    """

    return sync_detailed(
        queue_id=queue_id,
        signal_id=signal_id,
        client=client,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    signal_id: str,
    *,
    client: AuthenticatedClient,
    timeout: int | Unset = UNSET,
) -> Response[AppQueueSignal | StderrErrResponse]:
    """Long-poll for queue signal completion

     Blocks until the queue signal finishes or the timeout is reached

    Args:
        queue_id (str):
        signal_id (str):
        timeout (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppQueueSignal | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        signal_id=signal_id,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    signal_id: str,
    *,
    client: AuthenticatedClient,
    timeout: int | Unset = UNSET,
) -> AppQueueSignal | StderrErrResponse | None:
    """Long-poll for queue signal completion

     Blocks until the queue signal finishes or the timeout is reached

    Args:
        queue_id (str):
        signal_id (str):
        timeout (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppQueueSignal | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            signal_id=signal_id,
            client=client,
            timeout=timeout,
        )
    ).parsed
