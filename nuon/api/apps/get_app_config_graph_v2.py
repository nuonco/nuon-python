from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    app_id: str,
    config_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/configs/{config_id}/graph".format(
            app_id=quote(str(app_id), safe=""),
            config_id=quote(str(config_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[StderrErrResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StderrErrResponse | str]:
    """get an app config graph

     Return raw graphviz data as a string that can be used to visualize a graph for an app.

    Note, for more complex viewing recommend to copy this output directly into [Graphviz
    viewer](https://dreampuf.github.io/GraphvizOnline).

    Args:
        app_id (str):
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | str]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        config_id=config_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | str | None:
    """get an app config graph

     Return raw graphviz data as a string that can be used to visualize a graph for an app.

    Note, for more complex viewing recommend to copy this output directly into [Graphviz
    viewer](https://dreampuf.github.io/GraphvizOnline).

    Args:
        app_id (str):
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | str
    """

    return sync_detailed(
        app_id=app_id,
        config_id=config_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[StderrErrResponse | str]:
    """get an app config graph

     Return raw graphviz data as a string that can be used to visualize a graph for an app.

    Note, for more complex viewing recommend to copy this output directly into [Graphviz
    viewer](https://dreampuf.github.io/GraphvizOnline).

    Args:
        app_id (str):
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | str]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        config_id=config_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> StderrErrResponse | str | None:
    """get an app config graph

     Return raw graphviz data as a string that can be used to visualize a graph for an app.

    Note, for more complex viewing recommend to copy this output directly into [Graphviz
    viewer](https://dreampuf.github.io/GraphvizOnline).

    Args:
        app_id (str):
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | str
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            config_id=config_id,
            client=client,
        )
    ).parsed
