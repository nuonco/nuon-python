from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppProposedInstall")


@_attrs_define
class AppProposedInstall:
    """
    Attributes:
        config (list[int] | Unset):
        file_path (str | Unset):
        name (str | Unset):
    """

    config: list[int] | Unset = UNSET
    file_path: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: list[int] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config

        file_path = self.file_path

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if file_path is not UNSET:
            field_dict["file_path"] = file_path
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config = cast(list[int], d.pop("config", UNSET))

        file_path = d.pop("file_path", UNSET)

        name = d.pop("name", UNSET)

        app_proposed_install = cls(
            config=config,
            file_path=file_path,
            name=name,
        )

        app_proposed_install.additional_properties = d
        return app_proposed_install

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
