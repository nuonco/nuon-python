from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_terraform_workspace_states_json_by_idv2_response_200 import (
    GetTerraformWorkspaceStatesJSONByIDV2Response200,
)
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    state_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/terraform-workspaces/{workspace_id}/state-json/{state_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            state_id=quote(str(state_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = GetTerraformWorkspaceStatesJSONByIDV2Response200.from_dict(response.json())

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
) -> Response[GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse]:
    r"""get terraform state json by id. This output is same as \"terraform show --json\"

     Return a terraform state in JSON format by id.

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        state_id=state_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse | None:
    r"""get terraform state json by id. This output is same as \"terraform show --json\"

     Return a terraform state in JSON format by id.

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        state_id=state_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse]:
    r"""get terraform state json by id. This output is same as \"terraform show --json\"

     Return a terraform state in JSON format by id.

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        state_id=state_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    state_id: str,
    *,
    client: AuthenticatedClient,
) -> GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse | None:
    r"""get terraform state json by id. This output is same as \"terraform show --json\"

     Return a terraform state in JSON format by id.

    Args:
        workspace_id (str):
        state_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTerraformWorkspaceStatesJSONByIDV2Response200 | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            state_id=state_id,
            client=client,
        )
    ).parsed
