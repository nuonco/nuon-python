from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_workflow import AppWorkflow
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    planonly: bool | Unset = True,
    type_: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params["planonly"] = planonly

    params["type"] = type_

    params["created_at_gte"] = created_at_gte

    params["created_at_lte"] = created_at_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/installs/{install_id}/workflows",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppWorkflow] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppWorkflow.from_dict(response_200_item_data)

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
) -> Response[StderrErrResponse | list[AppWorkflow]]:
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
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    planonly: bool | Unset = True,
    type_: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppWorkflow]]:
    """get workflows

     Return workflows for an install.

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        planonly (bool | Unset):  Default: True.
        type_ (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppWorkflow]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        offset=offset,
        limit=limit,
        page=page,
        planonly=planonly,
        type_=type_,
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
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    planonly: bool | Unset = True,
    type_: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> StderrErrResponse | list[AppWorkflow] | None:
    """get workflows

     Return workflows for an install.

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        planonly (bool | Unset):  Default: True.
        type_ (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppWorkflow]
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        offset=offset,
        limit=limit,
        page=page,
        planonly=planonly,
        type_=type_,
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    planonly: bool | Unset = True,
    type_: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppWorkflow]]:
    """get workflows

     Return workflows for an install.

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        planonly (bool | Unset):  Default: True.
        type_ (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppWorkflow]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        offset=offset,
        limit=limit,
        page=page,
        planonly=planonly,
        type_=type_,
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    page: int | Unset = 0,
    planonly: bool | Unset = True,
    type_: str | Unset = UNSET,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
) -> StderrErrResponse | list[AppWorkflow] | None:
    """get workflows

     Return workflows for an install.

    Args:
        install_id (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        page (int | Unset):  Default: 0.
        planonly (bool | Unset):  Default: True.
        type_ (str | Unset):
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppWorkflow]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            offset=offset,
            limit=limit,
            page=page,
            planonly=planonly,
            type_=type_,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
        )
    ).parsed
