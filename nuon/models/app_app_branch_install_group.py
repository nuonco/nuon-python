from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppBranchInstallGroup")


@_attrs_define
class AppAppBranchInstallGroup:
    """
    Attributes:
        app_branch_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_ids (list[str] | Unset):
        max_parallel (int | Unset):
        name (str | Unset):
        order (int | Unset):
        org_id (str | Unset):
        requires_approval (bool | Unset):
        rollback_on_failure (bool | Unset):
        updated_at (str | Unset):
    """

    app_branch_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_ids: list[str] | Unset = UNSET
    max_parallel: int | Unset = UNSET
    name: str | Unset = UNSET
    order: int | Unset = UNSET
    org_id: str | Unset = UNSET
    requires_approval: bool | Unset = UNSET
    rollback_on_failure: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_config_id = self.app_branch_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_ids: list[str] | Unset = UNSET
        if not isinstance(self.install_ids, Unset):
            install_ids = self.install_ids

        max_parallel = self.max_parallel

        name = self.name

        order = self.order

        org_id = self.org_id

        requires_approval = self.requires_approval

        rollback_on_failure = self.rollback_on_failure

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_config_id is not UNSET:
            field_dict["app_branch_config_id"] = app_branch_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_ids is not UNSET:
            field_dict["install_ids"] = install_ids
        if max_parallel is not UNSET:
            field_dict["max_parallel"] = max_parallel
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if requires_approval is not UNSET:
            field_dict["requires_approval"] = requires_approval
        if rollback_on_failure is not UNSET:
            field_dict["rollback_on_failure"] = rollback_on_failure
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_branch_config_id = d.pop("app_branch_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_ids = cast(list[str], d.pop("install_ids", UNSET))

        max_parallel = d.pop("max_parallel", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        org_id = d.pop("org_id", UNSET)

        requires_approval = d.pop("requires_approval", UNSET)

        rollback_on_failure = d.pop("rollback_on_failure", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_branch_install_group = cls(
            app_branch_config_id=app_branch_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_ids=install_ids,
            max_parallel=max_parallel,
            name=name,
            order=order,
            org_id=org_id,
            requires_approval=requires_approval,
            rollback_on_failure=rollback_on_failure,
            updated_at=updated_at,
        )

        app_app_branch_install_group.additional_properties = d
        return app_app_branch_install_group

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
