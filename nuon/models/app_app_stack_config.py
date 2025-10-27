from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_stack_type import AppStackType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppStackConfig")


@_attrs_define
class AppAppStackConfig:
    """
    Attributes:
        app_config_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        runner_nested_template_url (Union[Unset, str]):
        type_ (Union[Unset, AppStackType]):
        updated_at (Union[Unset, str]):
        vpc_nested_template_url (Union[Unset, str]):
    """

    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    runner_nested_template_url: Union[Unset, str] = UNSET
    type_: Union[Unset, AppStackType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    vpc_nested_template_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        description = self.description

        id = self.id

        name = self.name

        org_id = self.org_id

        runner_nested_template_url = self.runner_nested_template_url

        type_: Union[Unset, str] = UNSET
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
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        runner_nested_template_url = d.pop("runner_nested_template_url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AppStackType]
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
