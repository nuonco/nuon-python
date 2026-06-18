from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateInstallAppConfigUpdateRequest")


@_attrs_define
class ServiceCreateInstallAppConfigUpdateRequest:
    """
    Attributes:
        app_config_id (str):
        plan_only (bool | Unset):
    """

    app_config_id: str
    plan_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        plan_only = self.plan_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
            }
        )
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        plan_only = d.pop("plan_only", UNSET)

        service_create_install_app_config_update_request = cls(
            app_config_id=app_config_id,
            plan_only=plan_only,
        )

        service_create_install_app_config_update_request.additional_properties = d
        return service_create_install_app_config_update_request

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
