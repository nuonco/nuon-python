from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_job_group import AppRunnerJobGroup
from ..models.app_runner_job_operation_type import AppRunnerJobOperationType
from ..models.app_runner_job_status import AppRunnerJobStatus
from ..models.app_runner_job_type import AppRunnerJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job_execution import AppRunnerJobExecution
    from ..models.app_runner_job_metadata import AppRunnerJobMetadata
    from ..models.app_runner_job_outputs import AppRunnerJobOutputs


T = TypeVar("T", bound="AppRunnerJob")


@_attrs_define
class AppRunnerJob:
    """
    Attributes:
        available_timeout (int | Unset): available timeout is how long a job can be marked as "available" before being
            requeued
        created_at (str | Unset):
        created_by_id (str | Unset):
        execution_count (int | Unset):
        execution_time (int | Unset):
        execution_timeout (int | Unset): execution timeout is how long a job can be marked as "exeucuting" before being
            requeued
        executions (list[AppRunnerJobExecution] | Unset):
        final_runner_job_execution_id (str | Unset):
        finished_at (str | Unset):
        group (AppRunnerJobGroup | Unset):
        id (str | Unset):
        log_stream_id (str | Unset):
        max_executions (int | Unset):
        metadata (AppRunnerJobMetadata | Unset):
        operation (AppRunnerJobOperationType | Unset):
        org_id (str | Unset):
        outputs (AppRunnerJobOutputs | Unset):
        outputs_json (str | Unset):
        overall_timeout (int | Unset): overall timeout is how long a job can be attempted, before being cancelled
        owner_id (str | Unset):
        owner_type (str | Unset):
        queue_timeout (int | Unset): queue timeout is how long a job can be queued, before being made available
        runner_id (str | Unset):
        started_at (str | Unset):
        status (AppRunnerJobStatus | Unset):
        status_description (str | Unset):
        type_ (AppRunnerJobType | Unset):
        updated_at (str | Unset):
    """

    available_timeout: int | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    execution_count: int | Unset = UNSET
    execution_time: int | Unset = UNSET
    execution_timeout: int | Unset = UNSET
    executions: list[AppRunnerJobExecution] | Unset = UNSET
    final_runner_job_execution_id: str | Unset = UNSET
    finished_at: str | Unset = UNSET
    group: AppRunnerJobGroup | Unset = UNSET
    id: str | Unset = UNSET
    log_stream_id: str | Unset = UNSET
    max_executions: int | Unset = UNSET
    metadata: AppRunnerJobMetadata | Unset = UNSET
    operation: AppRunnerJobOperationType | Unset = UNSET
    org_id: str | Unset = UNSET
    outputs: AppRunnerJobOutputs | Unset = UNSET
    outputs_json: str | Unset = UNSET
    overall_timeout: int | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    queue_timeout: int | Unset = UNSET
    runner_id: str | Unset = UNSET
    started_at: str | Unset = UNSET
    status: AppRunnerJobStatus | Unset = UNSET
    status_description: str | Unset = UNSET
    type_: AppRunnerJobType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_timeout = self.available_timeout

        created_at = self.created_at

        created_by_id = self.created_by_id

        execution_count = self.execution_count

        execution_time = self.execution_time

        execution_timeout = self.execution_timeout

        executions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.executions, Unset):
            executions = []
            for executions_item_data in self.executions:
                executions_item = executions_item_data.to_dict()
                executions.append(executions_item)

        final_runner_job_execution_id = self.final_runner_job_execution_id

        finished_at = self.finished_at

        group: str | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.value

        id = self.id

        log_stream_id = self.log_stream_id

        max_executions = self.max_executions

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        org_id = self.org_id

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        outputs_json = self.outputs_json

        overall_timeout = self.overall_timeout

        owner_id = self.owner_id

        owner_type = self.owner_type

        queue_timeout = self.queue_timeout

        runner_id = self.runner_id

        started_at = self.started_at

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_description = self.status_description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_timeout is not UNSET:
            field_dict["available_timeout"] = available_timeout
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if execution_count is not UNSET:
            field_dict["execution_count"] = execution_count
        if execution_time is not UNSET:
            field_dict["execution_time"] = execution_time
        if execution_timeout is not UNSET:
            field_dict["execution_timeout"] = execution_timeout
        if executions is not UNSET:
            field_dict["executions"] = executions
        if final_runner_job_execution_id is not UNSET:
            field_dict["final_runner_job_execution_id"] = final_runner_job_execution_id
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if log_stream_id is not UNSET:
            field_dict["log_stream_id"] = log_stream_id
        if max_executions is not UNSET:
            field_dict["max_executions"] = max_executions
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if operation is not UNSET:
            field_dict["operation"] = operation
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if outputs_json is not UNSET:
            field_dict["outputs_json"] = outputs_json
        if overall_timeout is not UNSET:
            field_dict["overall_timeout"] = overall_timeout
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if queue_timeout is not UNSET:
            field_dict["queue_timeout"] = queue_timeout
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job_execution import AppRunnerJobExecution
        from ..models.app_runner_job_metadata import AppRunnerJobMetadata
        from ..models.app_runner_job_outputs import AppRunnerJobOutputs

        d = dict(src_dict)
        available_timeout = d.pop("available_timeout", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        execution_count = d.pop("execution_count", UNSET)

        execution_time = d.pop("execution_time", UNSET)

        execution_timeout = d.pop("execution_timeout", UNSET)

        _executions = d.pop("executions", UNSET)
        executions: list[AppRunnerJobExecution] | Unset = UNSET
        if _executions is not UNSET:
            executions = []
            for executions_item_data in _executions:
                executions_item = AppRunnerJobExecution.from_dict(executions_item_data)

                executions.append(executions_item)

        final_runner_job_execution_id = d.pop("final_runner_job_execution_id", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        _group = d.pop("group", UNSET)
        group: AppRunnerJobGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = AppRunnerJobGroup(_group)

        id = d.pop("id", UNSET)

        log_stream_id = d.pop("log_stream_id", UNSET)

        max_executions = d.pop("max_executions", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppRunnerJobMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppRunnerJobMetadata.from_dict(_metadata)

        _operation = d.pop("operation", UNSET)
        operation: AppRunnerJobOperationType | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = AppRunnerJobOperationType(_operation)

        org_id = d.pop("org_id", UNSET)

        _outputs = d.pop("outputs", UNSET)
        outputs: AppRunnerJobOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppRunnerJobOutputs.from_dict(_outputs)

        outputs_json = d.pop("outputs_json", UNSET)

        overall_timeout = d.pop("overall_timeout", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        queue_timeout = d.pop("queue_timeout", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        started_at = d.pop("started_at", UNSET)

        _status = d.pop("status", UNSET)
        status: AppRunnerJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppRunnerJobStatus(_status)

        status_description = d.pop("status_description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppRunnerJobType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppRunnerJobType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_job = cls(
            available_timeout=available_timeout,
            created_at=created_at,
            created_by_id=created_by_id,
            execution_count=execution_count,
            execution_time=execution_time,
            execution_timeout=execution_timeout,
            executions=executions,
            final_runner_job_execution_id=final_runner_job_execution_id,
            finished_at=finished_at,
            group=group,
            id=id,
            log_stream_id=log_stream_id,
            max_executions=max_executions,
            metadata=metadata,
            operation=operation,
            org_id=org_id,
            outputs=outputs,
            outputs_json=outputs_json,
            overall_timeout=overall_timeout,
            owner_id=owner_id,
            owner_type=owner_type,
            queue_timeout=queue_timeout,
            runner_id=runner_id,
            started_at=started_at,
            status=status,
            status_description=status_description,
            type_=type_,
            updated_at=updated_at,
        )

        app_runner_job.additional_properties = d
        return app_runner_job

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
