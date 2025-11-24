from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_input_group import AppAppInputGroup


T = TypeVar("T", bound="AppAppInput")


@_attrs_define
class AppAppInput:
    """
    Attributes:
        app_input_id (Union[Unset, str]):
        cloudformation_stack_name (Union[Unset, str]): CloudFormation configuration (computed fields, not stored in DB)
        cloudformation_stack_parameter_name (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        default (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        group (Union[Unset, AppAppInputGroup]):
        group_id (Union[Unset, str]):
        id (Union[Unset, str]):
        index (Union[Unset, int]):
        internal (Union[Unset, bool]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        required (Union[Unset, bool]):
        sensitive (Union[Unset, bool]):
        source (Union[Unset, str]):
        type_ (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    app_input_id: Union[Unset, str] = UNSET
    cloudformation_stack_name: Union[Unset, str] = UNSET
    cloudformation_stack_parameter_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    default: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    group: Union[Unset, "AppAppInputGroup"] = UNSET
    group_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    index: Union[Unset, int] = UNSET
    internal: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    sensitive: Union[Unset, bool] = UNSET
    source: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_input_id = self.app_input_id

        cloudformation_stack_name = self.cloudformation_stack_name

        cloudformation_stack_parameter_name = self.cloudformation_stack_parameter_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        default = self.default

        description = self.description

        display_name = self.display_name

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        group_id = self.group_id

        id = self.id

        index = self.index

        internal = self.internal

        name = self.name

        org_id = self.org_id

        required = self.required

        sensitive = self.sensitive

        source = self.source

        type_ = self.type_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_input_id is not UNSET:
            field_dict["app_input_id"] = app_input_id
        if cloudformation_stack_name is not UNSET:
            field_dict["cloudformation_stack_name"] = cloudformation_stack_name
        if cloudformation_stack_parameter_name is not UNSET:
            field_dict["cloudformation_stack_parameter_name"] = cloudformation_stack_parameter_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if group is not UNSET:
            field_dict["group"] = group
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if internal is not UNSET:
            field_dict["internal"] = internal
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if required is not UNSET:
            field_dict["required"] = required
        if sensitive is not UNSET:
            field_dict["sensitive"] = sensitive
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_input_group import AppAppInputGroup

        d = dict(src_dict)
        app_input_id = d.pop("app_input_id", UNSET)

        cloudformation_stack_name = d.pop("cloudformation_stack_name", UNSET)

        cloudformation_stack_parameter_name = d.pop("cloudformation_stack_parameter_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, AppAppInputGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = AppAppInputGroup.from_dict(_group)

        group_id = d.pop("group_id", UNSET)

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        internal = d.pop("internal", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        required = d.pop("required", UNSET)

        sensitive = d.pop("sensitive", UNSET)

        source = d.pop("source", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_input = cls(
            app_input_id=app_input_id,
            cloudformation_stack_name=cloudformation_stack_name,
            cloudformation_stack_parameter_name=cloudformation_stack_parameter_name,
            created_at=created_at,
            created_by_id=created_by_id,
            default=default,
            description=description,
            display_name=display_name,
            group=group,
            group_id=group_id,
            id=id,
            index=index,
            internal=internal,
            name=name,
            org_id=org_id,
            required=required,
            sensitive=sensitive,
            source=source,
            type_=type_,
            updated_at=updated_at,
        )

        app_app_input.additional_properties = d
        return app_app_input

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
