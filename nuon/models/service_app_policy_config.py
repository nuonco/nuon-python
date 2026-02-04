from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_app_policy_engine import ConfigAppPolicyEngine
from ..models.config_app_policy_type import ConfigAppPolicyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAppPolicyConfig")


@_attrs_define
class ServiceAppPolicyConfig:
    """
    Attributes:
        contents (str):
        type_ (ConfigAppPolicyType):
        components (list[str] | Unset):
        engine (ConfigAppPolicyEngine | Unset):
    """

    contents: str
    type_: ConfigAppPolicyType
    components: list[str] | Unset = UNSET
    engine: ConfigAppPolicyEngine | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents = self.contents

        type_ = self.type_.value

        components: list[str] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components

        engine: str | Unset = UNSET
        if not isinstance(self.engine, Unset):
            engine = self.engine.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contents": contents,
                "type": type_,
            }
        )
        if components is not UNSET:
            field_dict["components"] = components
        if engine is not UNSET:
            field_dict["engine"] = engine

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contents = d.pop("contents")

        type_ = ConfigAppPolicyType(d.pop("type"))

        components = cast(list[str], d.pop("components", UNSET))

        _engine = d.pop("engine", UNSET)
        engine: ConfigAppPolicyEngine | Unset
        if isinstance(_engine, Unset):
            engine = UNSET
        else:
            engine = ConfigAppPolicyEngine(_engine)

        service_app_policy_config = cls(
            contents=contents,
            type_=type_,
            components=components,
            engine=engine,
        )

        service_app_policy_config.additional_properties = d
        return service_app_policy_config

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
