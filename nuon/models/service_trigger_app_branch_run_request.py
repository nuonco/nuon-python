from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceTriggerAppBranchRunRequest")


@_attrs_define
class ServiceTriggerAppBranchRunRequest:
    """
    Attributes:
        config_id (str | Unset): optional - use latest if not provided
        force (bool | Unset): force run even if no changes detected
    """

    config_id: str | Unset = UNSET
    force: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_id = self.config_id

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_id is not UNSET:
            field_dict["config_id"] = config_id
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_id = d.pop("config_id", UNSET)

        force = d.pop("force", UNSET)

        service_trigger_app_branch_run_request = cls(
            config_id=config_id,
            force=force,
        )

        service_trigger_app_branch_run_request.additional_properties = d
        return service_trigger_app_branch_run_request

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
