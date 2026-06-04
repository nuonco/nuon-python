from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_log_stream_tail_logs_response import ServiceLogStreamTailLogsResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    log_stream_id: str,
    *,
    since: str | Unset = UNSET,
    wait: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params["wait"] = wait

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/log-streams/{log_stream_id}/logs/tail".format(
            log_stream_id=quote(str(log_stream_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceLogStreamTailLogsResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceLogStreamTailLogsResponse.from_dict(response.json())

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
) -> Response[ServiceLogStreamTailLogsResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    wait: str | Unset = UNSET,
) -> Response[ServiceLogStreamTailLogsResponse | StderrErrResponse]:
    """long-poll tail a log stream

     Returns rows after the supplied composite cursor, long-polling up to ~30s for new rows on an idle
    stream. Behind the `log-tail-long-poll` org feature flag.

    Args:
        log_stream_id (str):
        since (str | Unset):
        wait (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceLogStreamTailLogsResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
        since=since,
        wait=wait,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    wait: str | Unset = UNSET,
) -> ServiceLogStreamTailLogsResponse | StderrErrResponse | None:
    """long-poll tail a log stream

     Returns rows after the supplied composite cursor, long-polling up to ~30s for new rows on an idle
    stream. Behind the `log-tail-long-poll` org feature flag.

    Args:
        log_stream_id (str):
        since (str | Unset):
        wait (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceLogStreamTailLogsResponse | StderrErrResponse
    """

    return sync_detailed(
        log_stream_id=log_stream_id,
        client=client,
        since=since,
        wait=wait,
    ).parsed


async def asyncio_detailed(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    wait: str | Unset = UNSET,
) -> Response[ServiceLogStreamTailLogsResponse | StderrErrResponse]:
    """long-poll tail a log stream

     Returns rows after the supplied composite cursor, long-polling up to ~30s for new rows on an idle
    stream. Behind the `log-tail-long-poll` org feature flag.

    Args:
        log_stream_id (str):
        since (str | Unset):
        wait (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceLogStreamTailLogsResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
        since=since,
        wait=wait,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    since: str | Unset = UNSET,
    wait: str | Unset = UNSET,
) -> ServiceLogStreamTailLogsResponse | StderrErrResponse | None:
    """long-poll tail a log stream

     Returns rows after the supplied composite cursor, long-polling up to ~30s for new rows on an idle
    stream. Behind the `log-tail-long-poll` org feature flag.

    Args:
        log_stream_id (str):
        since (str | Unset):
        wait (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceLogStreamTailLogsResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            log_stream_id=log_stream_id,
            client=client,
            since=since,
            wait=wait,
        )
    ).parsed
