from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_audit_log import AppInstallAuditLog
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response


def _get_kwargs(
    install_id: str,
    *,
    start: str,
    end: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/installs/{install_id}/audit_logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[StderrErrResponse, list["AppInstallAuditLog"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for response_200_item_data in _response_200:
            response_200_item = AppInstallAuditLog.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.text)

        return response_400
    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.text)

        return response_401
    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.text)

        return response_403
    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.text)

        return response_404
    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[StderrErrResponse, list["AppInstallAuditLog"]]]:
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
    start: str,
    end: str,
) -> Response[Union[StderrErrResponse, list["AppInstallAuditLog"]]]:
    """get install audit logs

    Args:
        install_id (str):
        start (str):
        end (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, list['AppInstallAuditLog']]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
) -> Optional[Union[StderrErrResponse, list["AppInstallAuditLog"]]]:
    """get install audit logs

    Args:
        install_id (str):
        start (str):
        end (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, list['AppInstallAuditLog']]
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
) -> Response[Union[StderrErrResponse, list["AppInstallAuditLog"]]]:
    """get install audit logs

    Args:
        install_id (str):
        start (str):
        end (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, list['AppInstallAuditLog']]]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
) -> Optional[Union[StderrErrResponse, list["AppInstallAuditLog"]]]:
    """get install audit logs

    Args:
        install_id (str):
        start (str):
        end (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, list['AppInstallAuditLog']]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            start=start,
            end=end,
        )
    ).parsed
