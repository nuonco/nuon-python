from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_queue import AppQueue
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
        queues (list[AppQueue] | Unset): Queues holds per-job-group queues created when parallel-runner-jobs feature
            flag is enabled.
        runner_group (AppRunnerGroup | Unset):
        runner_group_id (str | Unset):
        runner_job (AppRunnerJob | Unset):
        status (str | Unset):
        status_description (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        warnings (list[str] | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    jobs: list[AppRunnerJob] | Unset = UNSET
    name: str | Unset = UNSET
    operations: list[AppRunnerOperation] | Unset = UNSET
    org_id: str | Unset = UNSET
    queues: list[AppQueue] | Unset = UNSET
    runner_group: AppRunnerGroup | Unset = UNSET
    runner_group_id: str | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    status: str | Unset = UNSET
    status_description: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
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

        queues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queues, Unset):
            queues = []
            for queues_item_data in self.queues:
                queues_item = queues_item_data.to_dict()
                queues.append(queues_item)

        runner_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_group, Unset):
            runner_group = self.runner_group.to_dict()

        runner_group_id = self.runner_group_id

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        status = self.status

        status_description = self.status_description

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        updated_at = self.updated_at

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

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
        if queues is not UNSET:
            field_dict["queues"] = queues
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
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_queue import AppQueue
        from ..models.app_runner_group import AppRunnerGroup
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_runner_operation import AppRunnerOperation

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        _jobs = d.pop("jobs", UNSET)
        jobs: list[AppRunnerJob] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = AppRunnerJob.from_dict(jobs_item_data)

                jobs.append(jobs_item)

        name = d.pop("name", UNSET)

        _operations = d.pop("operations", UNSET)
        operations: list[AppRunnerOperation] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = AppRunnerOperation.from_dict(operations_item_data)

                operations.append(operations_item)

        org_id = d.pop("org_id", UNSET)

        _queues = d.pop("queues", UNSET)
        queues: list[AppQueue] | Unset = UNSET
        if _queues is not UNSET:
            queues = []
            for queues_item_data in _queues:
                queues_item = AppQueue.from_dict(queues_item_data)

                queues.append(queues_item)

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

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        updated_at = d.pop("updated_at", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        app_runner = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            display_name=display_name,
            id=id,
            jobs=jobs,
            name=name,
            operations=operations,
            org_id=org_id,
            queues=queues,
            runner_group=runner_group,
            runner_group_id=runner_group_id,
            runner_job=runner_job,
            status=status,
            status_description=status_description,
            status_v2=status_v2,
            updated_at=updated_at,
            warnings=warnings,
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
