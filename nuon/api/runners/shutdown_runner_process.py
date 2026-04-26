from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_runner_process_shutdown import AppRunnerProcessShutdown
from ...models.service_shutdown_runner_process_request import ServiceShutdownRunnerProcessRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    runner_id: str,
    process_id: str,
    *,
    body: ServiceShutdownRunnerProcessRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/runners/{runner_id}/processes/{process_id}/shutdown".format(
            runner_id=quote(str(runner_id), safe=""),
            process_id=quote(str(process_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppRunnerProcessShutdown | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppRunnerProcessShutdown.from_dict(response.json())

        return response_201

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
) -> Response[AppRunnerProcessShutdown | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    runner_id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceShutdownRunnerProcessRequest,
) -> Response[AppRunnerProcessShutdown | StderrErrResponse]:
    """request shutdown of a runner process

    Args:
        runner_id (str):
        process_id (str):
        body (ServiceShutdownRunnerProcessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRunnerProcessShutdown | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    runner_id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceShutdownRunnerProcessRequest,
) -> AppRunnerProcessShutdown | StderrErrResponse | None:
    """request shutdown of a runner process

    Args:
        runner_id (str):
        process_id (str):
        body (ServiceShutdownRunnerProcessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRunnerProcessShutdown | StderrErrResponse
    """

    return sync_detailed(
        runner_id=runner_id,
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    runner_id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceShutdownRunnerProcessRequest,
) -> Response[AppRunnerProcessShutdown | StderrErrResponse]:
    """request shutdown of a runner process

    Args:
        runner_id (str):
        process_id (str):
        body (ServiceShutdownRunnerProcessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRunnerProcessShutdown | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    runner_id: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceShutdownRunnerProcessRequest,
) -> AppRunnerProcessShutdown | StderrErrResponse | None:
    """request shutdown of a runner process

    Args:
        runner_id (str):
        process_id (str):
        body (ServiceShutdownRunnerProcessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRunnerProcessShutdown | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            runner_id=runner_id,
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
