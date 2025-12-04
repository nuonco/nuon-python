from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_action_workflow import AppInstallActionWorkflow
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    trigger_types: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["trigger_types"] = trigger_types

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/installs/{install_id}/actions/latest-runs".format(
            install_id=quote(str(install_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppInstallActionWorkflow] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppInstallActionWorkflow.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[StderrErrResponse | list[AppInstallActionWorkflow]]:
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
    trigger_types: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppInstallActionWorkflow]]:
    """get latest runs for all action workflows by install id

    Args:
        install_id (str):
        trigger_types (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppInstallActionWorkflow]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        trigger_types=trigger_types,
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    trigger_types: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> StderrErrResponse | list[AppInstallActionWorkflow] | None:
    """get latest runs for all action workflows by install id

    Args:
        install_id (str):
        trigger_types (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppInstallActionWorkflow]
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        trigger_types=trigger_types,
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    trigger_types: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppInstallActionWorkflow]]:
    """get latest runs for all action workflows by install id

    Args:
        install_id (str):
        trigger_types (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppInstallActionWorkflow]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        trigger_types=trigger_types,
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    trigger_types: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    q: str | Unset = UNSET,
) -> StderrErrResponse | list[AppInstallActionWorkflow] | None:
    """get latest runs for all action workflows by install id

    Args:
        install_id (str):
        trigger_types (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppInstallActionWorkflow]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            trigger_types=trigger_types,
            offset=offset,
            limit=limit,
            page=page,
            q=q,
        )
    ).parsed
