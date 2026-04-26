from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_action_workflow import AppActionWorkflow
from ...models.service_remove_action_labels_request import ServiceRemoveActionLabelsRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    action_id: str,
    *,
    body: ServiceRemoveActionLabelsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/apps/{app_id}/actions/{action_id}/labels".format(
            app_id=quote(str(app_id), safe=""),
            action_id=quote(str(action_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppActionWorkflow | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppActionWorkflow.from_dict(response.json())

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
) -> Response[AppActionWorkflow | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRemoveActionLabelsRequest,
) -> Response[AppActionWorkflow | StderrErrResponse]:
    """remove labels from an action

     Remove the specified label keys from the action.

    Args:
        app_id (str):
        action_id (str):
        body (ServiceRemoveActionLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppActionWorkflow | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        action_id=action_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRemoveActionLabelsRequest,
) -> AppActionWorkflow | StderrErrResponse | None:
    """remove labels from an action

     Remove the specified label keys from the action.

    Args:
        app_id (str):
        action_id (str):
        body (ServiceRemoveActionLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppActionWorkflow | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        action_id=action_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRemoveActionLabelsRequest,
) -> Response[AppActionWorkflow | StderrErrResponse]:
    """remove labels from an action

     Remove the specified label keys from the action.

    Args:
        app_id (str):
        action_id (str):
        body (ServiceRemoveActionLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppActionWorkflow | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        action_id=action_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRemoveActionLabelsRequest,
) -> AppActionWorkflow | StderrErrResponse | None:
    """remove labels from an action

     Remove the specified label keys from the action.

    Args:
        app_id (str):
        action_id (str):
        body (ServiceRemoveActionLabelsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppActionWorkflow | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            action_id=action_id,
            client=client,
            body=body,
        )
    ).parsed
