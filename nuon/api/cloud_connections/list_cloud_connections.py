from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_connection_list_response import ServiceConnectionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cloud-connections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[ServiceConnectionListResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceConnectionListResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ServiceConnectionListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> Response[list[ServiceConnectionListResponse]]:
    """list cloud connections

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ServiceConnectionListResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> list[ServiceConnectionListResponse] | None:
    """list cloud connections

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ServiceConnectionListResponse]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> Response[list[ServiceConnectionListResponse]]:
    """list cloud connections

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ServiceConnectionListResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> list[ServiceConnectionListResponse] | None:
    """list cloud connections

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ServiceConnectionListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            page=page,
            q=q,
        )
    ).parsed
