from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_install_deployment_summaries_sort import GetInstallDeploymentSummariesSort
from ...models.get_install_deployment_summaries_state import GetInstallDeploymentSummariesState
from ...models.service_get_install_deployment_summaries_response import ServiceGetInstallDeploymentSummariesResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    page: int | Unset = 0,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
    state: GetInstallDeploymentSummariesState | Unset = UNSET,
    sort: GetInstallDeploymentSummariesSort | Unset = UNSET,
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

    params["cursor"] = cursor

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["type"] = type_

    params["status"] = status

    params["resource"] = resource

    params["search"] = search

    params["created_at_gte"] = created_at_gte

    params["created_at_lte"] = created_at_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/deployment-summaries".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceGetInstallDeploymentSummariesResponse.from_dict(response.json())

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
) -> Response[ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse]:
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
    cursor: str | Unset = UNSET,
    state: GetInstallDeploymentSummariesState | Unset = UNSET,
    sort: GetInstallDeploymentSummariesSort | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse]:
    """get lightweight deployment summaries for an install

     Returns a lightweight, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning, and
    install-config updates. Action runs, runbook runs, and policy checks are returned by the activity
    feed. Plan-only and preview records are excluded.

    Records include a `type`, workflow `status`, `title`, `activity`, `finished`, and slim workflow
    `steps` for progress and resource outcomes. Use the single deployment endpoint for app branch,
    image, affected resource, and change details.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `resource`, `search`, `created_at_gte`, and `created_at_lte`.

    `state=active` returns deployments whose workflow status is pending, queued, in progress, retrying,
    awaiting approval, approved, or failed pending retry. `state=finished` returns every other status.
    When `state=active`, `total` counts all matching active deployments, ignoring `limit` and `cursor`.

    `sort=attention` orders deployments awaiting approval first, failed pending retry second, then all
    others. Each group is ordered newest first. The default order is newest first.

    When `has_more` is true, `next_cursor` is an opaque cursor for the next page. Pass it back as
    `cursor` with the same `state` and `sort`. A cursor cannot be combined with a non-zero `page` or
    `offset`. An invalid `state`, `sort`, or `cursor` returns 400.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        state (GetInstallDeploymentSummariesState | Unset):
        sort (GetInstallDeploymentSummariesSort | Unset):
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
        Response[ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
        cursor=cursor,
        state=state,
        sort=sort,
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
    cursor: str | Unset = UNSET,
    state: GetInstallDeploymentSummariesState | Unset = UNSET,
    sort: GetInstallDeploymentSummariesSort | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse | None:
    """get lightweight deployment summaries for an install

     Returns a lightweight, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning, and
    install-config updates. Action runs, runbook runs, and policy checks are returned by the activity
    feed. Plan-only and preview records are excluded.

    Records include a `type`, workflow `status`, `title`, `activity`, `finished`, and slim workflow
    `steps` for progress and resource outcomes. Use the single deployment endpoint for app branch,
    image, affected resource, and change details.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `resource`, `search`, `created_at_gte`, and `created_at_lte`.

    `state=active` returns deployments whose workflow status is pending, queued, in progress, retrying,
    awaiting approval, approved, or failed pending retry. `state=finished` returns every other status.
    When `state=active`, `total` counts all matching active deployments, ignoring `limit` and `cursor`.

    `sort=attention` orders deployments awaiting approval first, failed pending retry second, then all
    others. Each group is ordered newest first. The default order is newest first.

    When `has_more` is true, `next_cursor` is an opaque cursor for the next page. Pass it back as
    `cursor` with the same `state` and `sort`. A cursor cannot be combined with a non-zero `page` or
    `offset`. An invalid `state`, `sort`, or `cursor` returns 400.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        state (GetInstallDeploymentSummariesState | Unset):
        sort (GetInstallDeploymentSummariesSort | Unset):
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
        ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        page=page,
        offset=offset,
        limit=limit,
        cursor=cursor,
        state=state,
        sort=sort,
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
    cursor: str | Unset = UNSET,
    state: GetInstallDeploymentSummariesState | Unset = UNSET,
    sort: GetInstallDeploymentSummariesSort | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse]:
    """get lightweight deployment summaries for an install

     Returns a lightweight, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning, and
    install-config updates. Action runs, runbook runs, and policy checks are returned by the activity
    feed. Plan-only and preview records are excluded.

    Records include a `type`, workflow `status`, `title`, `activity`, `finished`, and slim workflow
    `steps` for progress and resource outcomes. Use the single deployment endpoint for app branch,
    image, affected resource, and change details.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `resource`, `search`, `created_at_gte`, and `created_at_lte`.

    `state=active` returns deployments whose workflow status is pending, queued, in progress, retrying,
    awaiting approval, approved, or failed pending retry. `state=finished` returns every other status.
    When `state=active`, `total` counts all matching active deployments, ignoring `limit` and `cursor`.

    `sort=attention` orders deployments awaiting approval first, failed pending retry second, then all
    others. Each group is ordered newest first. The default order is newest first.

    When `has_more` is true, `next_cursor` is an opaque cursor for the next page. Pass it back as
    `cursor` with the same `state` and `sort`. A cursor cannot be combined with a non-zero `page` or
    `offset`. An invalid `state`, `sort`, or `cursor` returns 400.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        state (GetInstallDeploymentSummariesState | Unset):
        sort (GetInstallDeploymentSummariesSort | Unset):
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
        Response[ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
        cursor=cursor,
        state=state,
        sort=sort,
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
    cursor: str | Unset = UNSET,
    state: GetInstallDeploymentSummariesState | Unset = UNSET,
    sort: GetInstallDeploymentSummariesSort | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    resource: str | Unset = UNSET,
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse | None:
    """get lightweight deployment summaries for an install

     Returns a lightweight, chronological deployment feed for an install.

    Each record represents one install-owned workflow that caused a real change: provisioning,
    reprovisioning, component deploys, input updates, stack reprovisioning, sandbox reprovisioning, and
    install-config updates. Action runs, runbook runs, and policy checks are returned by the activity
    feed. Plan-only and preview records are excluded.

    Records include a `type`, workflow `status`, `title`, `activity`, `finished`, and slim workflow
    `steps` for progress and resource outcomes. Use the single deployment endpoint for app branch,
    image, affected resource, and change details.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `resource`, `search`, `created_at_gte`, and `created_at_lte`.

    `state=active` returns deployments whose workflow status is pending, queued, in progress, retrying,
    awaiting approval, approved, or failed pending retry. `state=finished` returns every other status.
    When `state=active`, `total` counts all matching active deployments, ignoring `limit` and `cursor`.

    `sort=attention` orders deployments awaiting approval first, failed pending retry second, then all
    others. Each group is ordered newest first. The default order is newest first.

    When `has_more` is true, `next_cursor` is an opaque cursor for the next page. Pass it back as
    `cursor` with the same `state` and `sort`. A cursor cannot be combined with a non-zero `page` or
    `offset`. An invalid `state`, `sort`, or `cursor` returns 400.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):
        state (GetInstallDeploymentSummariesState | Unset):
        sort (GetInstallDeploymentSummariesSort | Unset):
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
        ServiceGetInstallDeploymentSummariesResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            page=page,
            offset=offset,
            limit=limit,
            cursor=cursor,
            state=state,
            sort=sort,
            type_=type_,
            status=status,
            resource=resource,
            search=search,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
        )
    ).parsed
