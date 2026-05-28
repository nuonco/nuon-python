from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_runbook_config import AppRunbookConfig
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    runbook_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/runbooks/{runbook_id}/configs".format(
            app_id=quote(str(app_id), safe=""),
            runbook_id=quote(str(runbook_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[AppRunbookConfig] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppRunbookConfig.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AppRunbookConfig]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[list[AppRunbookConfig]]:
    """get runbook configs

    Args:
        app_id (str):
        runbook_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppRunbookConfig]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        runbook_id=runbook_id,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> list[AppRunbookConfig] | None:
    """get runbook configs

    Args:
        app_id (str):
        runbook_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppRunbookConfig]
    """

    return sync_detailed(
        app_id=app_id,
        runbook_id=runbook_id,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[list[AppRunbookConfig]]:
    """get runbook configs

    Args:
        app_id (str):
        runbook_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppRunbookConfig]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        runbook_id=runbook_id,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> list[AppRunbookConfig] | None:
    """get runbook configs

    Args:
        app_id (str):
        runbook_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppRunbookConfig]
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            runbook_id=runbook_id,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
