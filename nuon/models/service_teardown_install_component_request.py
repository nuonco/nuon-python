from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceTeardownInstallComponentRequest")


@_attrs_define
class ServiceTeardownInstallComponentRequest:
    """
    Attributes:
        error_behavior (Union[Unset, str]):
        plan_only (Union[Unset, bool]):
    """

    error_behavior: Union[Unset, str] = UNSET
    plan_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_behavior = self.error_behavior

        plan_only = self.plan_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_behavior is not UNSET:
            field_dict["error_behavior"] = error_behavior
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_behavior = d.pop("error_behavior", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        service_teardown_install_component_request = cls(
            error_behavior=error_behavior,
            plan_only=plan_only,
        )

        service_teardown_install_component_request.additional_properties = d
        return service_teardown_install_component_request

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
