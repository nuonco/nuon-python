from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_nuonco_nuon_services_ctl_api_internal_app_tokens_service_create_token_response import (
    GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse,
)
from ...models.service_create_token_request import ServiceCreateTokenRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceCreateTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse.from_dict(
            response.json()
        )

        return response_201

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
) -> Response[GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateTokenRequest,
) -> Response[GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse]:
    """Create an API token for a service account in the current org

     Create an API token for a service account in the current org.

    Only service-account tokens are supported: `account_id` must be a service
    account in the current org (see `POST /v1/service-accounts`). The token
    uses the service account's role.

    The token secret is returned only in this response; it cannot be
    retrieved again. Defaults to a duration of one year (`8760h`) if
    `duration` is not specified. If `invalidate` is set, all existing tokens
    for the service account are revoked before the new token is created.

    Args:
        body (ServiceCreateTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse]
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
    body: ServiceCreateTokenRequest,
) -> GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse | None:
    """Create an API token for a service account in the current org

     Create an API token for a service account in the current org.

    Only service-account tokens are supported: `account_id` must be a service
    account in the current org (see `POST /v1/service-accounts`). The token
    uses the service account's role.

    The token secret is returned only in this response; it cannot be
    retrieved again. Defaults to a duration of one year (`8760h`) if
    `duration` is not specified. If `invalidate` is set, all existing tokens
    for the service account are revoked before the new token is created.

    Args:
        body (ServiceCreateTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateTokenRequest,
) -> Response[GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse]:
    """Create an API token for a service account in the current org

     Create an API token for a service account in the current org.

    Only service-account tokens are supported: `account_id` must be a service
    account in the current org (see `POST /v1/service-accounts`). The token
    uses the service account's role.

    The token secret is returned only in this response; it cannot be
    retrieved again. Defaults to a duration of one year (`8760h`) if
    `duration` is not specified. If `invalidate` is set, all existing tokens
    for the service account are revoked before the new token is created.

    Args:
        body (ServiceCreateTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateTokenRequest,
) -> GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse | None:
    """Create an API token for a service account in the current org

     Create an API token for a service account in the current org.

    Only service-account tokens are supported: `account_id` must be a service
    account in the current org (see `POST /v1/service-accounts`). The token
    uses the service account's role.

    The token secret is returned only in this response; it cannot be
    retrieved again. Defaults to a duration of one year (`8760h`) if
    `duration` is not specified. If `invalidate` is set, all existing tokens
    for the service account are revoked before the new token is created.

    Args:
        body (ServiceCreateTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComNuoncoNuonServicesCtlApiInternalAppTokensServiceCreateTokenResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
