from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_get_install_url_response import ServiceGetInstallURLResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    org_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/orgs/{org_id}/slack/install-url".format(
            org_id=quote(str(org_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceGetInstallURLResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceGetInstallURLResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StderrErrResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StderrErrResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ServiceGetInstallURLResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceGetInstallURLResponse | StderrErrResponse]:
    """Get the Slack OAuth install URL for the current org

     Returns a Slack OAuth v2 authorize URL with a signed state JWT bound to the calling account and org.
    The dashboard redirects the user to this URL to begin the install flow.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceGetInstallURLResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceGetInstallURLResponse | StderrErrResponse | None:
    """Get the Slack OAuth install URL for the current org

     Returns a Slack OAuth v2 authorize URL with a signed state JWT bound to the calling account and org.
    The dashboard redirects the user to this URL to begin the install flow.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceGetInstallURLResponse | StderrErrResponse
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServiceGetInstallURLResponse | StderrErrResponse]:
    """Get the Slack OAuth install URL for the current org

     Returns a Slack OAuth v2 authorize URL with a signed state JWT bound to the calling account and org.
    The dashboard redirects the user to this URL to begin the install flow.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceGetInstallURLResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> ServiceGetInstallURLResponse | StderrErrResponse | None:
    """Get the Slack OAuth install URL for the current org

     Returns a Slack OAuth v2 authorize URL with a signed state JWT bound to the calling account and org.
    The dashboard redirects the user to this URL to begin the install flow.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceGetInstallURLResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
        )
    ).parsed
