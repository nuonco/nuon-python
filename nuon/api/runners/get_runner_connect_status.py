from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_runner_connection_status import ServiceRunnerConnectionStatus
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    runner_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/runners/{runner_id}/connected",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]:
    if response.status_code == 200:
        response_200 = ServiceRunnerConnectionStatus.from_dict(response.json())

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]:
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
) -> Response[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]:
    """get a runner connection satus based on heartbeat

     # get runner connect status

    The connected status is based on runner heartbeat:

    if no heart beat found — false
    if heart beat > 15 seconds ago — false, hb timestamp
    if the heart beat < 15 seconds ago — true

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    runner_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]:
    """get a runner connection satus based on heartbeat

     # get runner connect status

    The connected status is based on runner heartbeat:

    if no heart beat found — false
    if heart beat > 15 seconds ago — false, hb timestamp
    if the heart beat < 15 seconds ago — true

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ServiceRunnerConnectionStatus, StderrErrResponse]
    """

    return sync_detailed(
        runner_id=runner_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    runner_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]:
    """get a runner connection satus based on heartbeat

     # get runner connect status

    The connected status is based on runner heartbeat:

    if no heart beat found — false
    if heart beat > 15 seconds ago — false, hb timestamp
    if the heart beat < 15 seconds ago — true

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    runner_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ServiceRunnerConnectionStatus, StderrErrResponse]]:
    """get a runner connection satus based on heartbeat

     # get runner connect status

    The connected status is based on runner heartbeat:

    if no heart beat found — false
    if heart beat > 15 seconds ago — false, hb timestamp
    if the heart beat < 15 seconds ago — true

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ServiceRunnerConnectionStatus, StderrErrResponse]
    """

    return (
        await asyncio_detailed(
            runner_id=runner_id,
            client=client,
        )
    ).parsed
