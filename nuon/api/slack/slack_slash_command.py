from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_slash_response import ServiceSlashResponse
from ...models.slack_slash_command_body import SlackSlashCommandBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SlackSlashCommandBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/slack/commands/nuon",
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ServiceSlashResponse | None:
    if response.status_code == 200:
        response_200 = ServiceSlashResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceSlashResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlackSlashCommandBody | Unset = UNSET,
) -> Response[ServiceSlashResponse]:
    """Slack /nuon slash command webhook

     Slack invokes this endpoint when a user runs `/nuon <subcommand>` in any channel of an installed
    workspace. Authenticated via the Slack signing-secret middleware (X-Slack-Signature + X-Slack-
    Request-Timestamp); not via API key. Subcommands: subscribe, unsubscribe, status, help. Responses
    are ephemeral.

    Args:
        body (SlackSlashCommandBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceSlashResponse]
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
    body: SlackSlashCommandBody | Unset = UNSET,
) -> ServiceSlashResponse | None:
    """Slack /nuon slash command webhook

     Slack invokes this endpoint when a user runs `/nuon <subcommand>` in any channel of an installed
    workspace. Authenticated via the Slack signing-secret middleware (X-Slack-Signature + X-Slack-
    Request-Timestamp); not via API key. Subcommands: subscribe, unsubscribe, status, help. Responses
    are ephemeral.

    Args:
        body (SlackSlashCommandBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceSlashResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SlackSlashCommandBody | Unset = UNSET,
) -> Response[ServiceSlashResponse]:
    """Slack /nuon slash command webhook

     Slack invokes this endpoint when a user runs `/nuon <subcommand>` in any channel of an installed
    workspace. Authenticated via the Slack signing-secret middleware (X-Slack-Signature + X-Slack-
    Request-Timestamp); not via API key. Subcommands: subscribe, unsubscribe, status, help. Responses
    are ephemeral.

    Args:
        body (SlackSlashCommandBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceSlashResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SlackSlashCommandBody | Unset = UNSET,
) -> ServiceSlashResponse | None:
    """Slack /nuon slash command webhook

     Slack invokes this endpoint when a user runs `/nuon <subcommand>` in any channel of an installed
    workspace. Authenticated via the Slack signing-secret middleware (X-Slack-Signature + X-Slack-
    Request-Timestamp); not via API key. Subcommands: subscribe, unsubscribe, status, help. Responses
    are ephemeral.

    Args:
        body (SlackSlashCommandBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceSlashResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
