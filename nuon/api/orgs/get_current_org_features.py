from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_current_org_features_response_200 import GetCurrentOrgFeaturesResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/orgs/current/features",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCurrentOrgFeaturesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCurrentOrgFeaturesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCurrentOrgFeaturesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetCurrentOrgFeaturesResponse200]:
    r"""get current org's feature flags

     Get the current organization's feature flag values.

    Returns a map of feature flag names to their enabled/disabled status for the authenticated
    organization.

    This endpoint shows which features are currently enabled or disabled for your organization, unlike
    `/v1/orgs/features` which returns all available features with their descriptions.

    Example response:
    ```json
    {
      \"api-pagination\": true,
      \"org-dashboard\": false,
      \"org-runner\": true,
      \"stratus-layout\": true,
      \"user-managed-features\": false
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCurrentOrgFeaturesResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetCurrentOrgFeaturesResponse200 | None:
    r"""get current org's feature flags

     Get the current organization's feature flag values.

    Returns a map of feature flag names to their enabled/disabled status for the authenticated
    organization.

    This endpoint shows which features are currently enabled or disabled for your organization, unlike
    `/v1/orgs/features` which returns all available features with their descriptions.

    Example response:
    ```json
    {
      \"api-pagination\": true,
      \"org-dashboard\": false,
      \"org-runner\": true,
      \"stratus-layout\": true,
      \"user-managed-features\": false
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCurrentOrgFeaturesResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetCurrentOrgFeaturesResponse200]:
    r"""get current org's feature flags

     Get the current organization's feature flag values.

    Returns a map of feature flag names to their enabled/disabled status for the authenticated
    organization.

    This endpoint shows which features are currently enabled or disabled for your organization, unlike
    `/v1/orgs/features` which returns all available features with their descriptions.

    Example response:
    ```json
    {
      \"api-pagination\": true,
      \"org-dashboard\": false,
      \"org-runner\": true,
      \"stratus-layout\": true,
      \"user-managed-features\": false
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCurrentOrgFeaturesResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetCurrentOrgFeaturesResponse200 | None:
    r"""get current org's feature flags

     Get the current organization's feature flag values.

    Returns a map of feature flag names to their enabled/disabled status for the authenticated
    organization.

    This endpoint shows which features are currently enabled or disabled for your organization, unlike
    `/v1/orgs/features` which returns all available features with their descriptions.

    Example response:
    ```json
    {
      \"api-pagination\": true,
      \"org-dashboard\": false,
      \"org-runner\": true,
      \"stratus-layout\": true,
      \"user-managed-features\": false
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCurrentOrgFeaturesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
