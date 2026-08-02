from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_oidc_trust_policy import AppOIDCTrustPolicy
from ...models.service_update_oidc_trust_policy_request import ServiceUpdateOIDCTrustPolicyRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    policy_id: str,
    *,
    body: ServiceUpdateOIDCTrustPolicyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/oidc/trust-policies/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppOIDCTrustPolicy | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppOIDCTrustPolicy.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

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
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOIDCTrustPolicyRequest,
) -> Response[AppOIDCTrustPolicy | StderrErrResponse]:
    """update an OIDC trust policy

     Updates an OIDC workload identity trust policy belonging to your current org. Changing the role also
    updates the policy's service account role, which affects tokens already issued under the policy.

    Args:
        policy_id (str):
        body (ServiceUpdateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOIDCTrustPolicy | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOIDCTrustPolicyRequest,
) -> AppOIDCTrustPolicy | StderrErrResponse | None:
    """update an OIDC trust policy

     Updates an OIDC workload identity trust policy belonging to your current org. Changing the role also
    updates the policy's service account role, which affects tokens already issued under the policy.

    Args:
        policy_id (str):
        body (ServiceUpdateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOIDCTrustPolicy | StderrErrResponse
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOIDCTrustPolicyRequest,
) -> Response[AppOIDCTrustPolicy | StderrErrResponse]:
    """update an OIDC trust policy

     Updates an OIDC workload identity trust policy belonging to your current org. Changing the role also
    updates the policy's service account role, which affects tokens already issued under the policy.

    Args:
        policy_id (str):
        body (ServiceUpdateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOIDCTrustPolicy | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOIDCTrustPolicyRequest,
) -> AppOIDCTrustPolicy | StderrErrResponse | None:
    """update an OIDC trust policy

     Updates an OIDC workload identity trust policy belonging to your current org. Changing the role also
    updates the policy's service account role, which affects tokens already issued under the policy.

    Args:
        policy_id (str):
        body (ServiceUpdateOIDCTrustPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOIDCTrustPolicy | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            body=body,
        )
    ).parsed
