from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_image_repository import AppImageRepository
from ...models.list_image_repositories_platform import ListImageRepositoriesPlatform
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
    platform: ListImageRepositoriesPlatform | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params["q"] = q

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/image-repositories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> StderrErrResponse | list[AppImageRepository] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppImageRepository.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[StderrErrResponse | list[AppImageRepository]]:
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
    platform: ListImageRepositoriesPlatform | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppImageRepository]]:
    """list image repositories

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):
        platform (ListImageRepositoriesPlatform | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppImageRepository]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
        q=q,
        platform=platform,
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
    platform: ListImageRepositoriesPlatform | Unset = UNSET,
) -> StderrErrResponse | list[AppImageRepository] | None:
    """list image repositories

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):
        platform (ListImageRepositoriesPlatform | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppImageRepository]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        page=page,
        q=q,
        platform=platform,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
    platform: ListImageRepositoriesPlatform | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppImageRepository]]:
    """list image repositories

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):
        platform (ListImageRepositoriesPlatform | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppImageRepository]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
        q=q,
        platform=platform,
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
    platform: ListImageRepositoriesPlatform | Unset = UNSET,
) -> StderrErrResponse | list[AppImageRepository] | None:
    """list image repositories

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):
        platform (ListImageRepositoriesPlatform | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppImageRepository]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            page=page,
            q=q,
            platform=platform,
        )
    ).parsed
