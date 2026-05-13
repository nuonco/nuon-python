from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_slack_channel_subscription import AppSlackChannelSubscription
from ...models.service_create_channel_subscription_request import ServiceCreateChannelSubscriptionRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    org_id: str,
    *,
    body: ServiceCreateChannelSubscriptionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/orgs/{org_id}/slack/channel-subscriptions".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppSlackChannelSubscription | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppSlackChannelSubscription.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = StderrErrResponse.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppSlackChannelSubscription | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateChannelSubscriptionRequest,
) -> Response[AppSlackChannelSubscription | StderrErrResponse]:
    """Create a Slack channel subscription

     Subscribes a Slack channel to events for the current org. The org_link_id must resolve to a verified
    SlackOrgLink belonging to the calling org; this is enforced at the DB query level (ABAC).

    Args:
        org_id (str):
        body (ServiceCreateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppSlackChannelSubscription | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateChannelSubscriptionRequest,
) -> AppSlackChannelSubscription | StderrErrResponse | None:
    """Create a Slack channel subscription

     Subscribes a Slack channel to events for the current org. The org_link_id must resolve to a verified
    SlackOrgLink belonging to the calling org; this is enforced at the DB query level (ABAC).

    Args:
        org_id (str):
        body (ServiceCreateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppSlackChannelSubscription | StderrErrResponse
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateChannelSubscriptionRequest,
) -> Response[AppSlackChannelSubscription | StderrErrResponse]:
    """Create a Slack channel subscription

     Subscribes a Slack channel to events for the current org. The org_link_id must resolve to a verified
    SlackOrgLink belonging to the calling org; this is enforced at the DB query level (ABAC).

    Args:
        org_id (str):
        body (ServiceCreateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppSlackChannelSubscription | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateChannelSubscriptionRequest,
) -> AppSlackChannelSubscription | StderrErrResponse | None:
    """Create a Slack channel subscription

     Subscribes a Slack channel to events for the current org. The org_link_id must resolve to a verified
    SlackOrgLink belonging to the calling org; this is enforced at the DB query level (ABAC).

    Args:
        org_id (str):
        body (ServiceCreateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppSlackChannelSubscription | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            body=body,
        )
    ).parsed
