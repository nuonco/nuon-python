from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_get_install_activity_response import ServiceGetInstallActivityResponse
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

    params["search"] = search

    params["created_at_gte"] = created_at_gte

    params["created_at_lte"] = created_at_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/activity".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceGetInstallActivityResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceGetInstallActivityResponse.from_dict(response.json())

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
) -> Response[ServiceGetInstallActivityResponse | StderrErrResponse]:
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
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[ServiceGetInstallActivityResponse | StderrErrResponse]:
    """get normalized activity feed for an install

     Returns a normalized, chronological activity feed for an install.

    Each record is a top-level operation that ran against the install rather than a change to it: a
    standalone action run, a runbook run, or an install-scoped policy check. Action runs executed as
    steps within another workflow are omitted. Policy checks recorded only against a component build,
    with no install, are also omitted.

    Records include a `type` (`action_run`, `runbook_run`, or `policy_check`), a `status` taken from
    that source, a human-readable `title` and `summary`, and a type-specific payload (`action`,
    `runbook`, or `policy`). Action and runbook records include a `workflow` reference when the run has
    one.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`. `status` matches each source's own status string.
    Action and runbook runs use values such as `queued`, `in-progress`, `finished`, and `error`. Policy
    checks use `success`, `warning`, and `error`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceGetInstallActivityResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
        type_=type_,
        status=status,
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
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> ServiceGetInstallActivityResponse | StderrErrResponse | None:
    """get normalized activity feed for an install

     Returns a normalized, chronological activity feed for an install.

    Each record is a top-level operation that ran against the install rather than a change to it: a
    standalone action run, a runbook run, or an install-scoped policy check. Action runs executed as
    steps within another workflow are omitted. Policy checks recorded only against a component build,
    with no install, are also omitted.

    Records include a `type` (`action_run`, `runbook_run`, or `policy_check`), a `status` taken from
    that source, a human-readable `title` and `summary`, and a type-specific payload (`action`,
    `runbook`, or `policy`). Action and runbook records include a `workflow` reference when the run has
    one.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`. `status` matches each source's own status string.
    Action and runbook runs use values such as `queued`, `in-progress`, `finished`, and `error`. Policy
    checks use `success`, `warning`, and `error`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceGetInstallActivityResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        page=page,
        offset=offset,
        limit=limit,
        type_=type_,
        status=status,
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
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[ServiceGetInstallActivityResponse | StderrErrResponse]:
    """get normalized activity feed for an install

     Returns a normalized, chronological activity feed for an install.

    Each record is a top-level operation that ran against the install rather than a change to it: a
    standalone action run, a runbook run, or an install-scoped policy check. Action runs executed as
    steps within another workflow are omitted. Policy checks recorded only against a component build,
    with no install, are also omitted.

    Records include a `type` (`action_run`, `runbook_run`, or `policy_check`), a `status` taken from
    that source, a human-readable `title` and `summary`, and a type-specific payload (`action`,
    `runbook`, or `policy`). Action and runbook records include a `workflow` reference when the run has
    one.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`. `status` matches each source's own status string.
    Action and runbook runs use values such as `queued`, `in-progress`, `finished`, and `error`. Policy
    checks use `success`, `warning`, and `error`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceGetInstallActivityResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        page=page,
        offset=offset,
        limit=limit,
        type_=type_,
        status=status,
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
    search: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> ServiceGetInstallActivityResponse | StderrErrResponse | None:
    """get normalized activity feed for an install

     Returns a normalized, chronological activity feed for an install.

    Each record is a top-level operation that ran against the install rather than a change to it: a
    standalone action run, a runbook run, or an install-scoped policy check. Action runs executed as
    steps within another workflow are omitted. Policy checks recorded only against a component build,
    with no install, are also omitted.

    Records include a `type` (`action_run`, `runbook_run`, or `policy_check`), a `status` taken from
    that source, a human-readable `title` and `summary`, and a type-specific payload (`action`,
    `runbook`, or `policy`). Action and runbook records include a `workflow` reference when the run has
    one.

    Supports pagination via `page`/`offset`/`limit`/`has_more`, and filtering by `type`, `status`,
    `search`, `created_at_gte`, and `created_at_lte`. `status` matches each source's own status string.
    Action and runbook runs use values such as `queued`, `in-progress`, `finished`, and `error`. Policy
    checks use `success`, `warning`, and `error`.

    Args:
        install_id (str):
        page (int | Unset):  Default: 0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        status (str | Unset):
        search (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceGetInstallActivityResponse | StderrErrResponse
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
            search=search,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
        )
    ).parsed
