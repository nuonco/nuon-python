from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kube_cluster_info import KubeClusterInfo


T = TypeVar("T", bound="PlantypesKubernetesManifestDeployPlan")


@_attrs_define
class PlantypesKubernetesManifestDeployPlan:
    """
    Attributes:
        cluster_info (Union[Unset, KubeClusterInfo]):
        manifest (Union[Unset, str]):
        namespace (Union[Unset, str]):
    """

    cluster_info: Union[Unset, "KubeClusterInfo"] = UNSET
    manifest: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        manifest = self.manifest

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kube_cluster_info import KubeClusterInfo

        d = dict(src_dict)
        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: Union[Unset, KubeClusterInfo]
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        manifest = d.pop("manifest", UNSET)

        namespace = d.pop("namespace", UNSET)

        plantypes_kubernetes_manifest_deploy_plan = cls(
            cluster_info=cluster_info,
            manifest=manifest,
            namespace=namespace,
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
