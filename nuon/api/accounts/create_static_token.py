from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_nuonco_nuon_services_ctl_api_internal_app_accounts_service_static_token_response import (
    GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse,
)
from ...models.service_create_static_token_request import ServiceCreateStaticTokenRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceCreateStaticTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/account/static-token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse | None:
    if response.status_code == 201:
        response_201 = GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse.from_dict(
            response.json()
        )

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateStaticTokenRequest,
) -> Response[GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse]:
    """create a static API token for your org

     Creates a long-lived static API token scoped to your current org. Each token gets its own dedicated
    service account, and only grants access to the current org.

    Args:
        body (ServiceCreateStaticTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse]
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
    client: AuthenticatedClient,
    body: ServiceCreateStaticTokenRequest,
) -> GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse | None:
    """create a static API token for your org

     Creates a long-lived static API token scoped to your current org. Each token gets its own dedicated
    service account, and only grants access to the current org.

    Args:
        body (ServiceCreateStaticTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateStaticTokenRequest,
) -> Response[GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse]:
    """create a static API token for your org

     Creates a long-lived static API token scoped to your current org. Each token gets its own dedicated
    service account, and only grants access to the current org.

    Args:
        body (ServiceCreateStaticTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateStaticTokenRequest,
) -> GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse | None:
    """create a static API token for your org

     Creates a long-lived static API token scoped to your current org. Each token gets its own dedicated
    service account, and only grants access to the current org.

    Args:
        body (ServiceCreateStaticTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComNuoncoNuonServicesCtlApiInternalAppAccountsServiceStaticTokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
