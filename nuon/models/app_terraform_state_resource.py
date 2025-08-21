from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_terraform_state_instance import AppTerraformStateInstance


T = TypeVar("T", bound="AppTerraformStateResource")


@_attrs_define
class AppTerraformStateResource:
    """
    Attributes:
        instances (Union[Unset, list['AppTerraformStateInstance']]):
        mode (Union[Unset, str]):
        name (Union[Unset, str]):
        provider (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    instances: Union[Unset, list["AppTerraformStateInstance"]] = UNSET
    mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        mode = self.mode

        name = self.name

        provider = self.provider

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instances is not UNSET:
            field_dict["instances"] = instances
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_terraform_state_instance import AppTerraformStateInstance

        d = dict(src_dict)
        instances = []
        _instances = d.pop("instances", UNSET)
        for instances_item_data in _instances or []:
            instances_item = AppTerraformStateInstance.from_dict(instances_item_data)

            instances.append(instances_item)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        provider = d.pop("provider", UNSET)

        type_ = d.pop("type", UNSET)

        app_terraform_state_resource = cls(
            instances=instances,
            mode=mode,
            name=name,
            provider=provider,
            type_=type_,
        )

        app_terraform_state_resource.additional_properties = d
        return app_terraform_state_resource

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
