from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_log_stream_span import ServiceLogStreamSpan
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    log_stream_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/log-streams/{log_stream_id}/spans".format(
            log_stream_id=quote(str(log_stream_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[ServiceLogStreamSpan] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceLogStreamSpan.from_dict(response_200_item_data)

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
) -> Response[StderrErrResponse | list[ServiceLogStreamSpan]]:
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
) -> Response[StderrErrResponse | list[ServiceLogStreamSpan]]:
    """read a log stream's trace spans

     Read OTEL trace spans for a log stream.

    Returns the flat list of spans recorded by the runner for the job execution
    (or executions) associated with this log stream, ordered by start timestamp
    ASC. The frontend assembles the tree from `parent_span_id`.

    Args:
        log_stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[ServiceLogStreamSpan]]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | list[ServiceLogStreamSpan] | None:
    """read a log stream's trace spans

     Read OTEL trace spans for a log stream.

    Returns the flat list of spans recorded by the runner for the job execution
    (or executions) associated with this log stream, ordered by start timestamp
    ASC. The frontend assembles the tree from `parent_span_id`.

    Args:
        log_stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[ServiceLogStreamSpan]
    """

    return sync_detailed(
        log_stream_id=log_stream_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StderrErrResponse | list[ServiceLogStreamSpan]]:
    """read a log stream's trace spans

     Read OTEL trace spans for a log stream.

    Returns the flat list of spans recorded by the runner for the job execution
    (or executions) associated with this log stream, ordered by start timestamp
    ASC. The frontend assembles the tree from `parent_span_id`.

    Args:
        log_stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[ServiceLogStreamSpan]]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | list[ServiceLogStreamSpan] | None:
    """read a log stream's trace spans

     Read OTEL trace spans for a log stream.

    Returns the flat list of spans recorded by the runner for the job execution
    (or executions) associated with this log stream, ordered by start timestamp
    ASC. The frontend assembles the tree from `parent_span_id`.

    Args:
        log_stream_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[ServiceLogStreamSpan]
    """

    return (
        await asyncio_detailed(
            log_stream_id=log_stream_id,
            client=client,
        )
    ).parsed
