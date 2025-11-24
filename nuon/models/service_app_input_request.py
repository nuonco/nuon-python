from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_input_source import AppAppInputSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppInputRequest")


@_attrs_define
class ServiceAppInputRequest:
    """
    Attributes:
        description (str):
        display_name (str):
        group (str):
        index (int):
        default (Union[Unset, str]):
        internal (Union[Unset, bool]): New, optional fields
        required (Union[Unset, bool]):
        sensitive (Union[Unset, bool]):
        source (Union[Unset, AppAppInputSource]):
        type_ (Union[Unset, str]):
    """

    description: str
    display_name: str
    group: str
    index: int
    default: Union[Unset, str] = UNSET
    internal: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    sensitive: Union[Unset, bool] = UNSET
    source: Union[Unset, AppAppInputSource] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        group = self.group

        index = self.index

        default = self.default

        internal = self.internal

        required = self.required

        sensitive = self.sensitive

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "display_name": display_name,
                "group": group,
                "index": index,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if internal is not UNSET:
            field_dict["internal"] = internal
        if required is not UNSET:
            field_dict["required"] = required
        if sensitive is not UNSET:
            field_dict["sensitive"] = sensitive
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        display_name = d.pop("display_name")

        group = d.pop("group")

        index = d.pop("index")

        default = d.pop("default", UNSET)

        internal = d.pop("internal", UNSET)

        required = d.pop("required", UNSET)

        sensitive = d.pop("sensitive", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, AppAppInputSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AppAppInputSource(_source)

        type_ = d.pop("type", UNSET)

        service_app_input_request = cls(
            description=description,
            display_name=display_name,
            group=group,
            index=index,
            default=default,
            internal=internal,
            required=required,
            sensitive=sensitive,
            source=source,
            type_=type_,
        )

        service_app_input_request.additional_properties = d
        return service_app_input_request

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
