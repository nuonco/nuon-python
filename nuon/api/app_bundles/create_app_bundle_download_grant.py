from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_download_grant_response import ServiceDownloadGrantResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    bundle_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_id}/bundles/{bundle_id}/download-grants".format(
            app_id=quote(str(app_id), safe=""),
            bundle_id=quote(str(bundle_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceDownloadGrantResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceDownloadGrantResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = StderrErrResponse.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceDownloadGrantResponse | StderrErrResponse]:
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
) -> Response[ServiceDownloadGrantResponse | StderrErrResponse]:
    """create a download grant for a published app bundle

     Returns a short-lived presigned URL that serves the bundle archive bytes directly from storage;
    requests never pass through ctl-api. Requires the bundle to be published with a verified upload.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceDownloadGrantResponse | StderrErrResponse]
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
) -> ServiceDownloadGrantResponse | StderrErrResponse | None:
    """create a download grant for a published app bundle

     Returns a short-lived presigned URL that serves the bundle archive bytes directly from storage;
    requests never pass through ctl-api. Requires the bundle to be published with a verified upload.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceDownloadGrantResponse | StderrErrResponse
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
) -> Response[ServiceDownloadGrantResponse | StderrErrResponse]:
    """create a download grant for a published app bundle

     Returns a short-lived presigned URL that serves the bundle archive bytes directly from storage;
    requests never pass through ctl-api. Requires the bundle to be published with a verified upload.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceDownloadGrantResponse | StderrErrResponse]
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
) -> ServiceDownloadGrantResponse | StderrErrResponse | None:
    """create a download grant for a published app bundle

     Returns a short-lived presigned URL that serves the bundle archive bytes directly from storage;
    requests never pass through ctl-api. Requires the bundle to be published with a verified upload.

    Args:
        app_id (str):
        bundle_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceDownloadGrantResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            bundle_id=bundle_id,
            client=client,
        )
    ).parsed
