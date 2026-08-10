from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_install_creation_approval_status import AppInstallCreationApprovalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_proposed_install import AppProposedInstall


T = TypeVar("T", bound="AppInstallCreationApproval")


@_attrs_define
class AppInstallCreationApproval:
    """
    Attributes:
        app_id (str | Unset):
        app_install_config_sync_id (str | Unset):
        approved_at (str | Unset):
        approved_by_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        proposed_installs (list[AppProposedInstall] | Unset):
        status (AppInstallCreationApprovalStatus | Unset):
        updated_at (str | Unset):
    """

    app_id: str | Unset = UNSET
    app_install_config_sync_id: str | Unset = UNSET
    approved_at: str | Unset = UNSET
    approved_by_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    proposed_installs: list[AppProposedInstall] | Unset = UNSET
    status: AppInstallCreationApprovalStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_install_config_sync_id = self.app_install_config_sync_id

        approved_at = self.approved_at

        approved_by_id = self.approved_by_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        proposed_installs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.proposed_installs, Unset):
            proposed_installs = []
            for proposed_installs_item_data in self.proposed_installs:
                proposed_installs_item = proposed_installs_item_data.to_dict()
                proposed_installs.append(proposed_installs_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_install_config_sync_id is not UNSET:
            field_dict["app_install_config_sync_id"] = app_install_config_sync_id
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if approved_by_id is not UNSET:
            field_dict["approved_by_id"] = approved_by_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if proposed_installs is not UNSET:
            field_dict["proposed_installs"] = proposed_installs
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_proposed_install import AppProposedInstall

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        app_install_config_sync_id = d.pop("app_install_config_sync_id", UNSET)

        approved_at = d.pop("approved_at", UNSET)

        approved_by_id = d.pop("approved_by_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _proposed_installs = d.pop("proposed_installs", UNSET)
        proposed_installs: list[AppProposedInstall] | Unset = UNSET
        if _proposed_installs is not UNSET:
            proposed_installs = []
            for proposed_installs_item_data in _proposed_installs:
                proposed_installs_item = AppProposedInstall.from_dict(proposed_installs_item_data)

                proposed_installs.append(proposed_installs_item)

        _status = d.pop("status", UNSET)
        status: AppInstallCreationApprovalStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppInstallCreationApprovalStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        app_install_creation_approval = cls(
            app_id=app_id,
            app_install_config_sync_id=app_install_config_sync_id,
            approved_at=approved_at,
            approved_by_id=approved_by_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            proposed_installs=proposed_installs,
            status=status,
            updated_at=updated_at,
        )

        app_install_creation_approval.additional_properties = d
        return app_install_creation_approval

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
