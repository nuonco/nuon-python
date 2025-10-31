from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_mng_update_request import ServiceMngUpdateRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    runner_id: str,
    *,
    body: ServiceMngUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/runners/{runner_id}/mng/update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | bool | None:
    if response.status_code == 201:
        response_201 = cast(bool, response.json())
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
) -> Response[StderrErrResponse | bool]:
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
    body: ServiceMngUpdateRequest,
) -> Response[StderrErrResponse | bool]:
    """update an install runner via the mng process

    Args:
        runner_id (str):
        body (ServiceMngUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | bool]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceMngUpdateRequest,
) -> StderrErrResponse | bool | None:
    """update an install runner via the mng process

    Args:
        runner_id (str):
        body (ServiceMngUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | bool
    """

    return sync_detailed(
        runner_id=runner_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceMngUpdateRequest,
) -> Response[StderrErrResponse | bool]:
    """update an install runner via the mng process

    Args:
        runner_id (str):
        body (ServiceMngUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | bool]
    """

    kwargs = _get_kwargs(
        runner_id=runner_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    runner_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceMngUpdateRequest,
) -> StderrErrResponse | bool | None:
    """update an install runner via the mng process

    Args:
        runner_id (str):
        body (ServiceMngUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | bool
    """

    return (
        await asyncio_detailed(
            runner_id=runner_id,
            client=client,
            body=body,
        )
    ).parsed
