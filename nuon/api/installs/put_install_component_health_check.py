from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_component_resource_state import AppInstallComponentResourceState
from ...models.service_put_install_component_health_check_request import ServicePutInstallComponentHealthCheckRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    component_id: str,
    check_name: str,
    *,
    body: ServicePutInstallComponentHealthCheckRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/installs/{install_id}/components/{component_id}/health/checks/{check_name}".format(
            install_id=quote(str(install_id), safe=""),
            component_id=quote(str(component_id), safe=""),
            check_name=quote(str(check_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppInstallComponentResourceState | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppInstallComponentResourceState.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppInstallComponentResourceState | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    component_id: str,
    check_name: str,
    *,
    client: AuthenticatedClient,
    body: ServicePutInstallComponentHealthCheckRequest,
) -> Response[AppInstallComponentResourceState | StderrErrResponse]:
    r"""report a custom component health check

     Lets an external system (a vendor's CI, a Datadog monitor webhook, a custom action) report a named
    health signal for a component. The report is written as a resource observation with provider
    \"custom\", so it flows through the same live explorer, evaluator, alerting, and timeline as runner-
    reported resources. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        check_name (str):
        body (ServicePutInstallComponentHealthCheckRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallComponentResourceState | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        check_name=check_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    component_id: str,
    check_name: str,
    *,
    client: AuthenticatedClient,
    body: ServicePutInstallComponentHealthCheckRequest,
) -> AppInstallComponentResourceState | StderrErrResponse | None:
    r"""report a custom component health check

     Lets an external system (a vendor's CI, a Datadog monitor webhook, a custom action) report a named
    health signal for a component. The report is written as a resource observation with provider
    \"custom\", so it flows through the same live explorer, evaluator, alerting, and timeline as runner-
    reported resources. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        check_name (str):
        body (ServicePutInstallComponentHealthCheckRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallComponentResourceState | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        component_id=component_id,
        check_name=check_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    component_id: str,
    check_name: str,
    *,
    client: AuthenticatedClient,
    body: ServicePutInstallComponentHealthCheckRequest,
) -> Response[AppInstallComponentResourceState | StderrErrResponse]:
    r"""report a custom component health check

     Lets an external system (a vendor's CI, a Datadog monitor webhook, a custom action) report a named
    health signal for a component. The report is written as a resource observation with provider
    \"custom\", so it flows through the same live explorer, evaluator, alerting, and timeline as runner-
    reported resources. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        check_name (str):
        body (ServicePutInstallComponentHealthCheckRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallComponentResourceState | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        check_name=check_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    component_id: str,
    check_name: str,
    *,
    client: AuthenticatedClient,
    body: ServicePutInstallComponentHealthCheckRequest,
) -> AppInstallComponentResourceState | StderrErrResponse | None:
    r"""report a custom component health check

     Lets an external system (a vendor's CI, a Datadog monitor webhook, a custom action) report a named
    health signal for a component. The report is written as a resource observation with provider
    \"custom\", so it flows through the same live explorer, evaluator, alerting, and timeline as runner-
    reported resources. Requires the component-health feature.

    Args:
        install_id (str):
        component_id (str):
        check_name (str):
        body (ServicePutInstallComponentHealthCheckRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallComponentResourceState | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            component_id=component_id,
            check_name=check_name,
            client=client,
            body=body,
        )
    ).parsed
