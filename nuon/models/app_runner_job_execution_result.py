from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_job_execution_result_error_metadata import AppRunnerJobExecutionResultErrorMetadata


T = TypeVar("T", bound="AppRunnerJobExecutionResult")


@_attrs_define
class AppRunnerJobExecutionResult:
    """
    Attributes:
        contents (str | Unset):
        contents_display (str | Unset):
        contents_display_gzip (str | Unset):
        contents_gzip (str | Unset): columns for storage of gzipped contents and plans
        created_at (str | Unset):
        created_by_id (str | Unset):
        error_code (int | Unset):
        error_metadata (AppRunnerJobExecutionResultErrorMetadata | Unset):
        id (str | Unset):
        org_id (str | Unset):
        runner_job_execution_id (str | Unset):
        success (bool | Unset):
        updated_at (str | Unset):
    """

    contents: str | Unset = UNSET
    contents_display: str | Unset = UNSET
    contents_display_gzip: str | Unset = UNSET
    contents_gzip: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    error_metadata: AppRunnerJobExecutionResultErrorMetadata | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_job_execution_id: str | Unset = UNSET
    success: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = self.contents

        contents_display = self.contents_display

        contents_display_gzip = self.contents_display_gzip

        contents_gzip = self.contents_gzip

        created_at = self.created_at

        created_by_id = self.created_by_id

        error_code = self.error_code

        error_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_metadata, Unset):
            error_metadata = self.error_metadata.to_dict()

        id = self.id

        org_id = self.org_id

        runner_job_execution_id = self.runner_job_execution_id

        success = self.success

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if contents_display is not UNSET:
            field_dict["contents_display"] = contents_display
        if contents_display_gzip is not UNSET:
            field_dict["contents_display_gzip"] = contents_display_gzip
        if contents_gzip is not UNSET:
            field_dict["contents_gzip"] = contents_gzip
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_metadata is not UNSET:
            field_dict["error_metadata"] = error_metadata
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_job_execution_id is not UNSET:
            field_dict["runner_job_execution_id"] = runner_job_execution_id
        if success is not UNSET:
            field_dict["success"] = success
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_job_execution_result_error_metadata import AppRunnerJobExecutionResultErrorMetadata

        d = dict(src_dict)
        contents = d.pop("contents", UNSET)

        contents_display = d.pop("contents_display", UNSET)

        contents_display_gzip = d.pop("contents_display_gzip", UNSET)

        contents_gzip = d.pop("contents_gzip", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        error_code = d.pop("error_code", UNSET)

        _error_metadata = d.pop("error_metadata", UNSET)
        error_metadata: AppRunnerJobExecutionResultErrorMetadata | Unset
        if isinstance(_error_metadata, Unset):
            error_metadata = UNSET
        else:
            error_metadata = AppRunnerJobExecutionResultErrorMetadata.from_dict(_error_metadata)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        runner_job_execution_id = d.pop("runner_job_execution_id", UNSET)

        success = d.pop("success", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_job_execution_result = cls(
            contents=contents,
            contents_display=contents_display,
            contents_display_gzip=contents_display_gzip,
            contents_gzip=contents_gzip,
            created_at=created_at,
            created_by_id=created_by_id,
            error_code=error_code,
            error_metadata=error_metadata,
            id=id,
            org_id=org_id,
            runner_job_execution_id=runner_job_execution_id,
            success=success,
            updated_at=updated_at,
        )

        app_runner_job_execution_result.additional_properties = d
        return app_runner_job_execution_result

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
