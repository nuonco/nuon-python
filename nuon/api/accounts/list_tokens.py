from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_token_response import ServiceTokenResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["q"] = q

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tokens",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[ServiceTokenResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceTokenResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StderrErrResponse | list[ServiceTokenResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> Response[StderrErrResponse | list[ServiceTokenResponse]]:
    """List API tokens for service accounts in the current org

     List the API tokens for service accounts in the current org. Only
    service-account tokens are returned, and token secrets are never
    returned.

    Filter to a single service account with `account_id`, and search with
    `q`, which matches token names case-insensitively or a token ID exactly.

    Each result includes the owning account's `account_name` and
    `account_email`, plus `account_role`, the account's *current* role in this
    org (not the role copied onto the token at creation time).

    Args:
        account_id (str | Unset):
        q (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[ServiceTokenResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        q=q,
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
    account_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> StderrErrResponse | list[ServiceTokenResponse] | None:
    """List API tokens for service accounts in the current org

     List the API tokens for service accounts in the current org. Only
    service-account tokens are returned, and token secrets are never
    returned.

    Filter to a single service account with `account_id`, and search with
    `q`, which matches token names case-insensitively or a token ID exactly.

    Each result includes the owning account's `account_name` and
    `account_email`, plus `account_role`, the account's *current* role in this
    org (not the role copied onto the token at creation time).

    Args:
        account_id (str | Unset):
        q (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[ServiceTokenResponse]
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        q=q,
        offset=offset,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> Response[StderrErrResponse | list[ServiceTokenResponse]]:
    """List API tokens for service accounts in the current org

     List the API tokens for service accounts in the current org. Only
    service-account tokens are returned, and token secrets are never
    returned.

    Filter to a single service account with `account_id`, and search with
    `q`, which matches token names case-insensitively or a token ID exactly.

    Each result includes the owning account's `account_name` and
    `account_email`, plus `account_role`, the account's *current* role in this
    org (not the role copied onto the token at creation time).

    Args:
        account_id (str | Unset):
        q (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[ServiceTokenResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        q=q,
        offset=offset,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> StderrErrResponse | list[ServiceTokenResponse] | None:
    """List API tokens for service accounts in the current org

     List the API tokens for service accounts in the current org. Only
    service-account tokens are returned, and token secrets are never
    returned.

    Filter to a single service account with `account_id`, and search with
    `q`, which matches token names case-insensitively or a token ID exactly.

    Each result includes the owning account's `account_name` and
    `account_email`, plus `account_role`, the account's *current* role in this
    org (not the role copied onto the token at creation time).

    Args:
        account_id (str | Unset):
        q (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[ServiceTokenResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            q=q,
            offset=offset,
            limit=limit,
            page=page,
        )
    ).parsed
