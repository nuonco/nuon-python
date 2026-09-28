from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_get_install_deployments_response import ServiceGetInstallDeploymentsResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["offset"] = offset

    params["limit"] = limit

    params["type"] = type_

    params["status"] = status

    params["resource"] = resource

    params["search"] = search

    params["created_at_gte"] = created_at_gte

    params["created_at_lte"] = created_at_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/deployments".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceGetInstallDeploymentsResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceGetInstallDeploymentsResponse.from_dict(response.json())

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
) -> Response[ServiceGetInstallDeploymentsResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[ServiceGetInstallDeploymentsResponse | StderrErrResponse]:
    """get normalized deployment feed for an install

     Returns a normalized, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning,
    action runs, runbook runs, and install-config updates. Plan-only and preview records are excluded.

    Records include a `type`, unified `status`, human-readable `title` and `summary`, an optional
    `workflow` reference, an optional `app_branch` reference (when the change originated from a branch
    run), an optional primary `component` reference (for single-component operations), a flat
    `affected_resources` list of component names, and `change_groups` that group the affected resources
    by logical category.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        resource (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceGetInstallDeploymentsResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
        type_=type_,
        status=status,
        resource=resource,
        search=search,
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> ServiceGetInstallDeploymentsResponse | StderrErrResponse | None:
    """get normalized deployment feed for an install

     Returns a normalized, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning,
    action runs, runbook runs, and install-config updates. Plan-only and preview records are excluded.

    Records include a `type`, unified `status`, human-readable `title` and `summary`, an optional
    `workflow` reference, an optional `app_branch` reference (when the change originated from a branch
    run), an optional primary `component` reference (for single-component operations), a flat
    `affected_resources` list of component names, and `change_groups` that group the affected resources
    by logical category.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        resource (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceGetInstallDeploymentsResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        page=page,
        offset=offset,
        limit=limit,
        type_=type_,
        status=status,
        resource=resource,
        search=search,
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[ServiceGetInstallDeploymentsResponse | StderrErrResponse]:
    """get normalized deployment feed for an install

     Returns a normalized, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning,
    action runs, runbook runs, and install-config updates. Plan-only and preview records are excluded.

    Records include a `type`, unified `status`, human-readable `title` and `summary`, an optional
    `workflow` reference, an optional `app_branch` reference (when the change originated from a branch
    run), an optional primary `component` reference (for single-component operations), a flat
    `affected_resources` list of component names, and `change_groups` that group the affected resources
    by logical category.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        resource (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceGetInstallDeploymentsResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
        type_=type_,
        status=status,
        resource=resource,
        search=search,
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> ServiceGetInstallDeploymentsResponse | StderrErrResponse | None:
    """get normalized deployment feed for an install

     Returns a normalized, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning,
    action runs, runbook runs, and install-config updates. Plan-only and preview records are excluded.

    Records include a `type`, unified `status`, human-readable `title` and `summary`, an optional
    `workflow` reference, an optional `app_branch` reference (when the change originated from a branch
    run), an optional primary `component` reference (for single-component operations), a flat
    `affected_resources` list of component names, and `change_groups` that group the affected resources
    by logical category.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        resource (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceGetInstallDeploymentsResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            page=page,
            offset=offset,
            limit=limit,
            type_=type_,
            status=status,
            resource=resource,
            search=search,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
        )
    ).parsed
