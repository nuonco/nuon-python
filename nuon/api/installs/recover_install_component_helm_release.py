from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_workflow_response import AppWorkflowResponse
from ...models.service_recover_install_component_helm_release_request import (
    ServiceRecoverInstallComponentHelmReleaseRequest,
)
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    install_id: str,
    component_id: str,
    *,
    body: ServiceRecoverInstallComponentHelmReleaseRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/installs/{install_id}/components/{component_id}/recover-helm-release".format(
            install_id=quote(str(install_id), safe=""),
            component_id=quote(str(component_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppWorkflowResponse | StderrErrResponse | None:
    if response.status_code == 201:
        response_201 = AppWorkflowResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = StderrErrResponse.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = StderrErrResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppWorkflowResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRecoverInstallComponentHelmReleaseRequest | Unset = UNSET,
) -> Response[AppWorkflowResponse | StderrErrResponse]:
    """recover a stuck helm release for an install component

     Recover a Helm release that was left part-way through an operation.

    Helm records a `pending-install`, `pending-upgrade` or `pending-rollback` status before it
    starts changing the cluster and clears it once the operation finishes. A release left in one
    of those statuses is a rollout whose runner went away — a crash, a cancelled workflow, or a
    job that timed out. Helm then refuses every further operation on that release, and retrying
    the deploy cannot clear it.

    This endpoint starts a workflow that returns the release to a usable state:

    - when an earlier revision finished a rollout, the release is rolled back to it
    - when no revision ever rolled out, the stuck release is removed

    It deploys nothing and changes no desired state. Deploy the component afterwards to roll out
    the version you want.

    The recovery refuses to act on a release that is not pending, so it is safe to run when you
    are unsure and it is a no-op on a second run.

    Returns `409` when a job is already running for the component (recovering while Helm is
    genuinely mid-operation can corrupt the release) or when the component has never been
    deployed on this install. Returns `400` when the component is not a Helm chart.

    Args:
        install_id (str):
        component_id (str):
        body (ServiceRecoverInstallComponentHelmReleaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppWorkflowResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRecoverInstallComponentHelmReleaseRequest | Unset = UNSET,
) -> AppWorkflowResponse | StderrErrResponse | None:
    """recover a stuck helm release for an install component

     Recover a Helm release that was left part-way through an operation.

    Helm records a `pending-install`, `pending-upgrade` or `pending-rollback` status before it
    starts changing the cluster and clears it once the operation finishes. A release left in one
    of those statuses is a rollout whose runner went away — a crash, a cancelled workflow, or a
    job that timed out. Helm then refuses every further operation on that release, and retrying
    the deploy cannot clear it.

    This endpoint starts a workflow that returns the release to a usable state:

    - when an earlier revision finished a rollout, the release is rolled back to it
    - when no revision ever rolled out, the stuck release is removed

    It deploys nothing and changes no desired state. Deploy the component afterwards to roll out
    the version you want.

    The recovery refuses to act on a release that is not pending, so it is safe to run when you
    are unsure and it is a no-op on a second run.

    Returns `409` when a job is already running for the component (recovering while Helm is
    genuinely mid-operation can corrupt the release) or when the component has never been
    deployed on this install. Returns `400` when the component is not a Helm chart.

    Args:
        install_id (str):
        component_id (str):
        body (ServiceRecoverInstallComponentHelmReleaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppWorkflowResponse | StderrErrResponse
    """

    return sync_detailed(
        install_id=install_id,
        component_id=component_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRecoverInstallComponentHelmReleaseRequest | Unset = UNSET,
) -> Response[AppWorkflowResponse | StderrErrResponse]:
    """recover a stuck helm release for an install component

     Recover a Helm release that was left part-way through an operation.

    Helm records a `pending-install`, `pending-upgrade` or `pending-rollback` status before it
    starts changing the cluster and clears it once the operation finishes. A release left in one
    of those statuses is a rollout whose runner went away — a crash, a cancelled workflow, or a
    job that timed out. Helm then refuses every further operation on that release, and retrying
    the deploy cannot clear it.

    This endpoint starts a workflow that returns the release to a usable state:

    - when an earlier revision finished a rollout, the release is rolled back to it
    - when no revision ever rolled out, the stuck release is removed

    It deploys nothing and changes no desired state. Deploy the component afterwards to roll out
    the version you want.

    The recovery refuses to act on a release that is not pending, so it is safe to run when you
    are unsure and it is a no-op on a second run.

    Returns `409` when a job is already running for the component (recovering while Helm is
    genuinely mid-operation can corrupt the release) or when the component has never been
    deployed on this install. Returns `400` when the component is not a Helm chart.

    Args:
        install_id (str):
        component_id (str):
        body (ServiceRecoverInstallComponentHelmReleaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppWorkflowResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        install_id=install_id,
        component_id=component_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    install_id: str,
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: ServiceRecoverInstallComponentHelmReleaseRequest | Unset = UNSET,
) -> AppWorkflowResponse | StderrErrResponse | None:
    """recover a stuck helm release for an install component

     Recover a Helm release that was left part-way through an operation.

    Helm records a `pending-install`, `pending-upgrade` or `pending-rollback` status before it
    starts changing the cluster and clears it once the operation finishes. A release left in one
    of those statuses is a rollout whose runner went away — a crash, a cancelled workflow, or a
    job that timed out. Helm then refuses every further operation on that release, and retrying
    the deploy cannot clear it.

    This endpoint starts a workflow that returns the release to a usable state:

    - when an earlier revision finished a rollout, the release is rolled back to it
    - when no revision ever rolled out, the stuck release is removed

    It deploys nothing and changes no desired state. Deploy the component afterwards to roll out
    the version you want.

    The recovery refuses to act on a release that is not pending, so it is safe to run when you
    are unsure and it is a no-op on a second run.

    Returns `409` when a job is already running for the component (recovering while Helm is
    genuinely mid-operation can corrupt the release) or when the component has never been
    deployed on this install. Returns `400` when the component is not a Helm chart.

    Args:
        install_id (str):
        component_id (str):
        body (ServiceRecoverInstallComponentHelmReleaseRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppWorkflowResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            install_id=install_id,
            component_id=component_id,
            client=client,
            body=body,
        )
    ).parsed
