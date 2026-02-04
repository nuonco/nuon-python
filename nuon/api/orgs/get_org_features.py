from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_org_feature_info import AppOrgFeatureInfo
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/orgs/features",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[AppOrgFeatureInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppOrgFeatureInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[AppOrgFeatureInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[AppOrgFeatureInfo]]:
    """get available org features

     Get all available organization feature flags with their descriptions.

    This endpoint returns a list of all feature flags that can be enabled or disabled for organizations,
    along with detailed descriptions of what each feature provides.

    Feature flags control access to specific platform capabilities and can be managed by administrators
    through the admin API endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppOrgFeatureInfo]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> list[AppOrgFeatureInfo] | None:
    """get available org features

     Get all available organization feature flags with their descriptions.

    This endpoint returns a list of all feature flags that can be enabled or disabled for organizations,
    along with detailed descriptions of what each feature provides.

    Feature flags control access to specific platform capabilities and can be managed by administrators
    through the admin API endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppOrgFeatureInfo]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[AppOrgFeatureInfo]]:
    """get available org features

     Get all available organization feature flags with their descriptions.

    This endpoint returns a list of all feature flags that can be enabled or disabled for organizations,
    along with detailed descriptions of what each feature provides.

    Feature flags control access to specific platform capabilities and can be managed by administrators
    through the admin API endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[AppOrgFeatureInfo]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> list[AppOrgFeatureInfo] | None:
    """get available org features

     Get all available organization feature flags with their descriptions.

    This endpoint returns a list of all feature flags that can be enabled or disabled for organizations,
    along with detailed descriptions of what each feature provides.

    Feature flags control access to specific platform capabilities and can be managed by administrators
    through the admin API endpoints.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[AppOrgFeatureInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
