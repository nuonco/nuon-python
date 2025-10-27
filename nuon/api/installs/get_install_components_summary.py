from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_component_summary import AppInstallComponentSummary
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    *,
    types: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
    q: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["types"] = types

    params["offset"] = offset

    params["limit"] = limit

    params["page"] = page

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/installs/{install_id}/components/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[StderrErrResponse, list["AppInstallComponentSummary"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppInstallComponentSummary.from_dict(response_200_item_data)

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[StderrErrResponse, list["AppInstallComponentSummary"]]]:
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
    types: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
    q: Union[Unset, str] = UNSET,
) -> Response[Union[StderrErrResponse, list["AppInstallComponentSummary"]]]:
    """get an installs components summary

    Args:
        install_id (str):
        types (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, list['AppInstallComponentSummary']]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        types=types,
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
    types: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
    q: Union[Unset, str] = UNSET,
) -> Optional[Union[StderrErrResponse, list["AppInstallComponentSummary"]]]:
    """get an installs components summary

    Args:
        install_id (str):
        types (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, list['AppInstallComponentSummary']]
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        types=types,
        offset=offset,
        limit=limit,
        page=page,
        q=q,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    types: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
    q: Union[Unset, str] = UNSET,
) -> Response[Union[StderrErrResponse, list["AppInstallComponentSummary"]]]:
    """get an installs components summary

    Args:
        install_id (str):
        types (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, list['AppInstallComponentSummary']]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        types=types,
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
    types: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 10,
    page: Union[Unset, int] = 0,
    q: Union[Unset, str] = UNSET,
) -> Optional[Union[StderrErrResponse, list["AppInstallComponentSummary"]]]:
    """get an installs components summary

    Args:
        install_id (str):
        types (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 10.
        page (Union[Unset, int]):  Default: 0.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, list['AppInstallComponentSummary']]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            types=types,
            offset=offset,
            limit=limit,
            page=page,
            q=q,
        )
    ).parsed
