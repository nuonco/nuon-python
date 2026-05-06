from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_current_org_webhook_response import ServiceCurrentOrgWebhookResponse
from ...models.service_update_current_org_webhook_request import ServiceUpdateCurrentOrgWebhookRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    webhook_id: str,
    *,
    body: ServiceUpdateCurrentOrgWebhookRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/orgs/current/webhooks/{webhook_id}".format(
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceCurrentOrgWebhookResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceCurrentOrgWebhookResponse.from_dict(response.json())

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
) -> Response[ServiceCurrentOrgWebhookResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateCurrentOrgWebhookRequest,
) -> Response[ServiceCurrentOrgWebhookResponse | StderrErrResponse]:
    """update a webhook for the current org

     Replaces the webhook's interests filter and/or rotates its signing secret. WebhookURL is part of the
    (org_id, webhook_url) unique index and cannot be changed in place — delete and recreate to rename.

    Args:
        webhook_id (str):
        body (ServiceUpdateCurrentOrgWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCurrentOrgWebhookResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateCurrentOrgWebhookRequest,
) -> ServiceCurrentOrgWebhookResponse | StderrErrResponse | None:
    """update a webhook for the current org

     Replaces the webhook's interests filter and/or rotates its signing secret. WebhookURL is part of the
    (org_id, webhook_url) unique index and cannot be changed in place — delete and recreate to rename.

    Args:
        webhook_id (str):
        body (ServiceUpdateCurrentOrgWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCurrentOrgWebhookResponse | StderrErrResponse
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateCurrentOrgWebhookRequest,
) -> Response[ServiceCurrentOrgWebhookResponse | StderrErrResponse]:
    """update a webhook for the current org

     Replaces the webhook's interests filter and/or rotates its signing secret. WebhookURL is part of the
    (org_id, webhook_url) unique index and cannot be changed in place — delete and recreate to rename.

    Args:
        webhook_id (str):
        body (ServiceUpdateCurrentOrgWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCurrentOrgWebhookResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceUpdateCurrentOrgWebhookRequest,
) -> ServiceCurrentOrgWebhookResponse | StderrErrResponse | None:
    """update a webhook for the current org

     Replaces the webhook's interests filter and/or rotates its signing secret. WebhookURL is part of the
    (org_id, webhook_url) unique index and cannot be changed in place — delete and recreate to rename.

    Args:
        webhook_id (str):
        body (ServiceUpdateCurrentOrgWebhookRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCurrentOrgWebhookResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            body=body,
        )
    ).parsed
