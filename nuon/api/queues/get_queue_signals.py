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
    *,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["owner_id"] = owner_id

    params["owner_type"] = owner_type

    params["status"] = status

    params["type"] = type_

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/queues/{queue_id}/signals".format(
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppQueueSignal] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppQueueSignal.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[StderrErrResponse | list[AppQueueSignal]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppQueueSignal]]:
    """List queue signals

     Get a list of signals for a specific queue with optional filtering

    Args:
        queue_id (str):
        owner_id (str | Unset):
        owner_type (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppQueueSignal]]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        owner_id=owner_id,
        owner_type=owner_type,
        status=status,
        type_=type_,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> StderrErrResponse | list[AppQueueSignal] | None:
    """List queue signals

     Get a list of signals for a specific queue with optional filtering

    Args:
        queue_id (str):
        owner_id (str | Unset):
        owner_type (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppQueueSignal]
    """

    return sync_detailed(
        queue_id=queue_id,
        client=client,
        owner_id=owner_id,
        owner_type=owner_type,
        status=status,
        type_=type_,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppQueueSignal]]:
    """List queue signals

     Get a list of signals for a specific queue with optional filtering

    Args:
        queue_id (str):
        owner_id (str | Unset):
        owner_type (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppQueueSignal]]
    """

    kwargs = _get_kwargs(
        queue_id=queue_id,
        owner_id=owner_id,
        owner_type=owner_type,
        status=status,
        type_=type_,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    queue_id: str,
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> StderrErrResponse | list[AppQueueSignal] | None:
    """List queue signals

     Get a list of signals for a specific queue with optional filtering

    Args:
        queue_id (str):
        owner_id (str | Unset):
        owner_type (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppQueueSignal]
    """

    return (
        await asyncio_detailed(
            queue_id=queue_id,
            client=client,
            owner_id=owner_id,
            owner_type=owner_type,
            status=status,
            type_=type_,
            limit=limit,
            offset=offset,
        )
    ).parsed
