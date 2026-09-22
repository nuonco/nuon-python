from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch_run import AppAppBranchRun
    from ..models.service_install_update import ServiceInstallUpdate


T = TypeVar("T", bound="ServiceInstallUpdatesResponse")


@_attrs_define
class ServiceInstallUpdatesResponse:
    """
    Attributes:
        current_app_branch_run (AppAppBranchRun | Unset):
        has_more (bool | Unset):
        limit (int | Unset):
        page (int | Unset):
        updates (list[ServiceInstallUpdate] | Unset):
    """

    current_app_branch_run: AppAppBranchRun | Unset = UNSET
    has_more: bool | Unset = UNSET
    limit: int | Unset = UNSET
    page: int | Unset = UNSET
    updates: list[ServiceInstallUpdate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_app_branch_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_app_branch_run, Unset):
            current_app_branch_run = self.current_app_branch_run.to_dict()

        has_more = self.has_more

        limit = self.limit

        page = self.page

        updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for updates_item_data in self.updates:
                updates_item = updates_item_data.to_dict()
                updates.append(updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_app_branch_run is not UNSET:
            field_dict["current_app_branch_run"] = current_app_branch_run
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch_run import AppAppBranchRun  # noqa: PLC0415
        from ..models.service_install_update import ServiceInstallUpdate  # noqa: PLC0415

        d = dict(src_dict)
        _current_app_branch_run = d.pop("current_app_branch_run", UNSET)
        current_app_branch_run: AppAppBranchRun | Unset
        if isinstance(_current_app_branch_run, Unset):
            current_app_branch_run = UNSET
        else:
            current_app_branch_run = AppAppBranchRun.from_dict(_current_app_branch_run)

        has_more = d.pop("has_more", UNSET)

        limit = d.pop("limit", UNSET)

        page = d.pop("page", UNSET)

        _updates = d.pop("updates", UNSET)
        updates: list[ServiceInstallUpdate] | Unset = UNSET
        if _updates is not UNSET:
            updates = []
            for updates_item_data in _updates:
                updates_item = ServiceInstallUpdate.from_dict(updates_item_data)

                updates.append(updates_item)

        service_install_updates_response = cls(
            current_app_branch_run=current_app_branch_run,
            has_more=has_more,
            limit=limit,
            page=page,
            updates=updates,
        )

        service_install_updates_response.additional_properties = d
        return service_install_updates_response

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
