from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_stack_service_account_response import ServiceStackServiceAccountResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/stacks/{install_id}/service-account".format(
            install_id=quote(str(install_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceStackServiceAccountResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceStackServiceAccountResponse.from_dict(response.json())

        return response_200

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
) -> Response[ServiceStackServiceAccountResponse | StderrErrResponse]:
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
) -> Response[ServiceStackServiceAccountResponse | StderrErrResponse]:
    """get an install stack's service account

     Return the service account an install stack's Terraform module authenticates as, whether it holds a
    usable API token, and the runner API URL its provider authenticates against. Never returns a token
    value: create one with POST /v1/service-accounts/{account_id}/tokens, which returns it once.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceStackServiceAccountResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceStackServiceAccountResponse | StderrErrResponse | None:
    """get an install stack's service account

     Return the service account an install stack's Terraform module authenticates as, whether it holds a
    usable API token, and the runner API URL its provider authenticates against. Never returns a token
    value: create one with POST /v1/service-accounts/{account_id}/tokens, which returns it once.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceStackServiceAccountResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceStackServiceAccountResponse | StderrErrResponse]:
    """get an install stack's service account

     Return the service account an install stack's Terraform module authenticates as, whether it holds a
    usable API token, and the runner API URL its provider authenticates against. Never returns a token
    value: create one with POST /v1/service-accounts/{account_id}/tokens, which returns it once.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceStackServiceAccountResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceStackServiceAccountResponse | StderrErrResponse | None:
    """get an install stack's service account

     Return the service account an install stack's Terraform module authenticates as, whether it holds a
    usable API token, and the runner API URL its provider authenticates against. Never returns a token
    value: create one with POST /v1/service-accounts/{account_id}/tokens, which returns it once.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceStackServiceAccountResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
        )
    ).parsed
