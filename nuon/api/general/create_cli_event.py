from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_create_cli_event_request import ServiceCreateCLIEventRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceCreateCLIEventRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/general/cli-events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StderrErrResponse | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
) -> Response[Any | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateCLIEventRequest,
) -> Response[Any | StderrErrResponse]:
    """Record a CLI command run for product analytics

     Records one CLI command run (command path without arguments, CLI version, outcome, duration, OS and
    architecture) for product analytics. The CLI skips this call when telemetry is disabled with
    `DO_NOT_TRACK=1`, `NUON_DISABLE_TELEMETRY=true` or `disable_telemetry: true` in the CLI config. The
    event is dropped when the control plane has no analytics key configured.

    Args:
        body (ServiceCreateCLIEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateCLIEventRequest,
) -> Any | StderrErrResponse | None:
    """Record a CLI command run for product analytics

     Records one CLI command run (command path without arguments, CLI version, outcome, duration, OS and
    architecture) for product analytics. The CLI skips this call when telemetry is disabled with
    `DO_NOT_TRACK=1`, `NUON_DISABLE_TELEMETRY=true` or `disable_telemetry: true` in the CLI config. The
    event is dropped when the control plane has no analytics key configured.

    Args:
        body (ServiceCreateCLIEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateCLIEventRequest,
) -> Response[Any | StderrErrResponse]:
    """Record a CLI command run for product analytics

     Records one CLI command run (command path without arguments, CLI version, outcome, duration, OS and
    architecture) for product analytics. The CLI skips this call when telemetry is disabled with
    `DO_NOT_TRACK=1`, `NUON_DISABLE_TELEMETRY=true` or `disable_telemetry: true` in the CLI config. The
    event is dropped when the control plane has no analytics key configured.

    Args:
        body (ServiceCreateCLIEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateCLIEventRequest,
) -> Any | StderrErrResponse | None:
    """Record a CLI command run for product analytics

     Records one CLI command run (command path without arguments, CLI version, outcome, duration, OS and
    architecture) for product analytics. The CLI skips this call when telemetry is disabled with
    `DO_NOT_TRACK=1`, `NUON_DISABLE_TELEMETRY=true` or `disable_telemetry: true` in the CLI config. The
    event is dropped when the control plane has no analytics key configured.

    Args:
        body (ServiceCreateCLIEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
