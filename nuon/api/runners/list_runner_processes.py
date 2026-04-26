from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_runner_process import AppRunnerProcess
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    runner_id: str,
    *,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    params["status"] = status

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/runners/{runner_id}/processes".format(
            runner_id=quote(str(runner_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppRunnerProcess] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppRunnerProcess.from_dict(response_200_item_data)

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
) -> Response[StderrErrResponse | list[AppRunnerProcess]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppRunnerProcess]]:
    """list runner processes

    Args:
        runner_id (str):
        type_ (str | Unset):
        status (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppRunnerProcess]]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        type_=type_,
        status=status,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> StderrErrResponse | list[AppRunnerProcess] | None:
    """list runner processes

    Args:
        runner_id (str):
        type_ (str | Unset):
        status (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppRunnerProcess]
    """

    return sync_detailed(
        runner_id=runner_id,
        client=client,
        type_=type_,
        status=status,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppRunnerProcess]]:
    """list runner processes

    Args:
        runner_id (str):
        type_ (str | Unset):
        status (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppRunnerProcess]]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        type_=type_,
        status=status,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> StderrErrResponse | list[AppRunnerProcess] | None:
    """list runner processes

    Args:
        runner_id (str):
        type_ (str | Unset):
        status (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppRunnerProcess]
    """

    return (
        await asyncio_detailed(
            runner_id=runner_id,
            client=client,
            type_=type_,
            status=status,
            limit=limit,
            offset=offset,
        )
    ).parsed
