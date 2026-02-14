from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_stack_type import AppStackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_custom_nested_stack import ConfigCustomNestedStack


T = TypeVar("T", bound="AppAppStackConfig")


@_attrs_define
class AppAppStackConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        custom_nested_stacks (list[ConfigCustomNestedStack] | Unset):
        description (str | Unset):
        id (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        runner_nested_template_url (str | Unset):
        type_ (AppStackType | Unset):
        updated_at (str | Unset):
        vpc_nested_template_url (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    runner_nested_template_url: str | Unset = UNSET
    type_: AppStackType | Unset = UNSET
    updated_at: str | Unset = UNSET
    vpc_nested_template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        custom_nested_stacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_nested_stacks, Unset):
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in self.custom_nested_stacks:
                custom_nested_stacks_item = custom_nested_stacks_item_data.to_dict()
                custom_nested_stacks.append(custom_nested_stacks_item)

        description = self.description

        id = self.id

        name = self.name

        org_id = self.org_id

        runner_nested_template_url = self.runner_nested_template_url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        vpc_nested_template_url = self.vpc_nested_template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if custom_nested_stacks is not UNSET:
            field_dict["custom_nested_stacks"] = custom_nested_stacks
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if runner_nested_template_url is not UNSET:
            field_dict["runner_nested_template_url"] = runner_nested_template_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vpc_nested_template_url is not UNSET:
            field_dict["vpc_nested_template_url"] = vpc_nested_template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_custom_nested_stack import ConfigCustomNestedStack

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _custom_nested_stacks = d.pop("custom_nested_stacks", UNSET)
        custom_nested_stacks: list[ConfigCustomNestedStack] | Unset = UNSET
        if _custom_nested_stacks is not UNSET:
            custom_nested_stacks = []
            for custom_nested_stacks_item_data in _custom_nested_stacks:
                custom_nested_stacks_item = ConfigCustomNestedStack.from_dict(custom_nested_stacks_item_data)

                custom_nested_stacks.append(custom_nested_stacks_item)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        runner_nested_template_url = d.pop("runner_nested_template_url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppStackType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppStackType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        vpc_nested_template_url = d.pop("vpc_nested_template_url", UNSET)

        app_app_stack_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            created_at=created_at,
            created_by_id=created_by_id,
            custom_nested_stacks=custom_nested_stacks,
            description=description,
            id=id,
            name=name,
            org_id=org_id,
            runner_nested_template_url=runner_nested_template_url,
            type_=type_,
            updated_at=updated_at,
            vpc_nested_template_url=vpc_nested_template_url,
        )

        app_app_stack_config.additional_properties = d
        return app_app_stack_config

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
