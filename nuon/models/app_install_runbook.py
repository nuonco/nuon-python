from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_runbook_run import AppInstallRunbookRun
    from ..models.app_runbook import AppRunbook


T = TypeVar("T", bound="AppInstallRunbook")


@_attrs_define
class AppInstallRunbook:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        runbook (AppRunbook | Unset):
        runbook_id (str | Unset):
        runs (list[AppInstallRunbookRun] | Unset):
        status (str | Unset): after query fields
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    runbook: AppRunbook | Unset = UNSET
    runbook_id: str | Unset = UNSET
    runs: list[AppInstallRunbookRun] | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        runbook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runbook, Unset):
            runbook = self.runbook.to_dict()

        runbook_id = self.runbook_id

        runs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()
                runs.append(runs_item)

        status = self.status

        updated_at = self.updated_at

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
        if runbook is not UNSET:
            field_dict["runbook"] = runbook
        if runbook_id is not UNSET:
            field_dict["runbook_id"] = runbook_id
        if runs is not UNSET:
            field_dict["runs"] = runs
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_runbook_run import AppInstallRunbookRun
        from ..models.app_runbook import AppRunbook

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        _runbook = d.pop("runbook", UNSET)
        runbook: AppRunbook | Unset
        if isinstance(_runbook, Unset):
            runbook = UNSET
        else:
            runbook = AppRunbook.from_dict(_runbook)

        runbook_id = d.pop("runbook_id", UNSET)

        _runs = d.pop("runs", UNSET)
        runs: list[AppInstallRunbookRun] | Unset = UNSET
        if _runs is not UNSET:
            runs = []
            for runs_item_data in _runs:
                runs_item = AppInstallRunbookRun.from_dict(runs_item_data)

                runs.append(runs_item)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_runbook = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            runbook=runbook,
            runbook_id=runbook_id,
            runs=runs,
            status=status,
            updated_at=updated_at,
        )

        app_install_runbook.additional_properties = d
        return app_install_runbook

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
