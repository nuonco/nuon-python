from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_custom_nested_stack_status import ConfigCustomNestedStackStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigUploadedUIDefinition")


@_attrs_define
class ConfigUploadedUIDefinition:
    """
    Attributes:
        contents (str | Unset):
        contents_hash (str | Unset):
        path (str | Unset):
        source_url (str | Unset):
        status (ConfigCustomNestedStackStatus | Unset):
    """

    contents: str | Unset = UNSET
    contents_hash: str | Unset = UNSET
    path: str | Unset = UNSET
    source_url: str | Unset = UNSET
    status: ConfigCustomNestedStackStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = self.contents

        contents_hash = self.contents_hash

        path = self.path

        source_url = self.source_url

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if contents_hash is not UNSET:
            field_dict["contents_hash"] = contents_hash
        if path is not UNSET:
            field_dict["path"] = path
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contents = d.pop("contents", UNSET)

        contents_hash = d.pop("contents_hash", UNSET)

        path = d.pop("path", UNSET)

        source_url = d.pop("source_url", UNSET)

        _status = d.pop("status", UNSET)
        status: ConfigCustomNestedStackStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConfigCustomNestedStackStatus(_status)

        config_uploaded_ui_definition = cls(
            contents=contents,
            contents_hash=contents_hash,
            path=path,
            source_url=source_url,
            status=status,
        )

        config_uploaded_ui_definition.additional_properties = d
        return config_uploaded_ui_definition

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
