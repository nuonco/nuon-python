from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_app_policies_config import AppAppPoliciesConfig
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/apps/{app_id}/latest-app-policies-config",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppAppPoliciesConfig | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppAppPoliciesConfig.from_dict(response.json())

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
) -> Response[AppAppPoliciesConfig | StderrErrResponse]:
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
) -> Response[AppAppPoliciesConfig | StderrErrResponse]:
    """get latest app policies config

     Get latest app policies config.

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppPoliciesConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
) -> AppAppPoliciesConfig | StderrErrResponse | None:
    """get latest app policies config

     Get latest app policies config.

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppPoliciesConfig | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppAppPoliciesConfig | StderrErrResponse]:
    """get latest app policies config

     Get latest app policies config.

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppAppPoliciesConfig | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
) -> AppAppPoliciesConfig | StderrErrResponse | None:
    """get latest app policies config

     Get latest app policies config.

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppAppPoliciesConfig | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
        )
    ).parsed
