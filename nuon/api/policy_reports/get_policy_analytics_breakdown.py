from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_policy_analytics_breakdown import ServicePolicyAnalyticsBreakdown
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    dimension: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    install_id: str | Unset = UNSET,
    policy_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["dimension"] = dimension

    params["start"] = start

    params["end"] = end

    params["install_id"] = install_id

    params["policy_id"] = policy_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/policy-analytics/breakdown".format(
            app_id=quote(str(app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServicePolicyAnalyticsBreakdown | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServicePolicyAnalyticsBreakdown.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServicePolicyAnalyticsBreakdown | StderrErrResponse]:
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
    dimension: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    install_id: str | Unset = UNSET,
    policy_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ServicePolicyAnalyticsBreakdown | StderrErrResponse]:
    """get policy analytics breakdown by dimension

     Returns policy evaluation counts broken down by a single dimension (policy_id, install_id, or
    owner_type), sorted by violation count (denies first, then warns). Use this to identify which
    policies, installs, or lifecycle stages produce the most violations.

    Args:
        app_id (str):
        dimension (str):
        start (str | Unset):
        end (str | Unset):
        install_id (str | Unset):
        policy_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServicePolicyAnalyticsBreakdown | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        dimension=dimension,
        start=start,
        end=end,
        install_id=install_id,
        policy_id=policy_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    dimension: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    install_id: str | Unset = UNSET,
    policy_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ServicePolicyAnalyticsBreakdown | StderrErrResponse | None:
    """get policy analytics breakdown by dimension

     Returns policy evaluation counts broken down by a single dimension (policy_id, install_id, or
    owner_type), sorted by violation count (denies first, then warns). Use this to identify which
    policies, installs, or lifecycle stages produce the most violations.

    Args:
        app_id (str):
        dimension (str):
        start (str | Unset):
        end (str | Unset):
        install_id (str | Unset):
        policy_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServicePolicyAnalyticsBreakdown | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        dimension=dimension,
        start=start,
        end=end,
        install_id=install_id,
        policy_id=policy_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    dimension: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    install_id: str | Unset = UNSET,
    policy_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ServicePolicyAnalyticsBreakdown | StderrErrResponse]:
    """get policy analytics breakdown by dimension

     Returns policy evaluation counts broken down by a single dimension (policy_id, install_id, or
    owner_type), sorted by violation count (denies first, then warns). Use this to identify which
    policies, installs, or lifecycle stages produce the most violations.

    Args:
        app_id (str):
        dimension (str):
        start (str | Unset):
        end (str | Unset):
        install_id (str | Unset):
        policy_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServicePolicyAnalyticsBreakdown | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        dimension=dimension,
        start=start,
        end=end,
        install_id=install_id,
        policy_id=policy_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    dimension: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    install_id: str | Unset = UNSET,
    policy_id: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ServicePolicyAnalyticsBreakdown | StderrErrResponse | None:
    """get policy analytics breakdown by dimension

     Returns policy evaluation counts broken down by a single dimension (policy_id, install_id, or
    owner_type), sorted by violation count (denies first, then warns). Use this to identify which
    policies, installs, or lifecycle stages produce the most violations.

    Args:
        app_id (str):
        dimension (str):
        start (str | Unset):
        end (str | Unset):
        install_id (str | Unset):
        policy_id (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServicePolicyAnalyticsBreakdown | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            dimension=dimension,
            start=start,
            end=end,
            install_id=install_id,
            policy_id=policy_id,
            limit=limit,
        )
    ).parsed
