from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job import AppRunnerJob


T = TypeVar("T", bound="AppTerraformWorkspaceStateJSON")


@_attrs_define
class AppTerraformWorkspaceStateJSON:
    """
    Attributes:
        contents (list[int] | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        runner_job (AppRunnerJob | Unset):
        runner_job_id (str | Unset):
        updated_at (str | Unset):
        workspace_id (str | Unset): Foreign key to TerraformWorkspace with unique constraint to prevent conflicting
            states for a workspace
    """

    contents: list[int] | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_job: AppRunnerJob | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents: list[int] | Unset = UNSET
        if not isinstance(self.contents, Unset):
            contents = self.contents

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        runner_job: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runner_job, Unset):
            runner_job = self.runner_job.to_dict()

        runner_job_id = self.runner_job_id

        updated_at = self.updated_at

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
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

        d = dict(src_dict)
        contents = cast(list[int], d.pop("contents", UNSET))

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _runner_job = d.pop("runner_job", UNSET)
        runner_job: AppRunnerJob | Unset
        if isinstance(_runner_job, Unset):
            runner_job = UNSET
        else:
            runner_job = AppRunnerJob.from_dict(_runner_job)

        runner_job_id = d.pop("runner_job_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        app_terraform_workspace_state_json = cls(
            contents=contents,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            runner_job=runner_job,
            runner_job_id=runner_job_id,
            updated_at=updated_at,
            workspace_id=workspace_id,
        )

        app_terraform_workspace_state_json.additional_properties = d
        return app_terraform_workspace_state_json

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
