from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_list_channels_response import ServiceListChannelsResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: str,
    installation_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    types: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["types"] = types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/orgs/{org_id}/slack/installations/{installation_id}/channels".format(
            org_id=quote(str(org_id), safe=""),
            installation_id=quote(str(installation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceListChannelsResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceListChannelsResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceListChannelsResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    installation_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[ServiceListChannelsResponse | StderrErrResponse]:
    """List channels visible to a Slack installation

     Calls Slack's conversations.list using the installation's bot token and returns the page of channels
    the bot can see. The installation must belong to a verified org link for the calling org.

    Args:
        org_id (str):
        installation_id (str):
        cursor (str | Unset):
        limit (int | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceListChannelsResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        installation_id=installation_id,
        cursor=cursor,
        limit=limit,
        types=types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    installation_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    types: str | Unset = UNSET,
) -> ServiceListChannelsResponse | StderrErrResponse | None:
    """List channels visible to a Slack installation

     Calls Slack's conversations.list using the installation's bot token and returns the page of channels
    the bot can see. The installation must belong to a verified org link for the calling org.

    Args:
        org_id (str):
        installation_id (str):
        cursor (str | Unset):
        limit (int | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceListChannelsResponse | StderrErrResponse
    """

    return sync_detailed(
        org_id=org_id,
        installation_id=installation_id,
        client=client,
        cursor=cursor,
        limit=limit,
        types=types,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    installation_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    types: str | Unset = UNSET,
) -> Response[ServiceListChannelsResponse | StderrErrResponse]:
    """List channels visible to a Slack installation

     Calls Slack's conversations.list using the installation's bot token and returns the page of channels
    the bot can see. The installation must belong to a verified org link for the calling org.

    Args:
        org_id (str):
        installation_id (str):
        cursor (str | Unset):
        limit (int | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceListChannelsResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        installation_id=installation_id,
        cursor=cursor,
        limit=limit,
        types=types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    installation_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    types: str | Unset = UNSET,
) -> ServiceListChannelsResponse | StderrErrResponse | None:
    """List channels visible to a Slack installation

     Calls Slack's conversations.list using the installation's bot token and returns the page of channels
    the bot can see. The installation must belong to a verified org link for the calling org.

    Args:
        org_id (str):
        installation_id (str):
        cursor (str | Unset):
        limit (int | Unset):
        types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceListChannelsResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            installation_id=installation_id,
            client=client,
            cursor=cursor,
            limit=limit,
            types=types,
        )
    ).parsed
