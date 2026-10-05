from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceInstallHealthcheck")


@_attrs_define
class ServiceInstallHealthcheck:
    """
    Attributes:
        action_id (str | Unset):
        last_run_at (str | Unset):
        name (str | Unset):
        status (str | Unset):
        workflow_id (str | Unset):
    """

    action_id: str | Unset = UNSET
    last_run_at: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_id = self.action_id

        last_run_at = self.last_run_at

        name = self.name

        status = self.status

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_id is not UNSET:
            field_dict["action_id"] = action_id
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_id = d.pop("action_id", UNSET)

        last_run_at = d.pop("last_run_at", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        service_install_healthcheck = cls(
            action_id=action_id,
            last_run_at=last_run_at,
            name=name,
            status=status,
            workflow_id=workflow_id,
        )

        service_install_healthcheck.additional_properties = d
        return service_install_healthcheck

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
