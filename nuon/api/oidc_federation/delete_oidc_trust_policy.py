from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    policy_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/oidc/trust-policies/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | StderrErrResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 403:
        response_403 = StderrErrResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StderrErrResponse.from_dict(response.json())

        return response_404

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
    policy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | StderrErrResponse]:
    """delete an OIDC trust policy

     Deletes an OIDC workload identity trust policy belonging to your current org, along with its
    dedicated service account. Tokens already issued under the policy stop working immediately.

    Args:
        policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    policy_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | StderrErrResponse | None:
    """delete an OIDC trust policy

     Deletes an OIDC workload identity trust policy belonging to your current org, along with its
    dedicated service account. Tokens already issued under the policy stop working immediately.

    Args:
        policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    policy_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | StderrErrResponse]:
    """delete an OIDC trust policy

     Deletes an OIDC workload identity trust policy belonging to your current org, along with its
    dedicated service account. Tokens already issued under the policy stop working immediately.

    Args:
        policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | StderrErrResponse | None:
    """delete an OIDC trust policy

     Deletes an OIDC workload identity trust policy belonging to your current org, along with its
    dedicated service account. Tokens already issued under the policy stop working immediately.

    Args:
        policy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
        )
    ).parsed
