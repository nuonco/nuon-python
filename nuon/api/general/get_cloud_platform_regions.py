from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_cloud_platform_region import AppCloudPlatformRegion
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    cloud_platform: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/general/cloud-platform/{cloud_platform}/regions",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[StderrErrResponse, list["AppCloudPlatformRegion"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppCloudPlatformRegion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[StderrErrResponse, list["AppCloudPlatformRegion"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[StderrErrResponse, list["AppCloudPlatformRegion"]]]:
    """Get regions for a cloud platform

     Return region metadata for the Nuon supported cloud platforms.

    Args:
        cloud_platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, list['AppCloudPlatformRegion']]]
    """

    kwargs = _get_kwargs(
        cloud_platform=cloud_platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cloud_platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[StderrErrResponse, list["AppCloudPlatformRegion"]]]:
    """Get regions for a cloud platform

     Return region metadata for the Nuon supported cloud platforms.

    Args:
        cloud_platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, list['AppCloudPlatformRegion']]
    """

    return sync_detailed(
        cloud_platform=cloud_platform,
        client=client,
    ).parsed


async def asyncio_detailed(
    cloud_platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[StderrErrResponse, list["AppCloudPlatformRegion"]]]:
    """Get regions for a cloud platform

     Return region metadata for the Nuon supported cloud platforms.

    Args:
        cloud_platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, list['AppCloudPlatformRegion']]]
    """

    kwargs = _get_kwargs(
        cloud_platform=cloud_platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cloud_platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[StderrErrResponse, list["AppCloudPlatformRegion"]]]:
    """Get regions for a cloud platform

     Return region metadata for the Nuon supported cloud platforms.

    Args:
        cloud_platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, list['AppCloudPlatformRegion']]
    """

    return (
        await asyncio_detailed(
            cloud_platform=cloud_platform,
            client=client,
        )
    ).parsed
