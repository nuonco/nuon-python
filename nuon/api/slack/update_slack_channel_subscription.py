from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_slack_channel_subscription import AppSlackChannelSubscription
from ...models.service_update_channel_subscription_request import ServiceUpdateChannelSubscriptionRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    org_id: str,
    sub_id: str,
    *,
    body: ServiceUpdateChannelSubscriptionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/orgs/{org_id}/slack/channel-subscriptions/{sub_id}".format(
            org_id=quote(str(org_id), safe=""),
            sub_id=quote(str(sub_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppSlackChannelSubscription | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppSlackChannelSubscription.from_dict(response.json())

        return response_200

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
    sub_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateChannelSubscriptionRequest,
) -> Response[AppSlackChannelSubscription | StderrErrResponse]:
    """Update a Slack channel subscription

     Mutates a per-channel routing rule. Pass only the fields you want to change. Updating `match` may
    collide with the `(team_id, channel_id, org_link_id, match_canonical)` unique index — the API
    returns 409 with a clear description in that case so the dashboard can render the same toast it
    shows on a duplicate create. The subscription must belong to the calling org (ABAC enforced at the
    DB query level).

    Args:
        org_id (str):
        sub_id (str):
        body (ServiceUpdateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppSlackChannelSubscription | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        sub_id=sub_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    sub_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateChannelSubscriptionRequest,
) -> AppSlackChannelSubscription | StderrErrResponse | None:
    """Update a Slack channel subscription

     Mutates a per-channel routing rule. Pass only the fields you want to change. Updating `match` may
    collide with the `(team_id, channel_id, org_link_id, match_canonical)` unique index — the API
    returns 409 with a clear description in that case so the dashboard can render the same toast it
    shows on a duplicate create. The subscription must belong to the calling org (ABAC enforced at the
    DB query level).

    Args:
        org_id (str):
        sub_id (str):
        body (ServiceUpdateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppSlackChannelSubscription | StderrErrResponse
    """

    return sync_detailed(
        org_id=org_id,
        sub_id=sub_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    sub_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateChannelSubscriptionRequest,
) -> Response[AppSlackChannelSubscription | StderrErrResponse]:
    """Update a Slack channel subscription

     Mutates a per-channel routing rule. Pass only the fields you want to change. Updating `match` may
    collide with the `(team_id, channel_id, org_link_id, match_canonical)` unique index — the API
    returns 409 with a clear description in that case so the dashboard can render the same toast it
    shows on a duplicate create. The subscription must belong to the calling org (ABAC enforced at the
    DB query level).

    Args:
        org_id (str):
        sub_id (str):
        body (ServiceUpdateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppSlackChannelSubscription | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        sub_id=sub_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    sub_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateChannelSubscriptionRequest,
) -> AppSlackChannelSubscription | StderrErrResponse | None:
    """Update a Slack channel subscription

     Mutates a per-channel routing rule. Pass only the fields you want to change. Updating `match` may
    collide with the `(team_id, channel_id, org_link_id, match_canonical)` unique index — the API
    returns 409 with a clear description in that case so the dashboard can render the same toast it
    shows on a duplicate create. The subscription must belong to the calling org (ABAC enforced at the
    DB query level).

    Args:
        org_id (str):
        sub_id (str):
        body (ServiceUpdateChannelSubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppSlackChannelSubscription | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            sub_id=sub_id,
            client=client,
            body=body,
        )
    ).parsed
