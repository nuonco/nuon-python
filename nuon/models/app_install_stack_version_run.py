from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_stack_version_run_data import AppInstallStackVersionRunData
    from ..models.app_install_stack_version_run_data_contents import AppInstallStackVersionRunDataContents


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
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    data: AppInstallStackVersionRunData | Unset = UNSET
    data_contents: AppInstallStackVersionRunDataContents | Unset = UNSET
    id: str | Unset = UNSET
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
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_stack_version_run_data import AppInstallStackVersionRunData
        from ..models.app_install_stack_version_run_data_contents import AppInstallStackVersionRunDataContents

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

        updated_at = d.pop("updated_at", UNSET)

        app_install_stack_version_run = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            data=data,
            data_contents=data_contents,
            id=id,
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
