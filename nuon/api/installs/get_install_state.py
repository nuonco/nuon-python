from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_powertoolsdev_mono_pkg_types_state_state import GithubComPowertoolsdevMonoPkgTypesStateState
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/installs/{install_id}/state",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]:
    if response.status_code == 200:
        response_200 = GithubComPowertoolsdevMonoPkgTypesStateState.from_dict(response.json())

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
) -> Response[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]:
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
) -> Response[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]:
    """Get the current state of an install.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]
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
) -> Optional[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]:
    """Get the current state of an install.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]
    """

    return sync_detailed(
        install_id=install_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]:
    """Get the current state of an install.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]
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
) -> Optional[Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]]:
    """Get the current state of an install.

    Args:
        install_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GithubComPowertoolsdevMonoPkgTypesStateState, StderrErrResponse]
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
        )
    ).parsed
