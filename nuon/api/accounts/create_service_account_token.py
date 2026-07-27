from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_create_service_account_token_request import ServiceCreateServiceAccountTokenRequest
from ...models.service_create_service_account_token_response import ServiceCreateServiceAccountTokenResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ServiceCreateServiceAccountTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/service-accounts/{account_id}/tokens".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceCreateServiceAccountTokenResponse | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = ServiceCreateServiceAccountTokenResponse.from_dict(response.json())

        return response_201

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
) -> Response[ServiceCreateServiceAccountTokenResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateServiceAccountTokenRequest,
) -> Response[ServiceCreateServiceAccountTokenResponse | StderrErrResponse]:
    """Create a token for a service account in the current org

     Create an API token for a service account in the current org.

    Defaults to a duration of one year (`8760h`) if `duration` is not
    specified. If `invalidate` is set, all existing tokens for the service
    account are invalidated before the new token is created.

    Args:
        account_id (str):
        body (ServiceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCreateServiceAccountTokenResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateServiceAccountTokenRequest,
) -> ServiceCreateServiceAccountTokenResponse | StderrErrResponse | None:
    """Create a token for a service account in the current org

     Create an API token for a service account in the current org.

    Defaults to a duration of one year (`8760h`) if `duration` is not
    specified. If `invalidate` is set, all existing tokens for the service
    account are invalidated before the new token is created.

    Args:
        account_id (str):
        body (ServiceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCreateServiceAccountTokenResponse | StderrErrResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateServiceAccountTokenRequest,
) -> Response[ServiceCreateServiceAccountTokenResponse | StderrErrResponse]:
    """Create a token for a service account in the current org

     Create an API token for a service account in the current org.

    Defaults to a duration of one year (`8760h`) if `duration` is not
    specified. If `invalidate` is set, all existing tokens for the service
    account are invalidated before the new token is created.

    Args:
        account_id (str):
        body (ServiceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCreateServiceAccountTokenResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceCreateServiceAccountTokenRequest,
) -> ServiceCreateServiceAccountTokenResponse | StderrErrResponse | None:
    """Create a token for a service account in the current org

     Create an API token for a service account in the current org.

    Defaults to a duration of one year (`8760h`) if `duration` is not
    specified. If `invalidate` is set, all existing tokens for the service
    account are invalidated before the new token is created.

    Args:
        account_id (str):
        body (ServiceCreateServiceAccountTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCreateServiceAccountTokenResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
