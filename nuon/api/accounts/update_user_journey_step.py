from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_account import AppAccount
from ...models.service_update_user_journey_step_request import ServiceUpdateUserJourneyStepRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    journey_name: str,
    step_name: str,
    *,
    body: ServiceUpdateUserJourneyStepRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/account/user-journeys/{journey_name}/steps/{step_name}".format(
            journey_name=quote(str(journey_name), safe=""),
            step_name=quote(str(step_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    step_name: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateUserJourneyStepRequest,
) -> Response[AppAccount | StderrErrResponse]:
    """Update user journey step completion status

     Mark a user journey step as complete or incomplete

    Args:
        journey_name (str):
        step_name (str):
        body (ServiceUpdateUserJourneyStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAccount | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        journey_name=journey_name,
        step_name=step_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    journey_name: str,
    step_name: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateUserJourneyStepRequest,
) -> AppAccount | StderrErrResponse | None:
    """Update user journey step completion status

     Mark a user journey step as complete or incomplete

    Args:
        journey_name (str):
        step_name (str):
        body (ServiceUpdateUserJourneyStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAccount | StderrErrResponse
    """

    return sync_detailed(
        journey_name=journey_name,
        step_name=step_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    journey_name: str,
    step_name: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateUserJourneyStepRequest,
) -> Response[AppAccount | StderrErrResponse]:
    """Update user journey step completion status

     Mark a user journey step as complete or incomplete

    Args:
        journey_name (str):
        step_name (str):
        body (ServiceUpdateUserJourneyStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAccount | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        journey_name=journey_name,
        step_name=step_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    journey_name: str,
    step_name: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateUserJourneyStepRequest,
) -> AppAccount | StderrErrResponse | None:
    """Update user journey step completion status

     Mark a user journey step as complete or incomplete

    Args:
        journey_name (str):
        step_name (str):
        body (ServiceUpdateUserJourneyStepRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAccount | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            journey_name=journey_name,
            step_name=step_name,
            client=client,
            body=body,
        )
    ).parsed
