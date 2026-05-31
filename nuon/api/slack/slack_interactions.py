from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.slack_interactions_body import SlackInteractionsBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SlackInteractionsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slack/interactions",
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlackInteractionsBody | Unset = UNSET,
) -> Response[Any]:
    """Slack interactivity & shortcuts request URL

     Receives interactive payloads (view_submission, block_actions, block_suggestion, shortcut).
    Authenticated via Slack signing-secret middleware (X-Slack-Signature + X-Slack-Request-Timestamp);
    not via API key. Dispatches subscribe/unsubscribe modal submissions, block_actions (scope/notif
    radios, Remove buttons), and the install picker's external_select block_suggestion handshake.
    Returns 200 on every parseable envelope so Slack does not retry; unhandled payload types are logged
    and acked.

    Args:
        body (SlackInteractionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlackInteractionsBody | Unset = UNSET,
) -> Response[Any]:
    """Slack interactivity & shortcuts request URL

     Receives interactive payloads (view_submission, block_actions, block_suggestion, shortcut).
    Authenticated via Slack signing-secret middleware (X-Slack-Signature + X-Slack-Request-Timestamp);
    not via API key. Dispatches subscribe/unsubscribe modal submissions, block_actions (scope/notif
    radios, Remove buttons), and the install picker's external_select block_suggestion handshake.
    Returns 200 on every parseable envelope so Slack does not retry; unhandled payload types are logged
    and acked.

    Args:
        body (SlackInteractionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
