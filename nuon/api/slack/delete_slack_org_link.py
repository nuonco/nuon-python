from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    org_id: str,
    link_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/orgs/{org_id}/slack/org-links/{link_id}".format(
            org_id=quote(str(org_id), safe=""),
            link_id=quote(str(link_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StderrErrResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | StderrErrResponse]:
    """Revoke a Slack workspace ↔ org binding

     Soft-deletes the SlackOrgLink. Channel subscriptions cascade off via the FK. Idempotent if the link
    is already revoked.

    Args:
        org_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        link_id=link_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | StderrErrResponse | None:
    """Revoke a Slack workspace ↔ org binding

     Soft-deletes the SlackOrgLink. Channel subscriptions cascade off via the FK. Idempotent if the link
    is already revoked.

    Args:
        org_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return sync_detailed(
        org_id=org_id,
        link_id=link_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | StderrErrResponse]:
    """Revoke a Slack workspace ↔ org binding

     Soft-deletes the SlackOrgLink. Channel subscriptions cascade off via the FK. Idempotent if the link
    is already revoked.

    Args:
        org_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        link_id=link_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | StderrErrResponse | None:
    """Revoke a Slack workspace ↔ org binding

     Soft-deletes the SlackOrgLink. Channel subscriptions cascade off via the FK. Idempotent if the link
    is already revoked.

    Args:
        org_id (str):
        link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            link_id=link_id,
            client=client,
        )
    ).parsed
