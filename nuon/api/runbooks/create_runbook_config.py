from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_runbook_config import AppRunbookConfig
from ...models.service_create_runbook_config_request import ServiceCreateRunbookConfigRequest
from ...types import Response


def _get_kwargs(
    app_id: str,
    runbook_id: str,
    *,
    body: ServiceCreateRunbookConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/apps/{app_id}/runbooks/{runbook_id}/configs".format(
            app_id=quote(str(app_id), safe=""),
            runbook_id=quote(str(runbook_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppRunbookConfig | None:
    if response.status_code == 201:
        response_201 = AppRunbookConfig.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppRunbookConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateRunbookConfigRequest,
) -> Response[AppRunbookConfig]:
    """create a runbook config

    Args:
        app_id (str):
        runbook_id (str):
        body (ServiceCreateRunbookConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRunbookConfig]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        runbook_id=runbook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateRunbookConfigRequest,
) -> AppRunbookConfig | None:
    """create a runbook config

    Args:
        app_id (str):
        runbook_id (str):
        body (ServiceCreateRunbookConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRunbookConfig
    """

    return sync_detailed(
        app_id=app_id,
        runbook_id=runbook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateRunbookConfigRequest,
) -> Response[AppRunbookConfig]:
    """create a runbook config

    Args:
        app_id (str):
        runbook_id (str):
        body (ServiceCreateRunbookConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppRunbookConfig]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        runbook_id=runbook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    runbook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateRunbookConfigRequest,
) -> AppRunbookConfig | None:
    """create a runbook config

    Args:
        app_id (str):
        runbook_id (str):
        body (ServiceCreateRunbookConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppRunbookConfig
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            runbook_id=runbook_id,
            client=client,
            body=body,
        )
    ).parsed
