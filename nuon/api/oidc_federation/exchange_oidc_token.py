from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_exchange_oidc_token_request import ServiceExchangeOIDCTokenRequest
from ...models.service_exchange_oidc_token_response import ServiceExchangeOIDCTokenResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceExchangeOIDCTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/oidc/token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceExchangeOIDCTokenResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceExchangeOIDCTokenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceExchangeOIDCTokenResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceExchangeOIDCTokenRequest,
) -> Response[ServiceExchangeOIDCTokenResponse | StderrErrResponse]:
    """exchange an OIDC token for a Nuon API token

     Exchanges an OIDC ID token (e.g. from GitHub Actions) for a short-lived Nuon API token. The token
    must match an enabled OIDC trust policy in the target org: its signature is verified against the
    policy issuer's JWKS, and its issuer, audience, and claims must satisfy the policy. No Nuon
    credentials are required to call this endpoint.

    Args:
        body (ServiceExchangeOIDCTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceExchangeOIDCTokenResponse | StderrErrResponse]
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
    body: ServiceExchangeOIDCTokenRequest,
) -> ServiceExchangeOIDCTokenResponse | StderrErrResponse | None:
    """exchange an OIDC token for a Nuon API token

     Exchanges an OIDC ID token (e.g. from GitHub Actions) for a short-lived Nuon API token. The token
    must match an enabled OIDC trust policy in the target org: its signature is verified against the
    policy issuer's JWKS, and its issuer, audience, and claims must satisfy the policy. No Nuon
    credentials are required to call this endpoint.

    Args:
        body (ServiceExchangeOIDCTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceExchangeOIDCTokenResponse | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceExchangeOIDCTokenRequest,
) -> Response[ServiceExchangeOIDCTokenResponse | StderrErrResponse]:
    """exchange an OIDC token for a Nuon API token

     Exchanges an OIDC ID token (e.g. from GitHub Actions) for a short-lived Nuon API token. The token
    must match an enabled OIDC trust policy in the target org: its signature is verified against the
    policy issuer's JWKS, and its issuer, audience, and claims must satisfy the policy. No Nuon
    credentials are required to call this endpoint.

    Args:
        body (ServiceExchangeOIDCTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceExchangeOIDCTokenResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceExchangeOIDCTokenRequest,
) -> ServiceExchangeOIDCTokenResponse | StderrErrResponse | None:
    """exchange an OIDC token for a Nuon API token

     Exchanges an OIDC ID token (e.g. from GitHub Actions) for a short-lived Nuon API token. The token
    must match an enabled OIDC trust policy in the target org: its signature is verified against the
    policy issuer's JWKS, and its issuer, audience, and claims must satisfy the policy. No Nuon
    credentials are required to call this endpoint.

    Args:
        body (ServiceExchangeOIDCTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceExchangeOIDCTokenResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
