from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_account import AppAccount
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/orgs/current/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AppAccount, StderrErrResponse]]:
    if response.status_code == 200:
        response_200 = AppAccount.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AppAccount, StderrErrResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
) -> Response[Union[AppAccount, StderrErrResponse]]:
    """Get user accounts for current org

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppAccount, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
) -> Optional[Union[AppAccount, StderrErrResponse]]:
    """Get user accounts for current org

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppAccount, StderrErrResponse]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
) -> Response[Union[AppAccount, StderrErrResponse]]:
    """Get user accounts for current org

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AppAccount, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
) -> Optional[Union[AppAccount, StderrErrResponse]]:
    """Get user accounts for current org

    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AppAccount, StderrErrResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            page=page,
        )
    ).parsed
