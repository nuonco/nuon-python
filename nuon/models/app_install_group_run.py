from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch_install_group import AppAppBranchInstallGroup
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_group_run_install import AppInstallGroupRunInstall


T = TypeVar("T", bound="AppInstallGroupRun")


@_attrs_define
class AppInstallGroupRun:
    """
    Attributes:
        app_branch_run_id (str | Unset):
        completed_at (str | Unset):
        completed_installs (int | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        failed_installs (int | Unset):
        id (str | Unset):
        install_group (AppAppBranchInstallGroup | Unset):
        install_group_id (str | Unset):
        install_group_name (str | Unset):
        installs (list[AppInstallGroupRunInstall] | Unset):
        org_id (str | Unset):
        started_at (str | Unset):
        status (AppCompositeStatus | Unset):
        total_installs (int | Unset):
        updated_at (str | Unset):
    """

    app_branch_run_id: str | Unset = UNSET
    completed_at: str | Unset = UNSET
    completed_installs: int | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    failed_installs: int | Unset = UNSET
    id: str | Unset = UNSET
    install_group: AppAppBranchInstallGroup | Unset = UNSET
    install_group_id: str | Unset = UNSET
    install_group_name: str | Unset = UNSET
    installs: list[AppInstallGroupRunInstall] | Unset = UNSET
    org_id: str | Unset = UNSET
    started_at: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    total_installs: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_run_id = self.app_branch_run_id

        completed_at = self.completed_at

        completed_installs = self.completed_installs

        created_at = self.created_at

        created_by_id = self.created_by_id

        failed_installs = self.failed_installs

        id = self.id

        install_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_group, Unset):
            install_group = self.install_group.to_dict()

        install_group_id = self.install_group_id

        install_group_name = self.install_group_name

        installs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installs, Unset):
            installs = []
            for installs_item_data in self.installs:
                installs_item = installs_item_data.to_dict()
                installs.append(installs_item)

        org_id = self.org_id

        started_at = self.started_at

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        total_installs = self.total_installs

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_run_id is not UNSET:
            field_dict["app_branch_run_id"] = app_branch_run_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if completed_installs is not UNSET:
            field_dict["completed_installs"] = completed_installs
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if failed_installs is not UNSET:
            field_dict["failed_installs"] = failed_installs
        if id is not UNSET:
            field_dict["id"] = id
        if install_group is not UNSET:
            field_dict["install_group"] = install_group
        if install_group_id is not UNSET:
            field_dict["install_group_id"] = install_group_id
        if install_group_name is not UNSET:
            field_dict["install_group_name"] = install_group_name
        if installs is not UNSET:
            field_dict["installs"] = installs
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if total_installs is not UNSET:
            field_dict["total_installs"] = total_installs
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch_install_group import AppAppBranchInstallGroup
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_group_run_install import AppInstallGroupRunInstall

        d = dict(src_dict)
        app_branch_run_id = d.pop("app_branch_run_id", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        completed_installs = d.pop("completed_installs", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        failed_installs = d.pop("failed_installs", UNSET)

        id = d.pop("id", UNSET)

        _install_group = d.pop("install_group", UNSET)
        install_group: AppAppBranchInstallGroup | Unset
        if isinstance(_install_group, Unset):
            install_group = UNSET
        else:
            install_group = AppAppBranchInstallGroup.from_dict(_install_group)

        install_group_id = d.pop("install_group_id", UNSET)

        install_group_name = d.pop("install_group_name", UNSET)

        _installs = d.pop("installs", UNSET)
        installs: list[AppInstallGroupRunInstall] | Unset = UNSET
        if _installs is not UNSET:
            installs = []
            for installs_item_data in _installs:
                installs_item = AppInstallGroupRunInstall.from_dict(installs_item_data)

                installs.append(installs_item)

        org_id = d.pop("org_id", UNSET)

        started_at = d.pop("started_at", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        total_installs = d.pop("total_installs", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_group_run = cls(
            app_branch_run_id=app_branch_run_id,
            completed_at=completed_at,
            completed_installs=completed_installs,
            created_at=created_at,
            created_by_id=created_by_id,
            failed_installs=failed_installs,
            id=id,
            install_group=install_group,
            install_group_id=install_group_id,
            install_group_name=install_group_name,
            installs=installs,
            org_id=org_id,
            started_at=started_at,
            status=status,
            total_installs=total_installs,
            updated_at=updated_at,
        )

        app_install_group_run.additional_properties = d
        return app_install_group_run

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
