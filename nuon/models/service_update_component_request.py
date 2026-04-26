from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_update_component_request_labels import ServiceUpdateComponentRequestLabels


T = TypeVar("T", bound="ServiceUpdateComponentRequest")


@_attrs_define
class ServiceUpdateComponentRequest:
    """
    Attributes:
        name (str):
        dependencies (list[str] | Unset):
        labels (ServiceUpdateComponentRequestLabels | Unset):
        var_name (str | Unset):
    """

    name: str
    dependencies: list[str] | Unset = UNSET
    labels: ServiceUpdateComponentRequestLabels | Unset = UNSET
    var_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        var_name = self.var_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if labels is not UNSET:
            field_dict["labels"] = labels
        if var_name is not UNSET:
            field_dict["var_name"] = var_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_update_component_request_labels import ServiceUpdateComponentRequestLabels

        d = dict(src_dict)
        name = d.pop("name")

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: ServiceUpdateComponentRequestLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServiceUpdateComponentRequestLabels.from_dict(_labels)

        var_name = d.pop("var_name", UNSET)

        service_update_component_request = cls(
            name=name,
            dependencies=dependencies,
            labels=labels,
            var_name=var_name,
        )

        service_update_component_request.additional_properties = d
        return service_update_component_request

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
