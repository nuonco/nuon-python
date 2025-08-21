from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateComponentRequest")


@_attrs_define
class ServiceCreateComponentRequest:
    """
    Attributes:
        name (str):
        dependencies (Union[Unset, list[str]]):
        var_name (Union[Unset, str]):
    """

    name: str
    dependencies: Union[Unset, list[str]] = UNSET
    var_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        dependencies: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

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
        if var_name is not UNSET:
            field_dict["var_name"] = var_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        var_name = d.pop("var_name", UNSET)

        service_create_component_request = cls(
            name=name,
            dependencies=dependencies,
            var_name=var_name,
        )

        service_create_component_request.additional_properties = d
        return service_create_component_request

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
