from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_queue import AppQueue
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["owner_id"] = owner_id

    params["owner_type"] = owner_type

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/queues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppQueue] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppQueue.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StderrErrResponse | list[AppQueue]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[StderrErrResponse | list[AppQueue]]:
    """List queues

     List queues with optional filtering by owner

    Args:
        owner_id (str | Unset):
        owner_type (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppQueue]]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        owner_type=owner_type,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> StderrErrResponse | list[AppQueue] | None:
    """List queues

     List queues with optional filtering by owner

    Args:
        owner_id (str | Unset):
        owner_type (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppQueue]
    """

    return sync_detailed(
        client=client,
        owner_id=owner_id,
        owner_type=owner_type,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[StderrErrResponse | list[AppQueue]]:
    """List queues

     List queues with optional filtering by owner

    Args:
        owner_id (str | Unset):
        owner_type (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppQueue]]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        owner_type=owner_type,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    owner_id: str | Unset = UNSET,
    owner_type: str | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> StderrErrResponse | list[AppQueue] | None:
    """List queues

     List queues with optional filtering by owner

    Args:
        owner_id (str | Unset):
        owner_type (str | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppQueue]
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_id=owner_id,
            owner_type=owner_type,
            limit=limit,
            offset=offset,
        )
    ).parsed
