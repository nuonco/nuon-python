from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job import AppRunnerJob
    from ..models.app_terraform_lock import AppTerraformLock


T = TypeVar("T", bound="AppTerraformWorkspaceLock")


@_attrs_define
class AppTerraformWorkspaceLock:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        lock (Union[Unset, AppTerraformLock]):
        runner_job (Union[Unset, AppRunnerJob]):
        runner_job_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        workspace_id (Union[Unset, str]): Foreign key to TerraformWorkspace with unique constraint to prevent multiple
            active locks
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    lock: Union[Unset, "AppTerraformLock"] = UNSET
    runner_job: Union[Unset, "AppRunnerJob"] = UNSET
    runner_job_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        lock: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock.to_dict()

        runner_job: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        runner_job_id = self.runner_job_id

        updated_at = self.updated_at

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock is not UNSET:
            field_dict["lock"] = lock
        if runner_job is not UNSET:
            field_dict["runner_job"] = runner_job
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job import AppRunnerJob
        from ..models.app_terraform_lock import AppTerraformLock

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _lock = d.pop("lock", UNSET)
        lock: Union[Unset, AppTerraformLock]
        if isinstance(_lock, Unset):
            lock = UNSET
        else:
            lock = AppTerraformLock.from_dict(_lock)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: Union[Unset, AppRunnerJob]
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        runner_job_id = d.pop("runner_job_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        app_terraform_workspace_lock = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            lock=lock,
            runner_job=runner_job,
            runner_job_id=runner_job_id,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        app_terraform_workspace_lock.additional_properties = d
        return app_terraform_workspace_lock

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
