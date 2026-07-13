from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    type_: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/general/config-schema/{type_}".format(
            type_=quote(str(type_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | StderrErrResponse]:
    r"""Get jsonschema for a config file type

     Return jsonschemas for Nuon configs. These can be used in frontmatter in most editors that have a
    TOML LSP (such as
    [Taplo](https://taplo.tamasfe.dev/) configured.

    ```toml
    #:schema https://api.nuon.co/v1/general/config-schema?source=inputs

    description = \"description\"
    ```

    You can pass in a valid source argument to render within a specific config file:

    - input
    - input-group
    - installer
    - sandbox
    - runner
    - docker_build
    - container_image
    - helm
    - terraform
    - runbook
    - job

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | StderrErrResponse | None:
    r"""Get jsonschema for a config file type

     Return jsonschemas for Nuon configs. These can be used in frontmatter in most editors that have a
    TOML LSP (such as
    [Taplo](https://taplo.tamasfe.dev/) configured.

    ```toml
    #:schema https://api.nuon.co/v1/general/config-schema?source=inputs

    description = \"description\"
    ```

    You can pass in a valid source argument to render within a specific config file:

    - input
    - input-group
    - installer
    - sandbox
    - runner
    - docker_build
    - container_image
    - helm
    - terraform
    - runbook
    - job

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return sync_detailed(
        type_=type_,
        client=client,
    ).parsed


async def asyncio_detailed(
    type_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | StderrErrResponse]:
    r"""Get jsonschema for a config file type

     Return jsonschemas for Nuon configs. These can be used in frontmatter in most editors that have a
    TOML LSP (such as
    [Taplo](https://taplo.tamasfe.dev/) configured.

    ```toml
    #:schema https://api.nuon.co/v1/general/config-schema?source=inputs

    description = \"description\"
    ```

    You can pass in a valid source argument to render within a specific config file:

    - input
    - input-group
    - installer
    - sandbox
    - runner
    - docker_build
    - container_image
    - helm
    - terraform
    - runbook
    - job

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | StderrErrResponse | None:
    r"""Get jsonschema for a config file type

     Return jsonschemas for Nuon configs. These can be used in frontmatter in most editors that have a
    TOML LSP (such as
    [Taplo](https://taplo.tamasfe.dev/) configured.

    ```toml
    #:schema https://api.nuon.co/v1/general/config-schema?source=inputs

    description = \"description\"
    ```

    You can pass in a valid source argument to render within a specific config file:

    - input
    - input-group
    - installer
    - sandbox
    - runner
    - docker_build
    - container_image
    - helm
    - terraform
    - runbook
    - job

    Args:
        type_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
        )
    ).parsed
