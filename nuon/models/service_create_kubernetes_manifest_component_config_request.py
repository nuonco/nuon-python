from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateKubernetesManifestComponentConfigRequest")


@_attrs_define
class ServiceCreateKubernetesManifestComponentConfigRequest:
    """
    Attributes:
        app_config_id (str | Unset):
        checksum (str | Unset):
        dependencies (list[str] | Unset):
        drift_schedule (str | Unset):
        manifest (str | Unset):
        namespace (str | Unset):
        references (list[str] | Unset):
    """

    app_config_id: str | Unset = UNSET
    checksum: str | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    manifest: str | Unset = UNSET
    namespace: str | Unset = UNSET
    references: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        checksum = self.checksum

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        drift_schedule = self.drift_schedule

        manifest = self.manifest

        namespace = self.namespace

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        checksum = d.pop("checksum", UNSET)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        drift_schedule = d.pop("drift_schedule", UNSET)

        manifest = d.pop("manifest", UNSET)

        namespace = d.pop("namespace", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        service_create_kubernetes_manifest_component_config_request = cls(
            app_config_id=app_config_id,
            checksum=checksum,
            dependencies=dependencies,
            drift_schedule=drift_schedule,
            manifest=manifest,
            namespace=namespace,
            references=references,
        )

        service_create_kubernetes_manifest_component_config_request.additional_properties = d
        return service_create_kubernetes_manifest_component_config_request

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
