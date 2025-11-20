from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_job_execution_status import AppRunnerJobExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job_execution_metadata import AppRunnerJobExecutionMetadata
    from ..models.app_runner_job_execution_outputs import AppRunnerJobExecutionOutputs
    from ..models.app_runner_job_execution_result import AppRunnerJobExecutionResult


T = TypeVar("T", bound="AppRunnerJobExecution")


@_attrs_define
class AppRunnerJobExecution:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        metadata (AppRunnerJobExecutionMetadata | Unset): Metadata is used to store additional information about the
            execution {e.g., client version.}
        org_id (str | Unset):
        outputs (AppRunnerJobExecutionOutputs | Unset):
        result (AppRunnerJobExecutionResult | Unset):
        runner_job_id (str | Unset):
        status (AppRunnerJobExecutionStatus | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    metadata: AppRunnerJobExecutionMetadata | Unset = UNSET
    org_id: str | Unset = UNSET
    outputs: AppRunnerJobExecutionOutputs | Unset = UNSET
    result: AppRunnerJobExecutionResult | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    status: AppRunnerJobExecutionStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_id = self.org_id

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        runner_job_id = self.runner_job_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if result is not UNSET:
            field_dict["result"] = result
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job_execution_metadata import AppRunnerJobExecutionMetadata
        from ..models.app_runner_job_execution_outputs import AppRunnerJobExecutionOutputs
        from ..models.app_runner_job_execution_result import AppRunnerJobExecutionResult

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppRunnerJobExecutionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppRunnerJobExecutionMetadata.from_dict(_metadata)

        org_id = d.pop("org_id", UNSET)

        _outputs = d.pop("outputs", UNSET)
        outputs: AppRunnerJobExecutionOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppRunnerJobExecutionOutputs.from_dict(_outputs)

        _result = d.pop("result", UNSET)
        result: AppRunnerJobExecutionResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = AppRunnerJobExecutionResult.from_dict(_result)

        runner_job_id = d.pop("runner_job_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppRunnerJobExecutionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppRunnerJobExecutionStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_job_execution = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            metadata=metadata,
            org_id=org_id,
            outputs=outputs,
            result=result,
            runner_job_id=runner_job_id,
            status=status,
            updated_at=updated_at,
        )

        app_runner_job_execution.additional_properties = d
        return app_runner_job_execution

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
