from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appbundle_qualification_report import AppbundleQualificationReport
from ...models.service_bundle_response import ServiceBundleResponse
from ...models.service_create_bundle_request import ServiceCreateBundleRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    body: ServiceCreateBundleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_id}/bundles".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceBundleResponse.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = ServiceBundleResponse.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

    if response.status_code == 412:
        response_412 = StderrErrResponse.from_dict(response.json())

        return response_412

    if response.status_code == 422:
        response_422 = AppbundleQualificationReport.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateBundleRequest,
) -> Response[AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse]:
    """create and publish an immutable app bundle from an app config

     Resolves the app config's successful sandbox and component builds once, pins them on the bundle, and
    enqueues an asynchronous publish that assembles an OCI-layout .tar.zst archive. Retries reuse the
    pinned builds and never select newer builds.

    Args:
        app_id (str):
        body (ServiceCreateBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateBundleRequest,
) -> AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse | None:
    """create and publish an immutable app bundle from an app config

     Resolves the app config's successful sandbox and component builds once, pins them on the bundle, and
    enqueues an asynchronous publish that assembles an OCI-layout .tar.zst archive. Retries reuse the
    pinned builds and never select newer builds.

    Args:
        app_id (str):
        body (ServiceCreateBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateBundleRequest,
) -> Response[AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse]:
    """create and publish an immutable app bundle from an app config

     Resolves the app config's successful sandbox and component builds once, pins them on the bundle, and
    enqueues an asynchronous publish that assembles an OCI-layout .tar.zst archive. Retries reuse the
    pinned builds and never select newer builds.

    Args:
        app_id (str):
        body (ServiceCreateBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateBundleRequest,
) -> AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse | None:
    """create and publish an immutable app bundle from an app config

     Resolves the app config's successful sandbox and component builds once, pins them on the bundle, and
    enqueues an asynchronous publish that assembles an OCI-layout .tar.zst archive. Retries reuse the
    pinned builds and never select newer builds.

    Args:
        app_id (str):
        body (ServiceCreateBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppbundleQualificationReport | ServiceBundleResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
