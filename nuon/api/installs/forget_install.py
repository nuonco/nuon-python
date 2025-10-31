from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_forget_install_request import ServiceForgetInstallRequest
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    *,
    body: ServiceForgetInstallRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/installs/{install_id}/forget",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

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
) -> Response[StderrErrResponse | bool]:
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
    body: ServiceForgetInstallRequest,
) -> Response[StderrErrResponse | bool]:
    """forget an install

     Forget an install that has been deleted outside of nuon.

    This should only be used in cases where an install was broken in an unordinary way and needs to be
    manually deleted so the parent resources can be deleted.

    Args:
        install_id (str):
        body (ServiceForgetInstallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | bool]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallRequest,
) -> StderrErrResponse | bool | None:
    """forget an install

     Forget an install that has been deleted outside of nuon.

    This should only be used in cases where an install was broken in an unordinary way and needs to be
    manually deleted so the parent resources can be deleted.

    Args:
        install_id (str):
        body (ServiceForgetInstallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | bool
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallRequest,
) -> Response[StderrErrResponse | bool]:
    """forget an install

     Forget an install that has been deleted outside of nuon.

    This should only be used in cases where an install was broken in an unordinary way and needs to be
    manually deleted so the parent resources can be deleted.

    Args:
        install_id (str):
        body (ServiceForgetInstallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | bool]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceForgetInstallRequest,
) -> StderrErrResponse | bool | None:
    """forget an install

     Forget an install that has been deleted outside of nuon.

    This should only be used in cases where an install was broken in an unordinary way and needs to be
    manually deleted so the parent resources can be deleted.

    Args:
        install_id (str):
        body (ServiceForgetInstallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | bool
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            body=body,
        )
    ).parsed
