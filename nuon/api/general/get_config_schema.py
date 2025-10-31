from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_config_schema_response_200 import GetConfigSchemaResponse200
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/general/config-schema",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetConfigSchemaResponse200 | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = GetConfigSchemaResponse200.from_dict(response.json())

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
) -> Response[GetConfigSchemaResponse200 | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
) -> Response[GetConfigSchemaResponse200 | StderrErrResponse]:
    r"""Get jsonschema for config file

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
    - job

    Args:
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConfigSchemaResponse200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
) -> GetConfigSchemaResponse200 | StderrErrResponse | None:
    r"""Get jsonschema for config file

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
    - job

    Args:
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConfigSchemaResponse200 | StderrErrResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
) -> Response[GetConfigSchemaResponse200 | StderrErrResponse]:
    r"""Get jsonschema for config file

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
    - job

    Args:
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConfigSchemaResponse200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
) -> GetConfigSchemaResponse200 | StderrErrResponse | None:
    r"""Get jsonschema for config file

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
    - job

    Args:
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConfigSchemaResponse200 | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
        )
    ).parsed
