from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_group import AppRunnerGroup
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_runner_operation import AppRunnerOperation


T = TypeVar("T", bound="AppRunner")


@_attrs_define
class AppRunner:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        jobs (list[AppRunnerJob] | Unset):
        name (str | Unset):
        operations (list[AppRunnerOperation] | Unset):
        org_id (str | Unset):
        runner_group (AppRunnerGroup | Unset):
        runner_group_id (str | Unset):
        runner_job (AppRunnerJob | Unset):
        status (str | Unset):
        status_description (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    jobs: list[AppRunnerJob] | Unset = UNSET
    name: str | Unset = UNSET
    operations: list[AppRunnerOperation] | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_group: AppRunnerGroup | Unset = UNSET
    runner_group_id: str | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        display_name = self.display_name

        id = self.id

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)

        name = self.name

        operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()
                operations.append(operations_item)

        org_id = self.org_id

        runner_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_group, Unset):
            runner_group = self.runner_group.to_dict()

        runner_group_id = self.runner_group_id

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if name is not UNSET:
            field_dict["name"] = name
        if operations is not UNSET:
            field_dict["operations"] = operations
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_group is not UNSET:
            field_dict["runner_group"] = runner_group
        if runner_group_id is not UNSET:
            field_dict["runner_group_id"] = runner_group_id
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_group import AppRunnerGroup
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_runner_operation import AppRunnerOperation

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        jobs = []
        _jobs = d.pop("jobs", UNSET)
        for jobs_item_data in _jobs or []:
            jobs_item = AppRunnerJob.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        name = d.pop("name", UNSET)

        operations = []
        _operations = d.pop("operations", UNSET)
        for operations_item_data in _operations or []:
            operations_item = AppRunnerOperation.from_dict(operations_item_data)

            operations.append(operations_item)

        org_id = d.pop("org_id", UNSET)

        _runner_group = d.pop("runner_group", UNSET)
        runner_group: AppRunnerGroup | Unset
        if isinstance(_runner_group, Unset):
            runner_group = UNSET
        else:
            runner_group = AppRunnerGroup.from_dict(_runner_group)

        runner_group_id = d.pop("runner_group_id", UNSET)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runner = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            display_name=display_name,
            id=id,
            jobs=jobs,
            name=name,
            operations=operations,
            org_id=org_id,
            runner_group=runner_group,
            runner_group_id=runner_group_id,
            runner_job=runner_job,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
        )

        app_runner.additional_properties = d
        return app_runner

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
