from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_log_stream import AppLogStream
from ...models.stderr_err_response import StderrErrResponse
from ...types import Response


def _get_kwargs(
    install_id: str,
    run_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/installs/{install_id}/actions/runs/{run_id}/logs".format(
            install_id=quote(str(install_id), safe=""),
            run_id=quote(str(run_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AppLogStream | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = AppLogStream.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AppLogStream | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppLogStream | StderrErrResponse]:
    """delete the logs and trace spans of an action run

     Permanently delete the logs and trace spans of a finished action run, for example after a command
    printed a secret.

    Only org admins can delete logs, and only after the run has ended, including runs that failed, timed
    out, or were
    cancelled. The run itself and its outputs are kept. The
    log stream is marked with `logs_deleted_at` and `logs_deleted_by_id` from the first deletion.
    Calling this again
    deletes any records that arrived late and keeps the original marker.

    Once the logs are deleted, the log stream's write token is revoked, new writes to the stream are
    dropped, and reads of
    the stream return no logs or spans. Trace spans are removed in the background after the call
    returns.

    Rotate any secret that was exposed: deleting the logs does not undo the exposure, and copies held in
    the ingestion
    queue expire on their own retention schedule. If that queue is replayed before then, call this
    endpoint again.

    Args:
        install_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppLogStream | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        run_id=run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> AppLogStream | StderrErrResponse | None:
    """delete the logs and trace spans of an action run

     Permanently delete the logs and trace spans of a finished action run, for example after a command
    printed a secret.

    Only org admins can delete logs, and only after the run has ended, including runs that failed, timed
    out, or were
    cancelled. The run itself and its outputs are kept. The
    log stream is marked with `logs_deleted_at` and `logs_deleted_by_id` from the first deletion.
    Calling this again
    deletes any records that arrived late and keeps the original marker.

    Once the logs are deleted, the log stream's write token is revoked, new writes to the stream are
    dropped, and reads of
    the stream return no logs or spans. Trace spans are removed in the background after the call
    returns.

    Rotate any secret that was exposed: deleting the logs does not undo the exposure, and copies held in
    the ingestion
    queue expire on their own retention schedule. If that queue is replayed before then, call this
    endpoint again.

    Args:
        install_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppLogStream | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppLogStream | StderrErrResponse]:
    """delete the logs and trace spans of an action run

     Permanently delete the logs and trace spans of a finished action run, for example after a command
    printed a secret.

    Only org admins can delete logs, and only after the run has ended, including runs that failed, timed
    out, or were
    cancelled. The run itself and its outputs are kept. The
    log stream is marked with `logs_deleted_at` and `logs_deleted_by_id` from the first deletion.
    Calling this again
    deletes any records that arrived late and keeps the original marker.

    Once the logs are deleted, the log stream's write token is revoked, new writes to the stream are
    dropped, and reads of
    the stream return no logs or spans. Trace spans are removed in the background after the call
    returns.

    Rotate any secret that was exposed: deleting the logs does not undo the exposure, and copies held in
    the ingestion
    queue expire on their own retention schedule. If that queue is replayed before then, call this
    endpoint again.

    Args:
        install_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppLogStream | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        run_id=run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
) -> AppLogStream | StderrErrResponse | None:
    """delete the logs and trace spans of an action run

     Permanently delete the logs and trace spans of a finished action run, for example after a command
    printed a secret.

    Only org admins can delete logs, and only after the run has ended, including runs that failed, timed
    out, or were
    cancelled. The run itself and its outputs are kept. The
    log stream is marked with `logs_deleted_at` and `logs_deleted_by_id` from the first deletion.
    Calling this again
    deletes any records that arrived late and keeps the original marker.

    Once the logs are deleted, the log stream's write token is revoked, new writes to the stream are
    dropped, and reads of
    the stream return no logs or spans. Trace spans are removed in the background after the call
    returns.

    Rotate any secret that was exposed: deleting the logs does not undo the exposure, and copies held in
    the ingestion
    queue expire on their own retention schedule. If that queue is replayed before then, call this
    endpoint again.

    Args:
        install_id (str):
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppLogStream | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            run_id=run_id,
            client=client,
        )
    ).parsed
