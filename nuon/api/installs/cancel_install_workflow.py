from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_workflow_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/install-workflows/{install_workflow_id}/cancel",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[StderrErrResponse, bool]]:
    if response.status_code == 202:
        response_202 = cast(bool, response.json())
        return response_202
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
) -> Response[Union[StderrErrResponse, bool]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[StderrErrResponse, bool]]:
    """cancel an ongoing install workflow

    Args:
        install_workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, bool]]
    """

    kwargs = _get_kwargs(
        install_workflow_id=install_workflow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[StderrErrResponse, bool]]:
    """cancel an ongoing install workflow

    Args:
        install_workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, bool]
    """

    return sync_detailed(
        install_workflow_id=install_workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[StderrErrResponse, bool]]:
    """cancel an ongoing install workflow

    Args:
        install_workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StderrErrResponse, bool]]
    """

    kwargs = _get_kwargs(
        install_workflow_id=install_workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[StderrErrResponse, bool]]:
    """cancel an ongoing install workflow

    Args:
        install_workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StderrErrResponse, bool]
    """

    return (
        await asyncio_detailed(
            install_workflow_id=install_workflow_id,
            client=client,
        )
    ).parsed
