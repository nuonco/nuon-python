from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_installs_health_response import ServiceInstallsHealthResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_id: str | Unset = UNSET,
    labels: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["app_id"] = app_id

    params["labels"] = labels

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/health",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceInstallsHealthResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceInstallsHealthResponse.from_dict(response.json())

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
) -> Response[ServiceInstallsHealthResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_id: str | Unset = UNSET,
    labels: str | Unset = UNSET,
) -> Response[ServiceInstallsHealthResponse | StderrErrResponse]:
    """fleet health summary

     Returns the health rollup for every install the caller can see, optionally narrowed by app and by an
    install label selector. This is the primitive a canary or bake-period rollout polls to decide
    whether to continue: all_healthy is only true when every counted install is healthy, and installs
    whose health has never been evaluated are counted separately in unset rather than treated as a pass.
    Requires the component-health feature.

    Args:
        app_id (str | Unset):
        labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallsHealthResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        labels=labels,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    app_id: str | Unset = UNSET,
    labels: str | Unset = UNSET,
) -> ServiceInstallsHealthResponse | StderrErrResponse | None:
    """fleet health summary

     Returns the health rollup for every install the caller can see, optionally narrowed by app and by an
    install label selector. This is the primitive a canary or bake-period rollout polls to decide
    whether to continue: all_healthy is only true when every counted install is healthy, and installs
    whose health has never been evaluated are counted separately in unset rather than treated as a pass.
    Requires the component-health feature.

    Args:
        app_id (str | Unset):
        labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallsHealthResponse | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        labels=labels,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_id: str | Unset = UNSET,
    labels: str | Unset = UNSET,
) -> Response[ServiceInstallsHealthResponse | StderrErrResponse]:
    """fleet health summary

     Returns the health rollup for every install the caller can see, optionally narrowed by app and by an
    install label selector. This is the primitive a canary or bake-period rollout polls to decide
    whether to continue: all_healthy is only true when every counted install is healthy, and installs
    whose health has never been evaluated are counted separately in unset rather than treated as a pass.
    Requires the component-health feature.

    Args:
        app_id (str | Unset):
        labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceInstallsHealthResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        labels=labels,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_id: str | Unset = UNSET,
    labels: str | Unset = UNSET,
) -> ServiceInstallsHealthResponse | StderrErrResponse | None:
    """fleet health summary

     Returns the health rollup for every install the caller can see, optionally narrowed by app and by an
    install label selector. This is the primitive a canary or bake-period rollout polls to decide
    whether to continue: all_healthy is only true when every counted install is healthy, and installs
    whose health has never been evaluated are counted separately in unset rather than treated as a pass.
    Requires the component-health feature.

    Args:
        app_id (str | Unset):
        labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceInstallsHealthResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            labels=labels,
        )
    ).parsed
