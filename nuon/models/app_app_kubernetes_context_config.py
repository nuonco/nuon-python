from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppKubernetesContextConfig")


@_attrs_define
class AppAppKubernetesContextConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        app_kubernetes_contexts_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        source_component_id (str | Unset):
        source_component_name (str | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    app_kubernetes_contexts_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    source_component_id: str | Unset = UNSET
    source_component_name: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        app_kubernetes_contexts_config_id = self.app_kubernetes_contexts_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        name = self.name

        org_id = self.org_id

        source_component_id = self.source_component_id

        source_component_name = self.source_component_name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_kubernetes_contexts_config_id is not UNSET:
            field_dict["app_kubernetes_contexts_config_id"] = app_kubernetes_contexts_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if source_component_id is not UNSET:
            field_dict["source_component_id"] = source_component_id
        if source_component_name is not UNSET:
            field_dict["source_component_name"] = source_component_name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        app_kubernetes_contexts_config_id = d.pop("app_kubernetes_contexts_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        source_component_id = d.pop("source_component_id", UNSET)

        source_component_name = d.pop("source_component_name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_kubernetes_context_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            app_kubernetes_contexts_config_id=app_kubernetes_contexts_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            name=name,
            org_id=org_id,
            source_component_id=source_component_id,
            source_component_name=source_component_name,
            updated_at=updated_at,
        )

        app_app_kubernetes_context_config.additional_properties = d
        return app_app_kubernetes_context_config

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
