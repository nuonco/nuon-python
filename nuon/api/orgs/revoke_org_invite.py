from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_org_invite import AppOrgInvite
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    invite_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/orgs/current/invites/{invite_id}/revoke".format(
            invite_id=quote(str(invite_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppOrgInvite | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppOrgInvite.from_dict(response.json())

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
) -> Response[AppOrgInvite | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invite_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppOrgInvite | StderrErrResponse]:
    r"""Revoke an org invite

     Revoke a pending org invite. The invite status is set to \"revoked\" and the record is soft-deleted,
    freeing the unique constraint so the same email can be re-invited.

    Only org admins can revoke invites. Only pending invites can be revoked.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOrgInvite | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invite_id: str,
    *,
    client: AuthenticatedClient,
) -> AppOrgInvite | StderrErrResponse | None:
    r"""Revoke an org invite

     Revoke a pending org invite. The invite status is set to \"revoked\" and the record is soft-deleted,
    freeing the unique constraint so the same email can be re-invited.

    Only org admins can revoke invites. Only pending invites can be revoked.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOrgInvite | StderrErrResponse
    """

    return sync_detailed(
        invite_id=invite_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invite_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppOrgInvite | StderrErrResponse]:
    r"""Revoke an org invite

     Revoke a pending org invite. The invite status is set to \"revoked\" and the record is soft-deleted,
    freeing the unique constraint so the same email can be re-invited.

    Only org admins can revoke invites. Only pending invites can be revoked.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOrgInvite | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invite_id: str,
    *,
    client: AuthenticatedClient,
) -> AppOrgInvite | StderrErrResponse | None:
    r"""Revoke an org invite

     Revoke a pending org invite. The invite status is set to \"revoked\" and the record is soft-deleted,
    freeing the unique constraint so the same email can be re-invited.

    Only org admins can revoke invites. Only pending invites can be revoked.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOrgInvite | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            invite_id=invite_id,
            client=client,
        )
    ).parsed
