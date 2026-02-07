from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_prune_tokens_response import ServicePruneTokensResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    runner_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/runners/{runner_id}/prune-tokens".format(
            runner_id=quote(str(runner_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServicePruneTokensResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServicePruneTokensResponse.from_dict(response.json())

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
) -> Response[ServicePruneTokensResponse | StderrErrResponse]:
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
) -> Response[ServicePruneTokensResponse | StderrErrResponse]:
    """Prune old tokens for a runner

     Prune old tokens for a specific runner by invalidating all tokens except the most recent one.

    This is useful for cleaning up old tokens without disrupting the currently running runner.
    The latest token (by creation time) is preserved, ensuring the active runner continues to function.

    Returns the count of invalidated tokens for the specified runner.

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServicePruneTokensResponse | StderrErrResponse]
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
) -> ServicePruneTokensResponse | StderrErrResponse | None:
    """Prune old tokens for a runner

     Prune old tokens for a specific runner by invalidating all tokens except the most recent one.

    This is useful for cleaning up old tokens without disrupting the currently running runner.
    The latest token (by creation time) is preserved, ensuring the active runner continues to function.

    Returns the count of invalidated tokens for the specified runner.

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServicePruneTokensResponse | StderrErrResponse
    """

    return sync_detailed(
        runner_id=runner_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    runner_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServicePruneTokensResponse | StderrErrResponse]:
    """Prune old tokens for a runner

     Prune old tokens for a specific runner by invalidating all tokens except the most recent one.

    This is useful for cleaning up old tokens without disrupting the currently running runner.
    The latest token (by creation time) is preserved, ensuring the active runner continues to function.

    Returns the count of invalidated tokens for the specified runner.

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServicePruneTokensResponse | StderrErrResponse]
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
) -> ServicePruneTokensResponse | StderrErrResponse | None:
    """Prune old tokens for a runner

     Prune old tokens for a specific runner by invalidating all tokens except the most recent one.

    This is useful for cleaning up old tokens without disrupting the currently running runner.
    The latest token (by creation time) is preserved, ensuring the active runner continues to function.

    Returns the count of invalidated tokens for the specified runner.

    Args:
        runner_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServicePruneTokensResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            runner_id=runner_id,
            client=client,
        )
    ).parsed
