from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppKubernetesManifestComponentConfig")


@_attrs_define
class AppKubernetesManifestComponentConfig:
    """
    Attributes:
        component_config_connection_id (Union[Unset, str]): value
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        manifest (Union[Unset, str]):
        namespace (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    component_config_connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    manifest: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_config_connection_id = self.component_config_connection_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        manifest = self.manifest

        namespace = self.namespace

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        manifest = d.pop("manifest", UNSET)

        namespace = d.pop("namespace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_kubernetes_manifest_component_config = cls(
            component_config_connection_id=component_config_connection_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            manifest=manifest,
            namespace=namespace,
            updated_at=updated_at,
        )

        app_kubernetes_manifest_component_config.additional_properties = d
        return app_kubernetes_manifest_component_config

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
