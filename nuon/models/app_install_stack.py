from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_stack_outputs import AppInstallStackOutputs
    from ..models.app_install_stack_version import AppInstallStackVersion


T = TypeVar("T", bound="AppInstallStack")


@_attrs_define
class AppInstallStack:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        install_stack_outputs (AppInstallStackOutputs | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
        versions (list[AppInstallStackVersion] | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_stack_outputs: AppInstallStackOutputs | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    versions: list[AppInstallStackVersion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        install_stack_outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_stack_outputs, Unset):
            install_stack_outputs = self.install_stack_outputs.to_dict()

        org_id = self.org_id

        updated_at = self.updated_at

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_stack_outputs is not UNSET:
            field_dict["install_stack_outputs"] = install_stack_outputs
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_stack_outputs import AppInstallStackOutputs
        from ..models.app_install_stack_version import AppInstallStackVersion

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _install_stack_outputs = d.pop("install_stack_outputs", UNSET)
        install_stack_outputs: AppInstallStackOutputs | Unset
        if isinstance(_install_stack_outputs, Unset):
            install_stack_outputs = UNSET
        else:
            install_stack_outputs = AppInstallStackOutputs.from_dict(_install_stack_outputs)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _versions = d.pop("versions", UNSET)
        versions: list[AppInstallStackVersion] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = AppInstallStackVersion.from_dict(versions_item_data)

                versions.append(versions_item)

        app_install_stack = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            install_stack_outputs=install_stack_outputs,
            org_id=org_id,
            updated_at=updated_at,
            versions=versions,
        )

        app_install_stack.additional_properties = d
        return app_install_stack

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
