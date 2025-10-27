from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_config_version import AppAppConfigVersion
from ..models.service_app_config_template_type import ServiceAppConfigTemplateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppConfigTemplate")


@_attrs_define
class ServiceAppConfigTemplate:
    """
    Attributes:
        content (Union[Unset, str]):
        filename (Union[Unset, str]):
        format_ (Union[Unset, AppAppConfigVersion]):
        type_ (Union[Unset, ServiceAppConfigTemplateType]):
    """

    content: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    format_: Union[Unset, AppAppConfigVersion] = UNSET
    type_: Union[Unset, ServiceAppConfigTemplateType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        filename = self.filename

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if filename is not UNSET:
            field_dict["filename"] = filename
        if format_ is not UNSET:
            field_dict["format"] = format_
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        filename = d.pop("filename", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, AppAppConfigVersion]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = AppAppConfigVersion(_format_)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ServiceAppConfigTemplateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServiceAppConfigTemplateType(_type_)

        service_app_config_template = cls(
            content=content,
            filename=filename,
            format_=format_,
            type_=type_,
        )

        service_app_config_template.additional_properties = d
        return service_app_config_template

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
