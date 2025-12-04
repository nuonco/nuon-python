from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_account import AppAccount
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    journey_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/account/user-journeys/{journey_name}/complete".format(
            journey_name=quote(str(journey_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAccount | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAccount.from_dict(response.json())

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
) -> Response[AppAccount | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    journey_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppAccount | StderrErrResponse]:
    """Complete all steps in a specific user journey

     Mark all remaining steps in the specified user journey as complete

    Args:
        journey_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAccount | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        journey_name=journey_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    journey_name: str,
    *,
    client: AuthenticatedClient,
) -> AppAccount | StderrErrResponse | None:
    """Complete all steps in a specific user journey

     Mark all remaining steps in the specified user journey as complete

    Args:
        journey_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAccount | StderrErrResponse
    """

    return sync_detailed(
        journey_name=journey_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    journey_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppAccount | StderrErrResponse]:
    """Complete all steps in a specific user journey

     Mark all remaining steps in the specified user journey as complete

    Args:
        journey_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAccount | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        journey_name=journey_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    journey_name: str,
    *,
    client: AuthenticatedClient,
) -> AppAccount | StderrErrResponse | None:
    """Complete all steps in a specific user journey

     Mark all remaining steps in the specified user journey as complete

    Args:
        journey_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAccount | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            journey_name=journey_name,
            client=client,
        )
    ).parsed
