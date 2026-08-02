from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_oidc_trust_policy import AppOIDCTrustPolicy
from ...models.service_create_oidc_trust_policy_request import ServiceCreateOIDCTrustPolicyRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceCreateOIDCTrustPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/oidc/trust-policies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppOIDCTrustPolicy | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppOIDCTrustPolicy.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppOIDCTrustPolicy | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateOIDCTrustPolicyRequest,
) -> Response[AppOIDCTrustPolicy | StderrErrResponse]:
    """create an OIDC trust policy

     Creates an OIDC workload identity trust policy for your current org. OIDC tokens matching the
    policy's issuer, audience, and claim conditions can be exchanged for short-lived Nuon API tokens.
    Each policy gets a dedicated service account with the configured role.

    Args:
        body (ServiceCreateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOIDCTrustPolicy | StderrErrResponse]
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
    body: ServiceCreateOIDCTrustPolicyRequest,
) -> AppOIDCTrustPolicy | StderrErrResponse | None:
    """create an OIDC trust policy

     Creates an OIDC workload identity trust policy for your current org. OIDC tokens matching the
    policy's issuer, audience, and claim conditions can be exchanged for short-lived Nuon API tokens.
    Each policy gets a dedicated service account with the configured role.

    Args:
        body (ServiceCreateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOIDCTrustPolicy | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateOIDCTrustPolicyRequest,
) -> Response[AppOIDCTrustPolicy | StderrErrResponse]:
    """create an OIDC trust policy

     Creates an OIDC workload identity trust policy for your current org. OIDC tokens matching the
    policy's issuer, audience, and claim conditions can be exchanged for short-lived Nuon API tokens.
    Each policy gets a dedicated service account with the configured role.

    Args:
        body (ServiceCreateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOIDCTrustPolicy | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceCreateOIDCTrustPolicyRequest,
) -> AppOIDCTrustPolicy | StderrErrResponse | None:
    """create an OIDC trust policy

     Creates an OIDC workload identity trust policy for your current org. OIDC tokens matching the
    policy's issuer, audience, and claim conditions can be exchanged for short-lived Nuon API tokens.
    Each policy gets a dedicated service account with the configured role.

    Args:
        body (ServiceCreateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOIDCTrustPolicy | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
