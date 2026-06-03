from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppSecretKubernetesSyncTarget")


@_attrs_define
class AppAppSecretKubernetesSyncTarget:
    """
    Attributes:
        app_secret_config_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        key (str | Unset):
        name (str | Unset):
        namespaces (list[str] | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    app_secret_config_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    namespaces: list[str] | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_secret_config_id = self.app_secret_config_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        key = self.key

        name = self.name

        namespaces: list[str] | Unset = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_secret_config_id is not UNSET:
            field_dict["app_secret_config_id"] = app_secret_config_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if namespaces is not UNSET:
            field_dict["namespaces"] = namespaces
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_secret_config_id = d.pop("app_secret_config_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        namespaces = cast(list[str], d.pop("namespaces", UNSET))

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_secret_kubernetes_sync_target = cls(
            app_secret_config_id=app_secret_config_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            key=key,
            name=name,
            namespaces=namespaces,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_app_secret_kubernetes_sync_target.additional_properties = d
        return app_app_secret_kubernetes_sync_target

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
