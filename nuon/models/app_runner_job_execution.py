from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_job_execution_status import AppRunnerJobExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job_execution_outputs import AppRunnerJobExecutionOutputs
    from ..models.app_runner_job_execution_result import AppRunnerJobExecutionResult


T = TypeVar("T", bound="AppRunnerJobExecution")


@_attrs_define
class AppRunnerJobExecution:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        outputs (Union[Unset, AppRunnerJobExecutionOutputs]):
        result (Union[Unset, AppRunnerJobExecutionResult]):
        runner_job_id (Union[Unset, str]):
        status (Union[Unset, AppRunnerJobExecutionStatus]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    outputs: Union[Unset, "AppRunnerJobExecutionOutputs"] = UNSET
    result: Union[Unset, "AppRunnerJobExecutionResult"] = UNSET
    runner_job_id: Union[Unset, str] = UNSET
    status: Union[Unset, AppRunnerJobExecutionStatus] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        outputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        runner_job_id = self.runner_job_id

        status: Union[Unset, str] = UNSET
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
        from ..models.app_runner_job_execution_outputs import AppRunnerJobExecutionOutputs
        from ..models.app_runner_job_execution_result import AppRunnerJobExecutionResult

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, AppRunnerJobExecutionOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = AppRunnerJobExecutionOutputs.from_dict(_outputs)

        _result = d.pop("result", UNSET)
        result: Union[Unset, AppRunnerJobExecutionResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = AppRunnerJobExecutionResult.from_dict(_result)

        runner_job_id = d.pop("runner_job_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppRunnerJobExecutionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppRunnerJobExecutionStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_job_execution = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
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
