from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_app_kubernetes_contexts_config import AppAppKubernetesContextsConfig
from ...models.service_create_app_kubernetes_contexts_config_request import (
    ServiceCreateAppKubernetesContextsConfigRequest,
)
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    body: ServiceCreateAppKubernetesContextsConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_id}/kubernetes-contexts-configs".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAppKubernetesContextsConfig | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppAppKubernetesContextsConfig.from_dict(response.json())

        return response_201

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
) -> Response[AppAppKubernetesContextsConfig | StderrErrResponse]:
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
    body: ServiceCreateAppKubernetesContextsConfigRequest,
) -> Response[AppAppKubernetesContextsConfig | StderrErrResponse]:
    """create a kubernetes contexts config

     Create the named kubernetes_context bindings for an app config version. Each context names a peer
    terraform_module or pulumi component that emits cluster connection details as outputs.

    Args:
        app_id (str):
        body (ServiceCreateAppKubernetesContextsConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppKubernetesContextsConfig | StderrErrResponse]
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
    body: ServiceCreateAppKubernetesContextsConfigRequest,
) -> AppAppKubernetesContextsConfig | StderrErrResponse | None:
    """create a kubernetes contexts config

     Create the named kubernetes_context bindings for an app config version. Each context names a peer
    terraform_module or pulumi component that emits cluster connection details as outputs.

    Args:
        app_id (str):
        body (ServiceCreateAppKubernetesContextsConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppKubernetesContextsConfig | StderrErrResponse
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
    body: ServiceCreateAppKubernetesContextsConfigRequest,
) -> Response[AppAppKubernetesContextsConfig | StderrErrResponse]:
    """create a kubernetes contexts config

     Create the named kubernetes_context bindings for an app config version. Each context names a peer
    terraform_module or pulumi component that emits cluster connection details as outputs.

    Args:
        app_id (str):
        body (ServiceCreateAppKubernetesContextsConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppKubernetesContextsConfig | StderrErrResponse]
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
    body: ServiceCreateAppKubernetesContextsConfigRequest,
) -> AppAppKubernetesContextsConfig | StderrErrResponse | None:
    """create a kubernetes contexts config

     Create the named kubernetes_context bindings for an app config version. Each context names a peer
    terraform_module or pulumi component that emits cluster connection details as outputs.

    Args:
        app_id (str):
        body (ServiceCreateAppKubernetesContextsConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppKubernetesContextsConfig | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
