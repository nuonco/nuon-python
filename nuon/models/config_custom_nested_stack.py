from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_custom_nested_stack_parameters import ConfigCustomNestedStackParameters


T = TypeVar("T", bound="ConfigCustomNestedStack")


@_attrs_define
class ConfigCustomNestedStack:
    """
    Attributes:
        contents (str | Unset):
        contents_hash (str | Unset):
        index (int | Unset):
        name (str | Unset):
        parameters (ConfigCustomNestedStackParameters | Unset):
        template_url (str | Unset):
    """

    contents: str | Unset = UNSET
    contents_hash: str | Unset = UNSET
    index: int | Unset = UNSET
    name: str | Unset = UNSET
    parameters: ConfigCustomNestedStackParameters | Unset = UNSET
    template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = self.contents

        contents_hash = self.contents_hash

        index = self.index

        name = self.name

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        template_url = self.template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if contents_hash is not UNSET:
            field_dict["contents_hash"] = contents_hash
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if template_url is not UNSET:
            field_dict["template_url"] = template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_custom_nested_stack_parameters import ConfigCustomNestedStackParameters

        d = dict(src_dict)
        contents = d.pop("contents", UNSET)

        contents_hash = d.pop("contents_hash", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: ConfigCustomNestedStackParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ConfigCustomNestedStackParameters.from_dict(_parameters)

        template_url = d.pop("template_url", UNSET)

        config_custom_nested_stack = cls(
            contents=contents,
            contents_hash=contents_hash,
            index=index,
            name=name,
            parameters=parameters,
            template_url=template_url,
        )

        config_custom_nested_stack.additional_properties = d
        return config_custom_nested_stack

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
