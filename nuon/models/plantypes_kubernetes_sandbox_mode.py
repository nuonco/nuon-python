from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlantypesKubernetesSandboxMode")


@_attrs_define
class PlantypesKubernetesSandboxMode:
    """
    Attributes:
        plan_contents (Union[Unset, str]):
        plan_display_contents (Union[Unset, str]):
    """

    plan_contents: Union[Unset, str] = UNSET
    plan_display_contents: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_contents = self.plan_contents

        plan_display_contents = self.plan_display_contents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_contents is not UNSET:
            field_dict["plan_contents"] = plan_contents
        if plan_display_contents is not UNSET:
            field_dict["plan_display_contents"] = plan_display_contents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_contents = d.pop("plan_contents", UNSET)

        plan_display_contents = d.pop("plan_display_contents", UNSET)

        plantypes_kubernetes_sandbox_mode = cls(
            plan_contents=plan_contents,
            plan_display_contents=plan_display_contents,
        )

        plantypes_kubernetes_sandbox_mode.additional_properties = d
        return plantypes_kubernetes_sandbox_mode

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
