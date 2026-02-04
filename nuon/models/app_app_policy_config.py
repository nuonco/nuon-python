from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_app_policy_engine import ConfigAppPolicyEngine
from ..models.config_app_policy_type import ConfigAppPolicyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppPolicyConfig")


@_attrs_define
class AppAppPolicyConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        app_policies_config (str | Unset):
        components (list[str] | Unset):
        contents (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        engine (ConfigAppPolicyEngine | Unset):
        id (str | Unset):
        org_id (str | Unset):
        type_ (ConfigAppPolicyType | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    app_policies_config: str | Unset = UNSET
    components: list[str] | Unset = UNSET
    contents: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    engine: ConfigAppPolicyEngine | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    type_: ConfigAppPolicyType | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        app_policies_config = self.app_policies_config

        components: list[str] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components

        contents = self.contents

        created_at = self.created_at

        created_by_id = self.created_by_id

        engine: str | Unset = UNSET
        if not isinstance(self.engine, Unset):
            engine = self.engine.value

        id = self.id

        org_id = self.org_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_policies_config is not UNSET:
            field_dict["app_policies_config"] = app_policies_config
        if components is not UNSET:
            field_dict["components"] = components
        if contents is not UNSET:
            field_dict["contents"] = contents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if engine is not UNSET:
            field_dict["engine"] = engine
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        app_policies_config = d.pop("app_policies_config", UNSET)

        components = cast(list[str], d.pop("components", UNSET))

        contents = d.pop("contents", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _engine = d.pop("engine", UNSET)
        engine: ConfigAppPolicyEngine | Unset
        if isinstance(_engine, Unset):
            engine = UNSET
        else:
            engine = ConfigAppPolicyEngine(_engine)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ConfigAppPolicyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConfigAppPolicyType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        app_app_policy_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            app_policies_config=app_policies_config,
            components=components,
            contents=contents,
            created_at=created_at,
            created_by_id=created_by_id,
            engine=engine,
            id=id,
            org_id=org_id,
            type_=type_,
            updated_at=updated_at,
        )

        app_app_policy_config.additional_properties = d
        return app_app_policy_config

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
