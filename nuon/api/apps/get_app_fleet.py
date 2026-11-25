from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_app_fleet_response import ServiceAppFleetResponse
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    q: str | Unset = UNSET,
    labels: str | Unset = UNSET,
    health: str | Unset = UNSET,
    runner_status: str | Unset = UNSET,
    rollout: str | Unset = UNSET,
    component_id: str | Unset = UNSET,
    app_branch_id: str | Unset = UNSET,
    app_branch_group: str | Unset = UNSET,
    per_group: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["labels"] = labels

    params["health"] = health

    params["runner_status"] = runner_status

    params["rollout"] = rollout

    params["component_id"] = component_id

    params["app_branch_id"] = app_branch_id

    params["app_branch_group"] = app_branch_group

    params["per_group"] = per_group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/apps/{app_id}/fleet".format(
            app_id=quote(str(app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ServiceAppFleetResponse | StderrErrResponse | None:
    if response.status_code == 200:
        response_200 = ServiceAppFleetResponse.from_dict(response.json())

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
) -> Response[ServiceAppFleetResponse | StderrErrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    labels: str | Unset = UNSET,
    health: str | Unset = UNSET,
    runner_status: str | Unset = UNSET,
    rollout: str | Unset = UNSET,
    component_id: str | Unset = UNSET,
    app_branch_id: str | Unset = UNSET,
    app_branch_group: str | Unset = UNSET,
    per_group: int | Unset = 10,
) -> Response[ServiceAppFleetResponse | StderrErrResponse]:
    """app fleet summary, branches, and install groups

     Returns the app's installs grouped by app branch and install group, with counts per lane and the
    first installs of each group. Filters apply to counts and to the returned installs. Rollout compares
    each install's applied app config against the target run of its branch.

    Args:
        app_id (str):
        q (str | Unset):
        labels (str | Unset):
        health (str | Unset):
        runner_status (str | Unset):
        rollout (str | Unset):
        component_id (str | Unset):
        app_branch_id (str | Unset):
        app_branch_group (str | Unset):
        per_group (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceAppFleetResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        q=q,
        labels=labels,
        health=health,
        runner_status=runner_status,
        rollout=rollout,
        component_id=component_id,
        app_branch_id=app_branch_id,
        app_branch_group=app_branch_group,
        per_group=per_group,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    labels: str | Unset = UNSET,
    health: str | Unset = UNSET,
    runner_status: str | Unset = UNSET,
    rollout: str | Unset = UNSET,
    component_id: str | Unset = UNSET,
    app_branch_id: str | Unset = UNSET,
    app_branch_group: str | Unset = UNSET,
    per_group: int | Unset = 10,
) -> ServiceAppFleetResponse | StderrErrResponse | None:
    """app fleet summary, branches, and install groups

     Returns the app's installs grouped by app branch and install group, with counts per lane and the
    first installs of each group. Filters apply to counts and to the returned installs. Rollout compares
    each install's applied app config against the target run of its branch.

    Args:
        app_id (str):
        q (str | Unset):
        labels (str | Unset):
        health (str | Unset):
        runner_status (str | Unset):
        rollout (str | Unset):
        component_id (str | Unset):
        app_branch_id (str | Unset):
        app_branch_group (str | Unset):
        per_group (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceAppFleetResponse | StderrErrResponse
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        q=q,
        labels=labels,
        health=health,
        runner_status=runner_status,
        rollout=rollout,
        component_id=component_id,
        app_branch_id=app_branch_id,
        app_branch_group=app_branch_group,
        per_group=per_group,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    labels: str | Unset = UNSET,
    health: str | Unset = UNSET,
    runner_status: str | Unset = UNSET,
    rollout: str | Unset = UNSET,
    component_id: str | Unset = UNSET,
    app_branch_id: str | Unset = UNSET,
    app_branch_group: str | Unset = UNSET,
    per_group: int | Unset = 10,
) -> Response[ServiceAppFleetResponse | StderrErrResponse]:
    """app fleet summary, branches, and install groups

     Returns the app's installs grouped by app branch and install group, with counts per lane and the
    first installs of each group. Filters apply to counts and to the returned installs. Rollout compares
    each install's applied app config against the target run of its branch.

    Args:
        app_id (str):
        q (str | Unset):
        labels (str | Unset):
        health (str | Unset):
        runner_status (str | Unset):
        rollout (str | Unset):
        component_id (str | Unset):
        app_branch_id (str | Unset):
        app_branch_group (str | Unset):
        per_group (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceAppFleetResponse | StderrErrResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        q=q,
        labels=labels,
        health=health,
        runner_status=runner_status,
        rollout=rollout,
        component_id=component_id,
        app_branch_id=app_branch_id,
        app_branch_group=app_branch_group,
        per_group=per_group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    labels: str | Unset = UNSET,
    health: str | Unset = UNSET,
    runner_status: str | Unset = UNSET,
    rollout: str | Unset = UNSET,
    component_id: str | Unset = UNSET,
    app_branch_id: str | Unset = UNSET,
    app_branch_group: str | Unset = UNSET,
    per_group: int | Unset = 10,
) -> ServiceAppFleetResponse | StderrErrResponse | None:
    """app fleet summary, branches, and install groups

     Returns the app's installs grouped by app branch and install group, with counts per lane and the
    first installs of each group. Filters apply to counts and to the returned installs. Rollout compares
    each install's applied app config against the target run of its branch.

    Args:
        app_id (str):
        q (str | Unset):
        labels (str | Unset):
        health (str | Unset):
        runner_status (str | Unset):
        rollout (str | Unset):
        component_id (str | Unset):
        app_branch_id (str | Unset):
        app_branch_group (str | Unset):
        per_group (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceAppFleetResponse | StderrErrResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            q=q,
            labels=labels,
            health=health,
            runner_status=runner_status,
            rollout=rollout,
            component_id=component_id,
            app_branch_id=app_branch_id,
            app_branch_group=app_branch_group,
            per_group=per_group,
        )
    ).parsed
