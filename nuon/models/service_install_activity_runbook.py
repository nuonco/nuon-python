from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallActivityRunbook")


@_attrs_define
class ServiceInstallActivityRunbook:
    """
    Attributes:
        name (str | Unset):
        run_id (str | Unset):
        runbook_id (str | Unset):
    """

    name: str | Unset = UNSET
    run_id: str | Unset = UNSET
    runbook_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        run_id = self.run_id

        runbook_id = self.runbook_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if runbook_id is not UNSET:
            field_dict["runbook_id"] = runbook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        run_id = d.pop("run_id", UNSET)

        runbook_id = d.pop("runbook_id", UNSET)

        service_install_activity_runbook = cls(
            name=name,
            run_id=run_id,
            runbook_id=runbook_id,
        )

        service_install_activity_runbook.additional_properties = d
        return service_install_activity_runbook

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
