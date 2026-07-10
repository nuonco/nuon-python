from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch import AppAppBranch


T = TypeVar("T", bound="AppInstallAppBranchConnection")


@_attrs_define
class AppInstallAppBranchConnection:
    """
    Attributes:
        activated_at (str | Unset):
        active (bool | Unset):
        app_branch (AppAppBranch | Unset):
        app_branch_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        deactivated_at (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        updated_at (str | Unset):
    """

    activated_at: str | Unset = UNSET
    active: bool | Unset = UNSET
    app_branch: AppAppBranch | Unset = UNSET
    app_branch_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    deactivated_at: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activated_at = self.activated_at

        active = self.active

        app_branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_branch, Unset):
            app_branch = self.app_branch.to_dict()

        app_branch_id = self.app_branch_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        deactivated_at = self.deactivated_at

        id = self.id

        install_id = self.install_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at
        if active is not UNSET:
            field_dict["active"] = active
        if app_branch is not UNSET:
            field_dict["app_branch"] = app_branch
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if deactivated_at is not UNSET:
            field_dict["deactivated_at"] = deactivated_at
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch import AppAppBranch

        d = dict(src_dict)
        activated_at = d.pop("activated_at", UNSET)

        active = d.pop("active", UNSET)

        _app_branch = d.pop("app_branch", UNSET)
        app_branch: AppAppBranch | Unset
        if isinstance(_app_branch, Unset):
            app_branch = UNSET
        else:
            app_branch = AppAppBranch.from_dict(_app_branch)

        app_branch_id = d.pop("app_branch_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        deactivated_at = d.pop("deactivated_at", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_app_branch_connection = cls(
            activated_at=activated_at,
            active=active,
            app_branch=app_branch,
            app_branch_id=app_branch_id,
            created_at=created_at,
            created_by_id=created_by_id,
            deactivated_at=deactivated_at,
            id=id,
            install_id=install_id,
            updated_at=updated_at,
        )

        app_install_app_branch_connection.additional_properties = d
        return app_install_app_branch_connection

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
