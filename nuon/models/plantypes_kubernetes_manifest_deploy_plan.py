from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kube_cluster_info import KubeClusterInfo
    from ..models.plantypes_oci_artifact_reference import PlantypesOCIArtifactReference


T = TypeVar("T", bound="PlantypesKubernetesManifestDeployPlan")


@_attrs_define
class PlantypesKubernetesManifestDeployPlan:
    """
    Attributes:
        cluster_info (KubeClusterInfo | Unset):
        manifest (str | Unset): Manifest is populated at runtime from the OCI artifact.
            This field is no longer set during plan creation - it's populated by the runner
            after pulling the OCI artifact during Initialize().
        namespace (str | Unset):
        oci_artifact (PlantypesOCIArtifactReference | Unset):
    """

    cluster_info: KubeClusterInfo | Unset = UNSET
    manifest: str | Unset = UNSET
    namespace: str | Unset = UNSET
    oci_artifact: PlantypesOCIArtifactReference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        manifest = self.manifest

        namespace = self.namespace

        oci_artifact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oci_artifact, Unset):
            oci_artifact = self.oci_artifact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if oci_artifact is not UNSET:
            field_dict["oci_artifact"] = oci_artifact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kube_cluster_info import KubeClusterInfo
        from ..models.plantypes_oci_artifact_reference import PlantypesOCIArtifactReference

        d = dict(src_dict)
        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: KubeClusterInfo | Unset
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        manifest = d.pop("manifest", UNSET)

        namespace = d.pop("namespace", UNSET)

        _oci_artifact = d.pop("oci_artifact", UNSET)
        oci_artifact: PlantypesOCIArtifactReference | Unset
        if isinstance(_oci_artifact, Unset):
            oci_artifact = UNSET
        else:
            oci_artifact = PlantypesOCIArtifactReference.from_dict(_oci_artifact)

        plantypes_kubernetes_manifest_deploy_plan = cls(
            cluster_info=cluster_info,
            manifest=manifest,
            namespace=namespace,
            oci_artifact=oci_artifact,
        )

        plantypes_kubernetes_manifest_deploy_plan.additional_properties = d
        return plantypes_kubernetes_manifest_deploy_plan

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
