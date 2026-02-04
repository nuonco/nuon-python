from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_kubernetes_manifest_build_plan_labels import PlantypesKubernetesManifestBuildPlanLabels
    from ..models.plantypes_kustomize_build_config import PlantypesKustomizeBuildConfig


T = TypeVar("T", bound="PlantypesKubernetesManifestBuildPlan")


@_attrs_define
class PlantypesKubernetesManifestBuildPlan:
    """
    Attributes:
        inline_manifest (str | Unset): InlineManifest contains the raw manifest YAML (for inline source type)
        kustomize_config (PlantypesKustomizeBuildConfig | Unset):
        kustomize_path (str | Unset): KustomizePath is the path to the kustomization directory (for kustomize source
            type)
            Relative to the repository root
        labels (PlantypesKubernetesManifestBuildPlanLabels | Unset): Labels for the OCI artifact
        source_type (str | Unset): SourceType indicates how manifests are sourced: "inline" or "kustomize"
    """

    inline_manifest: str | Unset = UNSET
    kustomize_config: PlantypesKustomizeBuildConfig | Unset = UNSET
    kustomize_path: str | Unset = UNSET
    labels: PlantypesKubernetesManifestBuildPlanLabels | Unset = UNSET
    source_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inline_manifest = self.inline_manifest

        kustomize_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kustomize_config, Unset):
            kustomize_config = self.kustomize_config.to_dict()

        kustomize_path = self.kustomize_path

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        source_type = self.source_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inline_manifest is not UNSET:
            field_dict["inline_manifest"] = inline_manifest
        if kustomize_config is not UNSET:
            field_dict["kustomize_config"] = kustomize_config
        if kustomize_path is not UNSET:
            field_dict["kustomize_path"] = kustomize_path
        if labels is not UNSET:
            field_dict["labels"] = labels
        if source_type is not UNSET:
            field_dict["source_type"] = source_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_kubernetes_manifest_build_plan_labels import PlantypesKubernetesManifestBuildPlanLabels
        from ..models.plantypes_kustomize_build_config import PlantypesKustomizeBuildConfig

        d = dict(src_dict)
        inline_manifest = d.pop("inline_manifest", UNSET)

        _kustomize_config = d.pop("kustomize_config", UNSET)
        kustomize_config: PlantypesKustomizeBuildConfig | Unset
        if isinstance(_kustomize_config, Unset):
            kustomize_config = UNSET
        else:
            kustomize_config = PlantypesKustomizeBuildConfig.from_dict(_kustomize_config)

        kustomize_path = d.pop("kustomize_path", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: PlantypesKubernetesManifestBuildPlanLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PlantypesKubernetesManifestBuildPlanLabels.from_dict(_labels)

        source_type = d.pop("source_type", UNSET)

        plantypes_kubernetes_manifest_build_plan = cls(
            inline_manifest=inline_manifest,
            kustomize_config=kustomize_config,
            kustomize_path=kustomize_path,
            labels=labels,
            source_type=source_type,
        )

        plantypes_kubernetes_manifest_build_plan.additional_properties = d
        return plantypes_kubernetes_manifest_build_plan

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
