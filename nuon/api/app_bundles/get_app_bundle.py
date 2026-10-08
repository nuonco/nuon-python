from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_bundle_response import ServiceBundleResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    bundle_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/bundles/{bundle_id}".format(
            app_id=quote(str(app_id), safe=""),
            bundle_id=quote(str(bundle_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceBundleResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceBundleResponse.from_dict(response.json())

        return response_200

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
) -> Response[ServiceBundleResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    bundle_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceBundleResponse | StderrErrResponse]:
    """get an app bundle

     Returns the bundle's publish status and any output metadata (manifest digests, archive checksum,
    size, verification timestamp) once publishing has completed.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceBundleResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        bundle_id=bundle_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    bundle_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceBundleResponse | StderrErrResponse | None:
    """get an app bundle

     Returns the bundle's publish status and any output metadata (manifest digests, archive checksum,
    size, verification timestamp) once publishing has completed.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceBundleResponse | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        bundle_id=bundle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    bundle_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceBundleResponse | StderrErrResponse]:
    """get an app bundle

     Returns the bundle's publish status and any output metadata (manifest digests, archive checksum,
    size, verification timestamp) once publishing has completed.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceBundleResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        bundle_id=bundle_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    bundle_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceBundleResponse | StderrErrResponse | None:
    """get an app bundle

     Returns the bundle's publish status and any output metadata (manifest digests, archive checksum,
    size, verification timestamp) once publishing has completed.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceBundleResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            bundle_id=bundle_id,
            client=client,
        )
    ).parsed
