from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_role import AppRole
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    context: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["context"] = context

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/roles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppRole] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppRole.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[StderrErrResponse | list[AppRole]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    context: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppRole]]:
    """List your org's roles

     List your org's roles. Each role carries its display metadata (`title`,
    `description`) and the assignment surfaces it may be offered on via the
    `applies_to` field (`team`, `service_account`, `api_token`,
    `oidc_trust_policy`). A role with no `applies_to` entries exists and may be
    displayed, but cannot be newly assigned. Pass `?context=<surface>` to filter
    to the roles assignable on a single surface.

    Args:
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppRole]]
    """

    kwargs = _get_kwargs(
        context=context,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    context: str | Unset = UNSET,
) -> StderrErrResponse | list[AppRole] | None:
    """List your org's roles

     List your org's roles. Each role carries its display metadata (`title`,
    `description`) and the assignment surfaces it may be offered on via the
    `applies_to` field (`team`, `service_account`, `api_token`,
    `oidc_trust_policy`). A role with no `applies_to` entries exists and may be
    displayed, but cannot be newly assigned. Pass `?context=<surface>` to filter
    to the roles assignable on a single surface.

    Args:
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppRole]
    """

    return sync_detailed(
        client=client,
        context=context,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    context: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppRole]]:
    """List your org's roles

     List your org's roles. Each role carries its display metadata (`title`,
    `description`) and the assignment surfaces it may be offered on via the
    `applies_to` field (`team`, `service_account`, `api_token`,
    `oidc_trust_policy`). A role with no `applies_to` entries exists and may be
    displayed, but cannot be newly assigned. Pass `?context=<surface>` to filter
    to the roles assignable on a single surface.

    Args:
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppRole]]
    """

    kwargs = _get_kwargs(
        context=context,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    context: str | Unset = UNSET,
) -> StderrErrResponse | list[AppRole] | None:
    """List your org's roles

     List your org's roles. Each role carries its display metadata (`title`,
    `description`) and the assignment surfaces it may be offered on via the
    `applies_to` field (`team`, `service_account`, `api_token`,
    `oidc_trust_policy`). A role with no `applies_to` entries exists and may be
    displayed, but cannot be newly assigned. Pass `?context=<surface>` to filter
    to the roles assignable on a single surface.

    Args:
        context (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppRole]
    """

    return (
        await asyncio_detailed(
            client=client,
            context=context,
        )
    ).parsed
