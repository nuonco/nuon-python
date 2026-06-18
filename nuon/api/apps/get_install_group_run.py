from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_install_group_run import AppInstallGroupRun
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    app_branch_id: str,
    run_id: str,
    install_group_run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/branches/{app_branch_id}/runs/{run_id}/install-group-runs/{install_group_run_id}".format(
            app_id=quote(str(app_id), safe=""),
            app_branch_id=quote(str(app_branch_id), safe=""),
            run_id=quote(str(run_id), safe=""),
            install_group_run_id=quote(str(install_group_run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppInstallGroupRun | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppInstallGroupRun.from_dict(response.json())

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
) -> Response[AppInstallGroupRun | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    app_branch_id: str,
    run_id: str,
    install_group_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppInstallGroupRun | StderrErrResponse]:
    """get a specific install group run

     Returns a single install group run with full details

    Args:
        app_id (str):
        app_branch_id (str):
        run_id (str):
        install_group_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallGroupRun | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
        run_id=run_id,
        install_group_run_id=install_group_run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    app_branch_id: str,
    run_id: str,
    install_group_run_id: str,
    *,
    client: AuthenticatedClient,
) -> AppInstallGroupRun | StderrErrResponse | None:
    """get a specific install group run

     Returns a single install group run with full details

    Args:
        app_id (str):
        app_branch_id (str):
        run_id (str):
        install_group_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallGroupRun | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        app_branch_id=app_branch_id,
        run_id=run_id,
        install_group_run_id=install_group_run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    app_branch_id: str,
    run_id: str,
    install_group_run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppInstallGroupRun | StderrErrResponse]:
    """get a specific install group run

     Returns a single install group run with full details

    Args:
        app_id (str):
        app_branch_id (str):
        run_id (str):
        install_group_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppInstallGroupRun | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        app_branch_id=app_branch_id,
        run_id=run_id,
        install_group_run_id=install_group_run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    app_branch_id: str,
    run_id: str,
    install_group_run_id: str,
    *,
    client: AuthenticatedClient,
) -> AppInstallGroupRun | StderrErrResponse | None:
    """get a specific install group run

     Returns a single install group run with full details

    Args:
        app_id (str):
        app_branch_id (str):
        run_id (str):
        install_group_run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppInstallGroupRun | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            app_branch_id=app_branch_id,
            run_id=run_id,
            install_group_run_id=install_group_run_id,
            client=client,
        )
    ).parsed
