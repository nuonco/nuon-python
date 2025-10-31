from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_otel_log_record import AppOtelLogRecord
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    log_stream_id: str,
    *,
    x_nuon_api_offset: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Nuon-API-Offset"] = x_nuon_api_offset

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/log-streams/{log_stream_id}/logs",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppOtelLogRecord] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppOtelLogRecord.from_dict(response_200_item_data)

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
) -> Response[StderrErrResponse | list[AppOtelLogRecord]]:
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
    x_nuon_api_offset: str,
) -> Response[StderrErrResponse | list[AppOtelLogRecord]]:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        x_nuon_api_offset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppOtelLogRecord]]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
        x_nuon_api_offset=x_nuon_api_offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    x_nuon_api_offset: str,
) -> StderrErrResponse | list[AppOtelLogRecord] | None:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        x_nuon_api_offset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppOtelLogRecord]
    """

    return sync_detailed(
        log_stream_id=log_stream_id,
        client=client,
        x_nuon_api_offset=x_nuon_api_offset,
    ).parsed


async def asyncio_detailed(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    x_nuon_api_offset: str,
) -> Response[StderrErrResponse | list[AppOtelLogRecord]]:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        x_nuon_api_offset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppOtelLogRecord]]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
        x_nuon_api_offset=x_nuon_api_offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    x_nuon_api_offset: str,
) -> StderrErrResponse | list[AppOtelLogRecord] | None:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        x_nuon_api_offset (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppOtelLogRecord]
    """

    return (
        await asyncio_detailed(
            log_stream_id=log_stream_id,
            client=client,
            x_nuon_api_offset=x_nuon_api_offset,
        )
    ).parsed
