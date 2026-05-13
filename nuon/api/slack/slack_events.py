from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_slack_challenge_response import ServiceSlackChallengeResponse
from ...models.slack_events_body import SlackEventsBody
from ...types import Response


def _get_kwargs(
    *,
    body: SlackEventsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slack/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceSlackChallengeResponse | None:
    if response.status_code == 200:
        response_200 = ServiceSlackChallengeResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceSlackChallengeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlackEventsBody,
) -> Response[ServiceSlackChallengeResponse]:
    """Slack Events API webhook

     Receives lifecycle events from Slack: url_verification (handshake), app_uninstalled (workspace
    removed Nuon), tokens_revoked (bot token invalidated). Authenticated via Slack signing-secret
    middleware (X-Slack-Signature + X-Slack-Request-Timestamp); not via API key. Returns 200 even for
    unhandled event types so Slack does not retry.

    Args:
        body (SlackEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceSlackChallengeResponse]
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
    client: AuthenticatedClient | Client,
    body: SlackEventsBody,
) -> ServiceSlackChallengeResponse | None:
    """Slack Events API webhook

     Receives lifecycle events from Slack: url_verification (handshake), app_uninstalled (workspace
    removed Nuon), tokens_revoked (bot token invalidated). Authenticated via Slack signing-secret
    middleware (X-Slack-Signature + X-Slack-Request-Timestamp); not via API key. Returns 200 even for
    unhandled event types so Slack does not retry.

    Args:
        body (SlackEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceSlackChallengeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlackEventsBody,
) -> Response[ServiceSlackChallengeResponse]:
    """Slack Events API webhook

     Receives lifecycle events from Slack: url_verification (handshake), app_uninstalled (workspace
    removed Nuon), tokens_revoked (bot token invalidated). Authenticated via Slack signing-secret
    middleware (X-Slack-Signature + X-Slack-Request-Timestamp); not via API key. Returns 200 even for
    unhandled event types so Slack does not retry.

    Args:
        body (SlackEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceSlackChallengeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SlackEventsBody,
) -> ServiceSlackChallengeResponse | None:
    """Slack Events API webhook

     Receives lifecycle events from Slack: url_verification (handshake), app_uninstalled (workspace
    removed Nuon), tokens_revoked (bot token invalidated). Authenticated via Slack signing-secret
    middleware (X-Slack-Signature + X-Slack-Request-Timestamp); not via API key. Returns 200 even for
    unhandled event types so Slack does not retry.

    Args:
        body (SlackEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceSlackChallengeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
