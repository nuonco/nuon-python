from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_runner_status import AppRunnerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job import AppRunnerJob


T = TypeVar("T", bound="AppRunnerHealthCheck")


@_attrs_define
class AppRunnerHealthCheck:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        minute_bucket (Union[Unset, str]):
        process (Union[Unset, str]):
        runner_id (Union[Unset, str]):
        runner_job (Union[Unset, AppRunnerJob]):
        status (Union[Unset, AppRunnerStatus]):
        status_code (Union[Unset, int]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    minute_bucket: Union[Unset, str] = UNSET
    process: Union[Unset, str] = UNSET
    runner_id: Union[Unset, str] = UNSET
    runner_job: Union[Unset, "AppRunnerJob"] = UNSET
    status: Union[Unset, AppRunnerStatus] = UNSET
    status_code: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        minute_bucket = self.minute_bucket

        process = self.process

        runner_id = self.runner_id

        runner_job: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_code = self.status_code

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
        if minute_bucket is not UNSET:
            field_dict["minute_bucket"] = minute_bucket
        if process is not UNSET:
            field_dict["process"] = process
        if runner_id is not UNSET:
            field_dict["runner_id"] = runner_id
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job import AppRunnerJob

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        minute_bucket = d.pop("minute_bucket", UNSET)

        process = d.pop("process", UNSET)

        runner_id = d.pop("runner_id", UNSET)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: Union[Unset, AppRunnerJob]
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppRunnerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppRunnerStatus(_status)

        status_code = d.pop("status_code", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_health_check = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            minute_bucket=minute_bucket,
            process=process,
            runner_id=runner_id,
            runner_job=runner_job,
            status=status,
            status_code=status_code,
            updated_at=updated_at,
        )

        app_runner_health_check.additional_properties = d
        return app_runner_health_check

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
