from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_otel_log_record import AppOtelLogRecord
from ...models.stderr_err_response import StderrErrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    log_stream_id: str,
    *,
    order: str | Unset = "asc",
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    service_name: list[str] | Unset = UNSET,
    scope_name: list[str] | Unset = UNSET,
    scope_version: list[str] | Unset = UNSET,
    resource_schema_url: list[str] | Unset = UNSET,
    scope_schema_url: list[str] | Unset = UNSET,
    severity_text: list[str] | Unset = UNSET,
    severity_number_min: int | Unset = UNSET,
    severity_number_max: int | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    trace_flags: int | Unset = UNSET,
    runner_id: str | Unset = UNSET,
    runner_job_id: str | Unset = UNSET,
    runner_group_id: str | Unset = UNSET,
    runner_job_execution_id: str | Unset = UNSET,
    runner_job_execution_step: str | Unset = UNSET,
    tool: list[str] | Unset = UNSET,
    helm_release_name: str | Unset = UNSET,
    helm_chart_name: str | Unset = UNSET,
    helm_chart_id: str | Unset = UNSET,
    helm_namespace: str | Unset = UNSET,
    helm_operation: str | Unset = UNSET,
    tf_workspace_id: str | Unset = UNSET,
    tf_operation: str | Unset = UNSET,
    k8s_kind: str | Unset = UNSET,
    k8s_namespace: str | Unset = UNSET,
    k8s_name: str | Unset = UNSET,
    k8s_operation: str | Unset = UNSET,
    attr: list[str] | Unset = UNSET,
    resource_attr: list[str] | Unset = UNSET,
    scope_attr: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    x_nuon_api_offset: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_nuon_api_offset, Unset):
        headers["X-Nuon-API-Offset"] = x_nuon_api_offset

    params: dict[str, Any] = {}

    params["order"] = order

    params["start_time"] = start_time

    params["end_time"] = end_time

    json_service_name: list[str] | Unset = UNSET
    if not isinstance(service_name, Unset):
        json_service_name = service_name

    params["service_name"] = json_service_name

    json_scope_name: list[str] | Unset = UNSET
    if not isinstance(scope_name, Unset):
        json_scope_name = scope_name

    params["scope_name"] = json_scope_name

    json_scope_version: list[str] | Unset = UNSET
    if not isinstance(scope_version, Unset):
        json_scope_version = scope_version

    params["scope_version"] = json_scope_version

    json_resource_schema_url: list[str] | Unset = UNSET
    if not isinstance(resource_schema_url, Unset):
        json_resource_schema_url = resource_schema_url

    params["resource_schema_url"] = json_resource_schema_url

    json_scope_schema_url: list[str] | Unset = UNSET
    if not isinstance(scope_schema_url, Unset):
        json_scope_schema_url = scope_schema_url

    params["scope_schema_url"] = json_scope_schema_url

    json_severity_text: list[str] | Unset = UNSET
    if not isinstance(severity_text, Unset):
        json_severity_text = severity_text

    params["severity_text"] = json_severity_text

    params["severity_number_min"] = severity_number_min

    params["severity_number_max"] = severity_number_max

    params["trace_id"] = trace_id

    params["span_id"] = span_id

    params["trace_flags"] = trace_flags

    params["runner_id"] = runner_id

    params["runner_job_id"] = runner_job_id

    params["runner_group_id"] = runner_group_id

    params["runner_job_execution_id"] = runner_job_execution_id

    params["runner_job_execution_step"] = runner_job_execution_step

    json_tool: list[str] | Unset = UNSET
    if not isinstance(tool, Unset):
        json_tool = tool

    params["tool"] = json_tool

    params["helm_release_name"] = helm_release_name

    params["helm_chart_name"] = helm_chart_name

    params["helm_chart_id"] = helm_chart_id

    params["helm_namespace"] = helm_namespace

    params["helm_operation"] = helm_operation

    params["tf_workspace_id"] = tf_workspace_id

    params["tf_operation"] = tf_operation

    params["k8s_kind"] = k8s_kind

    params["k8s_namespace"] = k8s_namespace

    params["k8s_name"] = k8s_name

    params["k8s_operation"] = k8s_operation

    json_attr: list[str] | Unset = UNSET
    if not isinstance(attr, Unset):
        json_attr = attr

    params["attr"] = json_attr

    json_resource_attr: list[str] | Unset = UNSET
    if not isinstance(resource_attr, Unset):
        json_resource_attr = resource_attr

    params["resource_attr"] = json_resource_attr

    json_scope_attr: list[str] | Unset = UNSET
    if not isinstance(scope_attr, Unset):
        json_scope_attr = scope_attr

    params["scope_attr"] = json_scope_attr

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/log-streams/{log_stream_id}/logs".format(
            log_stream_id=quote(str(log_stream_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> StderrErrResponse | list[AppOtelLogRecord] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppOtelLogRecord.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[StderrErrResponse | list[AppOtelLogRecord]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    order: str | Unset = "asc",
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    service_name: list[str] | Unset = UNSET,
    scope_name: list[str] | Unset = UNSET,
    scope_version: list[str] | Unset = UNSET,
    resource_schema_url: list[str] | Unset = UNSET,
    scope_schema_url: list[str] | Unset = UNSET,
    severity_text: list[str] | Unset = UNSET,
    severity_number_min: int | Unset = UNSET,
    severity_number_max: int | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    trace_flags: int | Unset = UNSET,
    runner_id: str | Unset = UNSET,
    runner_job_id: str | Unset = UNSET,
    runner_group_id: str | Unset = UNSET,
    runner_job_execution_id: str | Unset = UNSET,
    runner_job_execution_step: str | Unset = UNSET,
    tool: list[str] | Unset = UNSET,
    helm_release_name: str | Unset = UNSET,
    helm_chart_name: str | Unset = UNSET,
    helm_chart_id: str | Unset = UNSET,
    helm_namespace: str | Unset = UNSET,
    helm_operation: str | Unset = UNSET,
    tf_workspace_id: str | Unset = UNSET,
    tf_operation: str | Unset = UNSET,
    k8s_kind: str | Unset = UNSET,
    k8s_namespace: str | Unset = UNSET,
    k8s_name: str | Unset = UNSET,
    k8s_operation: str | Unset = UNSET,
    attr: list[str] | Unset = UNSET,
    resource_attr: list[str] | Unset = UNSET,
    scope_attr: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    x_nuon_api_offset: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppOtelLogRecord]]:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        order (str | Unset):  Default: 'asc'.
        start_time (str | Unset):
        end_time (str | Unset):
        service_name (list[str] | Unset):
        scope_name (list[str] | Unset):
        scope_version (list[str] | Unset):
        resource_schema_url (list[str] | Unset):
        scope_schema_url (list[str] | Unset):
        severity_text (list[str] | Unset):
        severity_number_min (int | Unset):
        severity_number_max (int | Unset):
        trace_id (str | Unset):
        span_id (str | Unset):
        trace_flags (int | Unset):
        runner_id (str | Unset):
        runner_job_id (str | Unset):
        runner_group_id (str | Unset):
        runner_job_execution_id (str | Unset):
        runner_job_execution_step (str | Unset):
        tool (list[str] | Unset):
        helm_release_name (str | Unset):
        helm_chart_name (str | Unset):
        helm_chart_id (str | Unset):
        helm_namespace (str | Unset):
        helm_operation (str | Unset):
        tf_workspace_id (str | Unset):
        tf_operation (str | Unset):
        k8s_kind (str | Unset):
        k8s_namespace (str | Unset):
        k8s_name (str | Unset):
        k8s_operation (str | Unset):
        attr (list[str] | Unset):
        resource_attr (list[str] | Unset):
        scope_attr (list[str] | Unset):
        q (str | Unset):
        x_nuon_api_offset (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppOtelLogRecord]]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
        order=order,
        start_time=start_time,
        end_time=end_time,
        service_name=service_name,
        scope_name=scope_name,
        scope_version=scope_version,
        resource_schema_url=resource_schema_url,
        scope_schema_url=scope_schema_url,
        severity_text=severity_text,
        severity_number_min=severity_number_min,
        severity_number_max=severity_number_max,
        trace_id=trace_id,
        span_id=span_id,
        trace_flags=trace_flags,
        runner_id=runner_id,
        runner_job_id=runner_job_id,
        runner_group_id=runner_group_id,
        runner_job_execution_id=runner_job_execution_id,
        runner_job_execution_step=runner_job_execution_step,
        tool=tool,
        helm_release_name=helm_release_name,
        helm_chart_name=helm_chart_name,
        helm_chart_id=helm_chart_id,
        helm_namespace=helm_namespace,
        helm_operation=helm_operation,
        tf_workspace_id=tf_workspace_id,
        tf_operation=tf_operation,
        k8s_kind=k8s_kind,
        k8s_namespace=k8s_namespace,
        k8s_name=k8s_name,
        k8s_operation=k8s_operation,
        attr=attr,
        resource_attr=resource_attr,
        scope_attr=scope_attr,
        q=q,
        x_nuon_api_offset=x_nuon_api_offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    order: str | Unset = "asc",
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    service_name: list[str] | Unset = UNSET,
    scope_name: list[str] | Unset = UNSET,
    scope_version: list[str] | Unset = UNSET,
    resource_schema_url: list[str] | Unset = UNSET,
    scope_schema_url: list[str] | Unset = UNSET,
    severity_text: list[str] | Unset = UNSET,
    severity_number_min: int | Unset = UNSET,
    severity_number_max: int | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    trace_flags: int | Unset = UNSET,
    runner_id: str | Unset = UNSET,
    runner_job_id: str | Unset = UNSET,
    runner_group_id: str | Unset = UNSET,
    runner_job_execution_id: str | Unset = UNSET,
    runner_job_execution_step: str | Unset = UNSET,
    tool: list[str] | Unset = UNSET,
    helm_release_name: str | Unset = UNSET,
    helm_chart_name: str | Unset = UNSET,
    helm_chart_id: str | Unset = UNSET,
    helm_namespace: str | Unset = UNSET,
    helm_operation: str | Unset = UNSET,
    tf_workspace_id: str | Unset = UNSET,
    tf_operation: str | Unset = UNSET,
    k8s_kind: str | Unset = UNSET,
    k8s_namespace: str | Unset = UNSET,
    k8s_name: str | Unset = UNSET,
    k8s_operation: str | Unset = UNSET,
    attr: list[str] | Unset = UNSET,
    resource_attr: list[str] | Unset = UNSET,
    scope_attr: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    x_nuon_api_offset: str | Unset = UNSET,
) -> StderrErrResponse | list[AppOtelLogRecord] | None:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        order (str | Unset):  Default: 'asc'.
        start_time (str | Unset):
        end_time (str | Unset):
        service_name (list[str] | Unset):
        scope_name (list[str] | Unset):
        scope_version (list[str] | Unset):
        resource_schema_url (list[str] | Unset):
        scope_schema_url (list[str] | Unset):
        severity_text (list[str] | Unset):
        severity_number_min (int | Unset):
        severity_number_max (int | Unset):
        trace_id (str | Unset):
        span_id (str | Unset):
        trace_flags (int | Unset):
        runner_id (str | Unset):
        runner_job_id (str | Unset):
        runner_group_id (str | Unset):
        runner_job_execution_id (str | Unset):
        runner_job_execution_step (str | Unset):
        tool (list[str] | Unset):
        helm_release_name (str | Unset):
        helm_chart_name (str | Unset):
        helm_chart_id (str | Unset):
        helm_namespace (str | Unset):
        helm_operation (str | Unset):
        tf_workspace_id (str | Unset):
        tf_operation (str | Unset):
        k8s_kind (str | Unset):
        k8s_namespace (str | Unset):
        k8s_name (str | Unset):
        k8s_operation (str | Unset):
        attr (list[str] | Unset):
        resource_attr (list[str] | Unset):
        scope_attr (list[str] | Unset):
        q (str | Unset):
        x_nuon_api_offset (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppOtelLogRecord]
    """

    return sync_detailed(
        log_stream_id=log_stream_id,
        client=client,
        order=order,
        start_time=start_time,
        end_time=end_time,
        service_name=service_name,
        scope_name=scope_name,
        scope_version=scope_version,
        resource_schema_url=resource_schema_url,
        scope_schema_url=scope_schema_url,
        severity_text=severity_text,
        severity_number_min=severity_number_min,
        severity_number_max=severity_number_max,
        trace_id=trace_id,
        span_id=span_id,
        trace_flags=trace_flags,
        runner_id=runner_id,
        runner_job_id=runner_job_id,
        runner_group_id=runner_group_id,
        runner_job_execution_id=runner_job_execution_id,
        runner_job_execution_step=runner_job_execution_step,
        tool=tool,
        helm_release_name=helm_release_name,
        helm_chart_name=helm_chart_name,
        helm_chart_id=helm_chart_id,
        helm_namespace=helm_namespace,
        helm_operation=helm_operation,
        tf_workspace_id=tf_workspace_id,
        tf_operation=tf_operation,
        k8s_kind=k8s_kind,
        k8s_namespace=k8s_namespace,
        k8s_name=k8s_name,
        k8s_operation=k8s_operation,
        attr=attr,
        resource_attr=resource_attr,
        scope_attr=scope_attr,
        q=q,
        x_nuon_api_offset=x_nuon_api_offset,
    ).parsed


async def asyncio_detailed(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    order: str | Unset = "asc",
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    service_name: list[str] | Unset = UNSET,
    scope_name: list[str] | Unset = UNSET,
    scope_version: list[str] | Unset = UNSET,
    resource_schema_url: list[str] | Unset = UNSET,
    scope_schema_url: list[str] | Unset = UNSET,
    severity_text: list[str] | Unset = UNSET,
    severity_number_min: int | Unset = UNSET,
    severity_number_max: int | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    trace_flags: int | Unset = UNSET,
    runner_id: str | Unset = UNSET,
    runner_job_id: str | Unset = UNSET,
    runner_group_id: str | Unset = UNSET,
    runner_job_execution_id: str | Unset = UNSET,
    runner_job_execution_step: str | Unset = UNSET,
    tool: list[str] | Unset = UNSET,
    helm_release_name: str | Unset = UNSET,
    helm_chart_name: str | Unset = UNSET,
    helm_chart_id: str | Unset = UNSET,
    helm_namespace: str | Unset = UNSET,
    helm_operation: str | Unset = UNSET,
    tf_workspace_id: str | Unset = UNSET,
    tf_operation: str | Unset = UNSET,
    k8s_kind: str | Unset = UNSET,
    k8s_namespace: str | Unset = UNSET,
    k8s_name: str | Unset = UNSET,
    k8s_operation: str | Unset = UNSET,
    attr: list[str] | Unset = UNSET,
    resource_attr: list[str] | Unset = UNSET,
    scope_attr: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    x_nuon_api_offset: str | Unset = UNSET,
) -> Response[StderrErrResponse | list[AppOtelLogRecord]]:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        order (str | Unset):  Default: 'asc'.
        start_time (str | Unset):
        end_time (str | Unset):
        service_name (list[str] | Unset):
        scope_name (list[str] | Unset):
        scope_version (list[str] | Unset):
        resource_schema_url (list[str] | Unset):
        scope_schema_url (list[str] | Unset):
        severity_text (list[str] | Unset):
        severity_number_min (int | Unset):
        severity_number_max (int | Unset):
        trace_id (str | Unset):
        span_id (str | Unset):
        trace_flags (int | Unset):
        runner_id (str | Unset):
        runner_job_id (str | Unset):
        runner_group_id (str | Unset):
        runner_job_execution_id (str | Unset):
        runner_job_execution_step (str | Unset):
        tool (list[str] | Unset):
        helm_release_name (str | Unset):
        helm_chart_name (str | Unset):
        helm_chart_id (str | Unset):
        helm_namespace (str | Unset):
        helm_operation (str | Unset):
        tf_workspace_id (str | Unset):
        tf_operation (str | Unset):
        k8s_kind (str | Unset):
        k8s_namespace (str | Unset):
        k8s_name (str | Unset):
        k8s_operation (str | Unset):
        attr (list[str] | Unset):
        resource_attr (list[str] | Unset):
        scope_attr (list[str] | Unset):
        q (str | Unset):
        x_nuon_api_offset (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StderrErrResponse | list[AppOtelLogRecord]]
    """

    kwargs = _get_kwargs(
        log_stream_id=log_stream_id,
        order=order,
        start_time=start_time,
        end_time=end_time,
        service_name=service_name,
        scope_name=scope_name,
        scope_version=scope_version,
        resource_schema_url=resource_schema_url,
        scope_schema_url=scope_schema_url,
        severity_text=severity_text,
        severity_number_min=severity_number_min,
        severity_number_max=severity_number_max,
        trace_id=trace_id,
        span_id=span_id,
        trace_flags=trace_flags,
        runner_id=runner_id,
        runner_job_id=runner_job_id,
        runner_group_id=runner_group_id,
        runner_job_execution_id=runner_job_execution_id,
        runner_job_execution_step=runner_job_execution_step,
        tool=tool,
        helm_release_name=helm_release_name,
        helm_chart_name=helm_chart_name,
        helm_chart_id=helm_chart_id,
        helm_namespace=helm_namespace,
        helm_operation=helm_operation,
        tf_workspace_id=tf_workspace_id,
        tf_operation=tf_operation,
        k8s_kind=k8s_kind,
        k8s_namespace=k8s_namespace,
        k8s_name=k8s_name,
        k8s_operation=k8s_operation,
        attr=attr,
        resource_attr=resource_attr,
        scope_attr=scope_attr,
        q=q,
        x_nuon_api_offset=x_nuon_api_offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    log_stream_id: str,
    *,
    client: AuthenticatedClient,
    order: str | Unset = "asc",
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    service_name: list[str] | Unset = UNSET,
    scope_name: list[str] | Unset = UNSET,
    scope_version: list[str] | Unset = UNSET,
    resource_schema_url: list[str] | Unset = UNSET,
    scope_schema_url: list[str] | Unset = UNSET,
    severity_text: list[str] | Unset = UNSET,
    severity_number_min: int | Unset = UNSET,
    severity_number_max: int | Unset = UNSET,
    trace_id: str | Unset = UNSET,
    span_id: str | Unset = UNSET,
    trace_flags: int | Unset = UNSET,
    runner_id: str | Unset = UNSET,
    runner_job_id: str | Unset = UNSET,
    runner_group_id: str | Unset = UNSET,
    runner_job_execution_id: str | Unset = UNSET,
    runner_job_execution_step: str | Unset = UNSET,
    tool: list[str] | Unset = UNSET,
    helm_release_name: str | Unset = UNSET,
    helm_chart_name: str | Unset = UNSET,
    helm_chart_id: str | Unset = UNSET,
    helm_namespace: str | Unset = UNSET,
    helm_operation: str | Unset = UNSET,
    tf_workspace_id: str | Unset = UNSET,
    tf_operation: str | Unset = UNSET,
    k8s_kind: str | Unset = UNSET,
    k8s_namespace: str | Unset = UNSET,
    k8s_name: str | Unset = UNSET,
    k8s_operation: str | Unset = UNSET,
    attr: list[str] | Unset = UNSET,
    resource_attr: list[str] | Unset = UNSET,
    scope_attr: list[str] | Unset = UNSET,
    q: str | Unset = UNSET,
    x_nuon_api_offset: str | Unset = UNSET,
) -> StderrErrResponse | list[AppOtelLogRecord] | None:
    """read a log stream's logs

     Read OTEL formatted logs for a log stream.

    Args:
        log_stream_id (str):
        order (str | Unset):  Default: 'asc'.
        start_time (str | Unset):
        end_time (str | Unset):
        service_name (list[str] | Unset):
        scope_name (list[str] | Unset):
        scope_version (list[str] | Unset):
        resource_schema_url (list[str] | Unset):
        scope_schema_url (list[str] | Unset):
        severity_text (list[str] | Unset):
        severity_number_min (int | Unset):
        severity_number_max (int | Unset):
        trace_id (str | Unset):
        span_id (str | Unset):
        trace_flags (int | Unset):
        runner_id (str | Unset):
        runner_job_id (str | Unset):
        runner_group_id (str | Unset):
        runner_job_execution_id (str | Unset):
        runner_job_execution_step (str | Unset):
        tool (list[str] | Unset):
        helm_release_name (str | Unset):
        helm_chart_name (str | Unset):
        helm_chart_id (str | Unset):
        helm_namespace (str | Unset):
        helm_operation (str | Unset):
        tf_workspace_id (str | Unset):
        tf_operation (str | Unset):
        k8s_kind (str | Unset):
        k8s_namespace (str | Unset):
        k8s_name (str | Unset):
        k8s_operation (str | Unset):
        attr (list[str] | Unset):
        resource_attr (list[str] | Unset):
        scope_attr (list[str] | Unset):
        q (str | Unset):
        x_nuon_api_offset (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StderrErrResponse | list[AppOtelLogRecord]
    """

    return (
        await asyncio_detailed(
            log_stream_id=log_stream_id,
            client=client,
            order=order,
            start_time=start_time,
            end_time=end_time,
            service_name=service_name,
            scope_name=scope_name,
            scope_version=scope_version,
            resource_schema_url=resource_schema_url,
            scope_schema_url=scope_schema_url,
            severity_text=severity_text,
            severity_number_min=severity_number_min,
            severity_number_max=severity_number_max,
            trace_id=trace_id,
            span_id=span_id,
            trace_flags=trace_flags,
            runner_id=runner_id,
            runner_job_id=runner_job_id,
            runner_group_id=runner_group_id,
            runner_job_execution_id=runner_job_execution_id,
            runner_job_execution_step=runner_job_execution_step,
            tool=tool,
            helm_release_name=helm_release_name,
            helm_chart_name=helm_chart_name,
            helm_chart_id=helm_chart_id,
            helm_namespace=helm_namespace,
            helm_operation=helm_operation,
            tf_workspace_id=tf_workspace_id,
            tf_operation=tf_operation,
            k8s_kind=k8s_kind,
            k8s_namespace=k8s_namespace,
            k8s_name=k8s_name,
            k8s_operation=k8s_operation,
            attr=attr,
            resource_attr=resource_attr,
            scope_attr=scope_attr,
            q=q,
            x_nuon_api_offset=x_nuon_api_offset,
        )
    ).parsed
