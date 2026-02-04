from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_org import AppOrg
from ...models.service_update_org_features_request import ServiceUpdateOrgFeaturesRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceUpdateOrgFeaturesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/orgs/current/features",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppOrg | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppOrg.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppOrg | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOrgFeaturesRequest,
) -> Response[AppOrg | StderrErrResponse]:
    r"""update org features (requires user-managed-features flag)

     Update feature flags for your current organization.

    This endpoint allows organization users to manage feature flags, but requires the `user-managed-
    features` flag to be enabled for the organization. The `user-managed-features` flag itself cannot be
    modified through this endpoint and can only be enabled/disabled by administrators.

    **Requirements:**
    - The `user-managed-features` flag must be enabled for your organization
    - You cannot toggle the `user-managed-features` flag through this endpoint (admin-only)

    **Example Request:**
    ```json
    {
      \"features\": {
        \"api-pagination\": true,
        \"install-delete\": false
      }
    }
    ```

    The request will update only the specified feature flags. Features not included in the request will
    retain their current values.

    Args:
        body (ServiceUpdateOrgFeaturesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOrg | StderrErrResponse]
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
    body: ServiceUpdateOrgFeaturesRequest,
) -> AppOrg | StderrErrResponse | None:
    r"""update org features (requires user-managed-features flag)

     Update feature flags for your current organization.

    This endpoint allows organization users to manage feature flags, but requires the `user-managed-
    features` flag to be enabled for the organization. The `user-managed-features` flag itself cannot be
    modified through this endpoint and can only be enabled/disabled by administrators.

    **Requirements:**
    - The `user-managed-features` flag must be enabled for your organization
    - You cannot toggle the `user-managed-features` flag through this endpoint (admin-only)

    **Example Request:**
    ```json
    {
      \"features\": {
        \"api-pagination\": true,
        \"install-delete\": false
      }
    }
    ```

    The request will update only the specified feature flags. Features not included in the request will
    retain their current values.

    Args:
        body (ServiceUpdateOrgFeaturesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOrg | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOrgFeaturesRequest,
) -> Response[AppOrg | StderrErrResponse]:
    r"""update org features (requires user-managed-features flag)

     Update feature flags for your current organization.

    This endpoint allows organization users to manage feature flags, but requires the `user-managed-
    features` flag to be enabled for the organization. The `user-managed-features` flag itself cannot be
    modified through this endpoint and can only be enabled/disabled by administrators.

    **Requirements:**
    - The `user-managed-features` flag must be enabled for your organization
    - You cannot toggle the `user-managed-features` flag through this endpoint (admin-only)

    **Example Request:**
    ```json
    {
      \"features\": {
        \"api-pagination\": true,
        \"install-delete\": false
      }
    }
    ```

    The request will update only the specified feature flags. Features not included in the request will
    retain their current values.

    Args:
        body (ServiceUpdateOrgFeaturesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppOrg | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateOrgFeaturesRequest,
) -> AppOrg | StderrErrResponse | None:
    r"""update org features (requires user-managed-features flag)

     Update feature flags for your current organization.

    This endpoint allows organization users to manage feature flags, but requires the `user-managed-
    features` flag to be enabled for the organization. The `user-managed-features` flag itself cannot be
    modified through this endpoint and can only be enabled/disabled by administrators.

    **Requirements:**
    - The `user-managed-features` flag must be enabled for your organization
    - You cannot toggle the `user-managed-features` flag through this endpoint (admin-only)

    **Example Request:**
    ```json
    {
      \"features\": {
        \"api-pagination\": true,
        \"install-delete\": false
      }
    }
    ```

    The request will update only the specified feature flags. Features not included in the request will
    retain their current values.

    Args:
        body (ServiceUpdateOrgFeaturesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppOrg | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
