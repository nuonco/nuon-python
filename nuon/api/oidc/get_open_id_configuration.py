from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oidcissuer_discovery_document import OidcissuerDiscoveryDocument
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/.well-known/openid-configuration",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OidcissuerDiscoveryDocument | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = OidcissuerDiscoveryDocument.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = StderrErrResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OidcissuerDiscoveryDocument | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[OidcissuerDiscoveryDocument | StderrErrResponse]:
    """Get OIDC discovery document

     Returns the OIDC discovery document cloud providers use to federate to this control plane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OidcissuerDiscoveryDocument | StderrErrResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> OidcissuerDiscoveryDocument | StderrErrResponse | None:
    """Get OIDC discovery document

     Returns the OIDC discovery document cloud providers use to federate to this control plane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OidcissuerDiscoveryDocument | StderrErrResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[OidcissuerDiscoveryDocument | StderrErrResponse]:
    """Get OIDC discovery document

     Returns the OIDC discovery document cloud providers use to federate to this control plane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OidcissuerDiscoveryDocument | StderrErrResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> OidcissuerDiscoveryDocument | StderrErrResponse | None:
    """Get OIDC discovery document

     Returns the OIDC discovery document cloud providers use to federate to this control plane.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OidcissuerDiscoveryDocument | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
