from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_stack_version_run_type import AppStackVersionRunType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_stack_version_run_data import AppInstallStackVersionRunData
    from ..models.app_install_stack_version_run_data_contents import AppInstallStackVersionRunDataContents
    from ..models.app_stack_version_run_input_diff import AppStackVersionRunInputDiff
    from ..models.app_stack_version_run_role_diff import AppStackVersionRunRoleDiff


T = TypeVar("T", bound="AppInstallStackVersionRun")


@_attrs_define
class AppInstallStackVersionRun:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        data (AppInstallStackVersionRunData | Unset):
        data_contents (AppInstallStackVersionRunDataContents | Unset):
        id (str | Unset):
        input_diff (AppStackVersionRunInputDiff | Unset):
        role_diff (AppStackVersionRunRoleDiff | Unset):
        run_type (AppStackVersionRunType | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    data: AppInstallStackVersionRunData | Unset = UNSET
    data_contents: AppInstallStackVersionRunDataContents | Unset = UNSET
    id: str | Unset = UNSET
    input_diff: AppStackVersionRunInputDiff | Unset = UNSET
    role_diff: AppStackVersionRunRoleDiff | Unset = UNSET
    run_type: AppStackVersionRunType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        data_contents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_contents, Unset):
            data_contents = self.data_contents.to_dict()

        id = self.id

        input_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_diff, Unset):
            input_diff = self.input_diff.to_dict()

        role_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_diff, Unset):
            role_diff = self.role_diff.to_dict()

        run_type: str | Unset = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if data is not UNSET:
            field_dict["data"] = data
        if data_contents is not UNSET:
            field_dict["data_contents"] = data_contents
        if id is not UNSET:
            field_dict["id"] = id
        if input_diff is not UNSET:
            field_dict["input_diff"] = input_diff
        if role_diff is not UNSET:
            field_dict["role_diff"] = role_diff
        if run_type is not UNSET:
            field_dict["run_type"] = run_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_stack_version_run_data import AppInstallStackVersionRunData
        from ..models.app_install_stack_version_run_data_contents import AppInstallStackVersionRunDataContents
        from ..models.app_stack_version_run_input_diff import AppStackVersionRunInputDiff
        from ..models.app_stack_version_run_role_diff import AppStackVersionRunRoleDiff

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _data = d.pop("data", UNSET)
        data: AppInstallStackVersionRunData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AppInstallStackVersionRunData.from_dict(_data)

        _data_contents = d.pop("data_contents", UNSET)
        data_contents: AppInstallStackVersionRunDataContents | Unset
        if isinstance(_data_contents, Unset):
            data_contents = UNSET
        else:
            data_contents = AppInstallStackVersionRunDataContents.from_dict(_data_contents)

        id = d.pop("id", UNSET)

        _input_diff = d.pop("input_diff", UNSET)
        input_diff: AppStackVersionRunInputDiff | Unset
        if isinstance(_input_diff, Unset):
            input_diff = UNSET
        else:
            input_diff = AppStackVersionRunInputDiff.from_dict(_input_diff)

        _role_diff = d.pop("role_diff", UNSET)
        role_diff: AppStackVersionRunRoleDiff | Unset
        if isinstance(_role_diff, Unset):
            role_diff = UNSET
        else:
            role_diff = AppStackVersionRunRoleDiff.from_dict(_role_diff)

        _run_type = d.pop("run_type", UNSET)
        run_type: AppStackVersionRunType | Unset
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = AppStackVersionRunType(_run_type)

        updated_at = d.pop("updated_at", UNSET)

        app_install_stack_version_run = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            data=data,
            data_contents=data_contents,
            id=id,
            input_diff=input_diff,
            role_diff=role_diff,
            run_type=run_type,
            updated_at=updated_at,
        )

        app_install_stack_version_run.additional_properties = d
        return app_install_stack_version_run

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
