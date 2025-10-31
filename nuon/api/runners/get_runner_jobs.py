from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_runner_job import AppRunnerJob
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    runner_id: str,
    *,
    group: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["group"] = group

    params["groups"] = groups

    params["status"] = status

    params["statuses"] = statuses

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/runners/{runner_id}/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppRunnerJob] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppRunnerJob.from_dict(response_200_item_data)

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
) -> Response[StderrErrResponse | list[AppRunnerJob]]:
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
    group: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> Response[StderrErrResponse | list[AppRunnerJob]]:
    """get runner jobs

     Return runner jobs.

    Args:
        runner_id (str):
        group (str | Unset):
        groups (str | Unset):
        status (str | Unset):
        statuses (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppRunnerJob]]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        group=group,
        groups=groups,
        status=status,
        statuses=statuses,
        offset=offset,
        limit=limit,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    group: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> StderrErrResponse | list[AppRunnerJob] | None:
    """get runner jobs

     Return runner jobs.

    Args:
        runner_id (str):
        group (str | Unset):
        groups (str | Unset):
        status (str | Unset):
        statuses (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppRunnerJob]
    """

    return sync_detailed(
        runner_id=runner_id,
        client=client,
        group=group,
        groups=groups,
        status=status,
        statuses=statuses,
        offset=offset,
        limit=limit,
        page=page,
    ).parsed


async def asyncio_detailed(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    group: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> Response[StderrErrResponse | list[AppRunnerJob]]:
    """get runner jobs

     Return runner jobs.

    Args:
        runner_id (str):
        group (str | Unset):
        groups (str | Unset):
        status (str | Unset):
        statuses (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppRunnerJob]]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        group=group,
        groups=groups,
        status=status,
        statuses=statuses,
        offset=offset,
        limit=limit,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    group: str | Unset = UNSET,
    groups: str | Unset = UNSET,
    status: str | Unset = UNSET,
    statuses: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
) -> StderrErrResponse | list[AppRunnerJob] | None:
    """get runner jobs

     Return runner jobs.

    Args:
        runner_id (str):
        group (str | Unset):
        groups (str | Unset):
        status (str | Unset):
        statuses (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppRunnerJob]
    """

    return (
        await asyncio_detailed(
            runner_id=runner_id,
            client=client,
            group=group,
            groups=groups,
            status=status,
            statuses=statuses,
            offset=offset,
            limit=limit,
            page=page,
        )
    ).parsed
