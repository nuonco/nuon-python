from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_stack_type import AppStackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_custom_nested_stack import ConfigCustomNestedStack


T = TypeVar("T", bound="ServiceCreateAppStackConfigRequest")


@_attrs_define
class ServiceCreateAppStackConfigRequest:
    """
    Attributes:
        app_config_id (str):
        description (str):
        name (str):
        type_ (AppStackType):
        custom_nested_stacks (list[ConfigCustomNestedStack] | Unset):
        runner_nested_template_url (str | Unset):
        vpc_nested_template_url (str | Unset):
    """

    app_config_id: str
    description: str
    name: str
    type_: AppStackType
    custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
    runner_nested_template_url: str | Unset = UNSET
    vpc_nested_template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        description = self.description

        name = self.name

        type_ = self.type_.value

        custom_nested_stacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_nested_stacks, Unset):
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in self.custom_nested_stacks:
                custom_nested_stacks_item = custom_nested_stacks_item_data.to_dict()
                custom_nested_stacks.append(custom_nested_stacks_item)

        runner_nested_template_url = self.runner_nested_template_url

        vpc_nested_template_url = self.vpc_nested_template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
                "description": description,
                "name": name,
                "type": type_,
            }
        )
        if custom_nested_stacks is not UNSET:
            field_dict["custom_nested_stacks"] = custom_nested_stacks
        if runner_nested_template_url is not UNSET:
            field_dict["runner_nested_template_url"] = runner_nested_template_url
        if vpc_nested_template_url is not UNSET:
            field_dict["vpc_nested_template_url"] = vpc_nested_template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_custom_nested_stack import ConfigCustomNestedStack

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        description = d.pop("description")

        name = d.pop("name")

        type_ = AppStackType(d.pop("type"))

        _custom_nested_stacks = d.pop("custom_nested_stacks", UNSET)
        custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
        if _custom_nested_stacks is not UNSET:
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in _custom_nested_stacks:
                custom_nested_stacks_item = ConfigCustomNestedStack.from_dict(custom_nested_stacks_item_data)

                custom_nested_stacks.append(custom_nested_stacks_item)

        runner_nested_template_url = d.pop("runner_nested_template_url", UNSET)

        vpc_nested_template_url = d.pop("vpc_nested_template_url", UNSET)

        service_create_app_stack_config_request = cls(
            app_config_id=app_config_id,
            description=description,
            name=name,
            type_=type_,
            custom_nested_stacks=custom_nested_stacks,
            runner_nested_template_url=runner_nested_template_url,
            vpc_nested_template_url=vpc_nested_template_url,
        )

        service_create_app_stack_config_request.additional_properties = d
        return service_create_app_stack_config_request

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
