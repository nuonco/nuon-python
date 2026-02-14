from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_create_ad_hoc_action_request import ServiceCreateAdHocActionRequest
from ...models.service_create_ad_hoc_action_response import ServiceCreateAdHocActionResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    *,
    body: ServiceCreateAdHocActionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/installs/{install_id}/actions/adhoc-run".format(
            install_id=quote(str(install_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ServiceCreateAdHocActionResponse | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = ServiceCreateAdHocActionResponse.from_dict(response.json())

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
) -> Response[ServiceCreateAdHocActionResponse | StderrErrResponse]:
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
    body: ServiceCreateAdHocActionRequest,
) -> Response[ServiceCreateAdHocActionResponse | StderrErrResponse]:
    r""" create an adhoc action run for an install

     # Create AdHoc Action

    Creates and executes a one-time action on an install without creating a permanent action workflow
    definition.

    ## Use Cases

    - Running ad-hoc debugging scripts
    - Executing maintenance commands
    - Testing bash snippets before creating permanent actions
    - Quick data exports or transformations

    ## Request Body

    Provide **either** `inline_contents` (for multi-line bash scripts) **or** `command` (for single-line
    commands), but not both.

    ### Fields

    - `inline_contents` (string, optional): Multi-line bash script to execute
    - `command` (string, optional): Single-line shell command to execute
    - `env_vars` (object, optional): Environment variables as key-value pairs
    - `timeout` (integer, optional): Execution timeout in seconds (1-3600, default: 300)
    - `name` (string, optional): Display name for the action (max 255 chars)

    ## Response

    Returns the created adhoc action run with status information.

    ## Example

    ```bash
    curl -X POST https://api.nuon.co/v1/installs/{install_id}/actions/adhoc \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Nuon-Org-ID: $ORG_ID\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inline_contents\": \"#!/bin/bash\necho \\"Hello from adhoc action\\"\nenv | grep NUON\",
        \"env_vars\": {
          \"DEBUG\": \"true\",
          \"LOG_LEVEL\": \"info\"
        },
        \"timeout\": 300,
        \"name\": \"Debug Script\"
      }'
    ```

    ## Notes

    - AdHoc actions are marked with `trigger_type: \"adhoc\"`
    - They appear in action run history and can be filtered via trigger_type
    - Execution happens on the install's runner using the same infrastructure as permanent actions
    - Logs are preserved and can be viewed via the action runs API
    - AdHoc runs are kept indefinitely (same retention as regular action runs)

    Args:
        install_id (str):
        body (ServiceCreateAdHocActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCreateAdHocActionResponse | StderrErrResponse]
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
    body: ServiceCreateAdHocActionRequest,
) -> ServiceCreateAdHocActionResponse | StderrErrResponse | None:
    r""" create an adhoc action run for an install

     # Create AdHoc Action

    Creates and executes a one-time action on an install without creating a permanent action workflow
    definition.

    ## Use Cases

    - Running ad-hoc debugging scripts
    - Executing maintenance commands
    - Testing bash snippets before creating permanent actions
    - Quick data exports or transformations

    ## Request Body

    Provide **either** `inline_contents` (for multi-line bash scripts) **or** `command` (for single-line
    commands), but not both.

    ### Fields

    - `inline_contents` (string, optional): Multi-line bash script to execute
    - `command` (string, optional): Single-line shell command to execute
    - `env_vars` (object, optional): Environment variables as key-value pairs
    - `timeout` (integer, optional): Execution timeout in seconds (1-3600, default: 300)
    - `name` (string, optional): Display name for the action (max 255 chars)

    ## Response

    Returns the created adhoc action run with status information.

    ## Example

    ```bash
    curl -X POST https://api.nuon.co/v1/installs/{install_id}/actions/adhoc \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Nuon-Org-ID: $ORG_ID\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inline_contents\": \"#!/bin/bash\necho \\"Hello from adhoc action\\"\nenv | grep NUON\",
        \"env_vars\": {
          \"DEBUG\": \"true\",
          \"LOG_LEVEL\": \"info\"
        },
        \"timeout\": 300,
        \"name\": \"Debug Script\"
      }'
    ```

    ## Notes

    - AdHoc actions are marked with `trigger_type: \"adhoc\"`
    - They appear in action run history and can be filtered via trigger_type
    - Execution happens on the install's runner using the same infrastructure as permanent actions
    - Logs are preserved and can be viewed via the action runs API
    - AdHoc runs are kept indefinitely (same retention as regular action runs)

    Args:
        install_id (str):
        body (ServiceCreateAdHocActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCreateAdHocActionResponse | StderrErrResponse
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
    body: ServiceCreateAdHocActionRequest,
) -> Response[ServiceCreateAdHocActionResponse | StderrErrResponse]:
    r""" create an adhoc action run for an install

     # Create AdHoc Action

    Creates and executes a one-time action on an install without creating a permanent action workflow
    definition.

    ## Use Cases

    - Running ad-hoc debugging scripts
    - Executing maintenance commands
    - Testing bash snippets before creating permanent actions
    - Quick data exports or transformations

    ## Request Body

    Provide **either** `inline_contents` (for multi-line bash scripts) **or** `command` (for single-line
    commands), but not both.

    ### Fields

    - `inline_contents` (string, optional): Multi-line bash script to execute
    - `command` (string, optional): Single-line shell command to execute
    - `env_vars` (object, optional): Environment variables as key-value pairs
    - `timeout` (integer, optional): Execution timeout in seconds (1-3600, default: 300)
    - `name` (string, optional): Display name for the action (max 255 chars)

    ## Response

    Returns the created adhoc action run with status information.

    ## Example

    ```bash
    curl -X POST https://api.nuon.co/v1/installs/{install_id}/actions/adhoc \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Nuon-Org-ID: $ORG_ID\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inline_contents\": \"#!/bin/bash\necho \\"Hello from adhoc action\\"\nenv | grep NUON\",
        \"env_vars\": {
          \"DEBUG\": \"true\",
          \"LOG_LEVEL\": \"info\"
        },
        \"timeout\": 300,
        \"name\": \"Debug Script\"
      }'
    ```

    ## Notes

    - AdHoc actions are marked with `trigger_type: \"adhoc\"`
    - They appear in action run history and can be filtered via trigger_type
    - Execution happens on the install's runner using the same infrastructure as permanent actions
    - Logs are preserved and can be viewed via the action runs API
    - AdHoc runs are kept indefinitely (same retention as regular action runs)

    Args:
        install_id (str):
        body (ServiceCreateAdHocActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCreateAdHocActionResponse | StderrErrResponse]
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
    body: ServiceCreateAdHocActionRequest,
) -> ServiceCreateAdHocActionResponse | StderrErrResponse | None:
    r""" create an adhoc action run for an install

     # Create AdHoc Action

    Creates and executes a one-time action on an install without creating a permanent action workflow
    definition.

    ## Use Cases

    - Running ad-hoc debugging scripts
    - Executing maintenance commands
    - Testing bash snippets before creating permanent actions
    - Quick data exports or transformations

    ## Request Body

    Provide **either** `inline_contents` (for multi-line bash scripts) **or** `command` (for single-line
    commands), but not both.

    ### Fields

    - `inline_contents` (string, optional): Multi-line bash script to execute
    - `command` (string, optional): Single-line shell command to execute
    - `env_vars` (object, optional): Environment variables as key-value pairs
    - `timeout` (integer, optional): Execution timeout in seconds (1-3600, default: 300)
    - `name` (string, optional): Display name for the action (max 255 chars)

    ## Response

    Returns the created adhoc action run with status information.

    ## Example

    ```bash
    curl -X POST https://api.nuon.co/v1/installs/{install_id}/actions/adhoc \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Nuon-Org-ID: $ORG_ID\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inline_contents\": \"#!/bin/bash\necho \\"Hello from adhoc action\\"\nenv | grep NUON\",
        \"env_vars\": {
          \"DEBUG\": \"true\",
          \"LOG_LEVEL\": \"info\"
        },
        \"timeout\": 300,
        \"name\": \"Debug Script\"
      }'
    ```

    ## Notes

    - AdHoc actions are marked with `trigger_type: \"adhoc\"`
    - They appear in action run history and can be filtered via trigger_type
    - Execution happens on the install's runner using the same infrastructure as permanent actions
    - Logs are preserved and can be viewed via the action runs API
    - AdHoc runs are kept indefinitely (same retention as regular action runs)

    Args:
        install_id (str):
        body (ServiceCreateAdHocActionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCreateAdHocActionResponse | StderrErrResponse
     """

    return (
        await asyncio_detailed(
            install_id=install_id,
            client=client,
            body=body,
        )
    ).parsed
