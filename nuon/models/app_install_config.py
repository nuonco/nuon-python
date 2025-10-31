from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_approval_option import AppInstallApprovalOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallConfig")


@_attrs_define
class AppInstallConfig:
    """
    Attributes:
        approval_option (AppInstallApprovalOption | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    approval_option: AppInstallApprovalOption | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_option: str | Unset = UNSET
        if not isinstance(self.approval_option, Unset):
            approval_option = self.approval_option.value

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_option is not UNSET:
            field_dict["approval_option"] = approval_option
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _approval_option = d.pop("approval_option", UNSET)
        approval_option: AppInstallApprovalOption | Unset
        if isinstance(_approval_option, Unset):
            approval_option = UNSET
        else:
            approval_option = AppInstallApprovalOption(_approval_option)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_config = cls(
            approval_option=approval_option,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_install_config.additional_properties = d
        return app_install_config

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
