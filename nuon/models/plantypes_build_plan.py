from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
    from ..models.plantypes_container_image_pull_plan import PlantypesContainerImagePullPlan
    from ..models.plantypes_docker_build_plan import PlantypesDockerBuildPlan
    from ..models.plantypes_git_source import PlantypesGitSource
    from ..models.plantypes_helm_build_plan import PlantypesHelmBuildPlan
    from ..models.plantypes_kubernetes_manifest_build_plan import PlantypesKubernetesManifestBuildPlan
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode
    from ..models.plantypes_terraform_build_plan import PlantypesTerraformBuildPlan


T = TypeVar("T", bound="PlantypesBuildPlan")


@_attrs_define
class PlantypesBuildPlan:
    """
    Attributes:
        dst_registry (ConfigsOCIRegistryRepository):
        dst_tag (str):
        component_build_id (str | Unset):
        component_id (str | Unset):
        container_image_pull_plan (PlantypesContainerImagePullPlan | Unset):
        docker_build_plan (PlantypesDockerBuildPlan | Unset):
        git_source (PlantypesGitSource | Unset):
        helm_build_plan (PlantypesHelmBuildPlan | Unset):
        kubernetes_manifest_build_plan (PlantypesKubernetesManifestBuildPlan | Unset):
        sandbox_mode (PlantypesSandboxMode | Unset):
        terraform_build_plan (PlantypesTerraformBuildPlan | Unset):
    """

    dst_registry: ConfigsOCIRegistryRepository
    dst_tag: str
    component_build_id: str | Unset = UNSET
    component_id: str | Unset = UNSET
    container_image_pull_plan: PlantypesContainerImagePullPlan | Unset = UNSET
    docker_build_plan: PlantypesDockerBuildPlan | Unset = UNSET
    git_source: PlantypesGitSource | Unset = UNSET
    helm_build_plan: PlantypesHelmBuildPlan | Unset = UNSET
    kubernetes_manifest_build_plan: PlantypesKubernetesManifestBuildPlan | Unset = UNSET
    sandbox_mode: PlantypesSandboxMode | Unset = UNSET
    terraform_build_plan: PlantypesTerraformBuildPlan | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dst_registry = self.dst_registry.to_dict()

        dst_tag = self.dst_tag

        component_build_id = self.component_build_id

        component_id = self.component_id

        container_image_pull_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.container_image_pull_plan, Unset):
            container_image_pull_plan = self.container_image_pull_plan.to_dict()

        docker_build_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.docker_build_plan, Unset):
            docker_build_plan = self.docker_build_plan.to_dict()

        git_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_source, Unset):
            git_source = self.git_source.to_dict()

        helm_build_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm_build_plan, Unset):
            helm_build_plan = self.helm_build_plan.to_dict()

        kubernetes_manifest_build_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kubernetes_manifest_build_plan, Unset):
            kubernetes_manifest_build_plan = self.kubernetes_manifest_build_plan.to_dict()

        sandbox_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        terraform_build_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terraform_build_plan, Unset):
            terraform_build_plan = self.terraform_build_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dst_registry": dst_registry,
                "dst_tag": dst_tag,
            }
        )
        if component_build_id is not UNSET:
            field_dict["component_build_id"] = component_build_id
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if container_image_pull_plan is not UNSET:
            field_dict["container_image_pull_plan"] = container_image_pull_plan
        if docker_build_plan is not UNSET:
            field_dict["docker_build_plan"] = docker_build_plan
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if helm_build_plan is not UNSET:
            field_dict["helm_build_plan"] = helm_build_plan
        if kubernetes_manifest_build_plan is not UNSET:
            field_dict["kubernetes_manifest_build_plan"] = kubernetes_manifest_build_plan
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if terraform_build_plan is not UNSET:
            field_dict["terraform_build_plan"] = terraform_build_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
        from ..models.plantypes_container_image_pull_plan import PlantypesContainerImagePullPlan
        from ..models.plantypes_docker_build_plan import PlantypesDockerBuildPlan
        from ..models.plantypes_git_source import PlantypesGitSource
        from ..models.plantypes_helm_build_plan import PlantypesHelmBuildPlan
        from ..models.plantypes_kubernetes_manifest_build_plan import PlantypesKubernetesManifestBuildPlan
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode
        from ..models.plantypes_terraform_build_plan import PlantypesTerraformBuildPlan

        d = dict(src_dict)
        dst_registry = ConfigsOCIRegistryRepository.from_dict(d.pop("dst_registry"))

        dst_tag = d.pop("dst_tag")

        component_build_id = d.pop("component_build_id", UNSET)

        component_id = d.pop("component_id", UNSET)

        _container_image_pull_plan = d.pop("container_image_pull_plan", UNSET)
        container_image_pull_plan: PlantypesContainerImagePullPlan | Unset
        if isinstance(_container_image_pull_plan, Unset):
            container_image_pull_plan = UNSET
        else:
            container_image_pull_plan = PlantypesContainerImagePullPlan.from_dict(_container_image_pull_plan)

        _docker_build_plan = d.pop("docker_build_plan", UNSET)
        docker_build_plan: PlantypesDockerBuildPlan | Unset
        if isinstance(_docker_build_plan, Unset):
            docker_build_plan = UNSET
        else:
            docker_build_plan = PlantypesDockerBuildPlan.from_dict(_docker_build_plan)

        _git_source = d.pop("git_source", UNSET)
        git_source: PlantypesGitSource | Unset
        if isinstance(_git_source, Unset):
            git_source = UNSET
        else:
            git_source = PlantypesGitSource.from_dict(_git_source)

        _helm_build_plan = d.pop("helm_build_plan", UNSET)
        helm_build_plan: PlantypesHelmBuildPlan | Unset
        if isinstance(_helm_build_plan, Unset):
            helm_build_plan = UNSET
        else:
            helm_build_plan = PlantypesHelmBuildPlan.from_dict(_helm_build_plan)

        _kubernetes_manifest_build_plan = d.pop("kubernetes_manifest_build_plan", UNSET)
        kubernetes_manifest_build_plan: PlantypesKubernetesManifestBuildPlan | Unset
        if isinstance(_kubernetes_manifest_build_plan, Unset):
            kubernetes_manifest_build_plan = UNSET
        else:
            kubernetes_manifest_build_plan = PlantypesKubernetesManifestBuildPlan.from_dict(
                _kubernetes_manifest_build_plan
            )

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: PlantypesSandboxMode | Unset
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        _terraform_build_plan = d.pop("terraform_build_plan", UNSET)
        terraform_build_plan: PlantypesTerraformBuildPlan | Unset
        if isinstance(_terraform_build_plan, Unset):
            terraform_build_plan = UNSET
        else:
            terraform_build_plan = PlantypesTerraformBuildPlan.from_dict(_terraform_build_plan)

        plantypes_build_plan = cls(
            dst_registry=dst_registry,
            dst_tag=dst_tag,
            component_build_id=component_build_id,
            component_id=component_id,
            container_image_pull_plan=container_image_pull_plan,
            docker_build_plan=docker_build_plan,
            git_source=git_source,
            helm_build_plan=helm_build_plan,
            kubernetes_manifest_build_plan=kubernetes_manifest_build_plan,
            sandbox_mode=sandbox_mode,
            terraform_build_plan=terraform_build_plan,
        )

        plantypes_build_plan.additional_properties = d
        return plantypes_build_plan

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
