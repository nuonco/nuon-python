from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
    from ..models.plantypes_helm_deploy_plan import PlantypesHelmDeployPlan
    from ..models.plantypes_kubernetes_manifest_deploy_plan import PlantypesKubernetesManifestDeployPlan
    from ..models.plantypes_noop_deploy_plan import PlantypesNoopDeployPlan
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode
    from ..models.plantypes_terraform_deploy_plan import PlantypesTerraformDeployPlan


T = TypeVar("T", bound="PlantypesDeployPlan")


@_attrs_define
class PlantypesDeployPlan:
    """
    Attributes:
        src_registry (ConfigsOCIRegistryRepository):
        src_tag (str):
        app_config_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        apply_plan_contents (Union[Unset, str]): The following field is for applying a plan that is already save
        apply_plan_display (Union[Unset, str]): This field is for storing a human legible plan or corollary
            representation
        component_id (Union[Unset, str]):
        component_name (Union[Unset, str]):
        helm (Union[Unset, PlantypesHelmDeployPlan]):
        install_id (Union[Unset, str]):
        kubernetes_manifest (Union[Unset, PlantypesKubernetesManifestDeployPlan]):
        noop (Union[Unset, PlantypesNoopDeployPlan]):
        sandbox_mode (Union[Unset, PlantypesSandboxMode]):
        terraform (Union[Unset, PlantypesTerraformDeployPlan]):
    """

    src_registry: "ConfigsOCIRegistryRepository"
    src_tag: str
    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    apply_plan_contents: Union[Unset, str] = UNSET
    apply_plan_display: Union[Unset, str] = UNSET
    component_id: Union[Unset, str] = UNSET
    component_name: Union[Unset, str] = UNSET
    helm: Union[Unset, "PlantypesHelmDeployPlan"] = UNSET
    install_id: Union[Unset, str] = UNSET
    kubernetes_manifest: Union[Unset, "PlantypesKubernetesManifestDeployPlan"] = UNSET
    noop: Union[Unset, "PlantypesNoopDeployPlan"] = UNSET
    sandbox_mode: Union[Unset, "PlantypesSandboxMode"] = UNSET
    terraform: Union[Unset, "PlantypesTerraformDeployPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_registry = self.src_registry.to_dict()

        src_tag = self.src_tag

        app_config_id = self.app_config_id

        app_id = self.app_id

        apply_plan_contents = self.apply_plan_contents

        apply_plan_display = self.apply_plan_display

        component_id = self.component_id

        component_name = self.component_name

        helm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        install_id = self.install_id

        kubernetes_manifest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kubernetes_manifest, Unset):
            kubernetes_manifest = self.kubernetes_manifest.to_dict()

        noop: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.noop, Unset):
            noop = self.noop.to_dict()

        sandbox_mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        terraform: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.terraform, Unset):
            terraform = self.terraform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "src_registry": src_registry,
                "src_tag": src_tag,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if apply_plan_contents is not UNSET:
            field_dict["apply_plan_contents"] = apply_plan_contents
        if apply_plan_display is not UNSET:
            field_dict["apply_plan_display"] = apply_plan_display
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if helm is not UNSET:
            field_dict["helm"] = helm
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if kubernetes_manifest is not UNSET:
            field_dict["kubernetes_manifest"] = kubernetes_manifest
        if noop is not UNSET:
            field_dict["noop"] = noop
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if terraform is not UNSET:
            field_dict["terraform"] = terraform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
        from ..models.plantypes_helm_deploy_plan import PlantypesHelmDeployPlan
        from ..models.plantypes_kubernetes_manifest_deploy_plan import PlantypesKubernetesManifestDeployPlan
        from ..models.plantypes_noop_deploy_plan import PlantypesNoopDeployPlan
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode
        from ..models.plantypes_terraform_deploy_plan import PlantypesTerraformDeployPlan

        d = dict(src_dict)
        src_registry = ConfigsOCIRegistryRepository.from_dict(d.pop("src_registry"))

        src_tag = d.pop("src_tag")

        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        apply_plan_contents = d.pop("apply_plan_contents", UNSET)

        apply_plan_display = d.pop("apply_plan_display", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        _helm = d.pop("helm", UNSET)
        helm: Union[Unset, PlantypesHelmDeployPlan]
        if isinstance(_helm, Unset):
            helm = UNSET
        else:
            helm = PlantypesHelmDeployPlan.from_dict(_helm)

        install_id = d.pop("install_id", UNSET)

        _kubernetes_manifest = d.pop("kubernetes_manifest", UNSET)
        kubernetes_manifest: Union[Unset, PlantypesKubernetesManifestDeployPlan]
        if isinstance(_kubernetes_manifest, Unset):
            kubernetes_manifest = UNSET
        else:
            kubernetes_manifest = PlantypesKubernetesManifestDeployPlan.from_dict(_kubernetes_manifest)

        _noop = d.pop("noop", UNSET)
        noop: Union[Unset, PlantypesNoopDeployPlan]
        if isinstance(_noop, Unset):
            noop = UNSET
        else:
            noop = PlantypesNoopDeployPlan.from_dict(_noop)

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: Union[Unset, PlantypesSandboxMode]
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        _terraform = d.pop("terraform", UNSET)
        terraform: Union[Unset, PlantypesTerraformDeployPlan]
        if isinstance(_terraform, Unset):
            terraform = UNSET
        else:
            terraform = PlantypesTerraformDeployPlan.from_dict(_terraform)

        plantypes_deploy_plan = cls(
            src_registry=src_registry,
            src_tag=src_tag,
            app_config_id=app_config_id,
            app_id=app_id,
            apply_plan_contents=apply_plan_contents,
            apply_plan_display=apply_plan_display,
            component_id=component_id,
            component_name=component_name,
            helm=helm,
            install_id=install_id,
            kubernetes_manifest=kubernetes_manifest,
            noop=noop,
            sandbox_mode=sandbox_mode,
            terraform=terraform,
        )

        plantypes_deploy_plan.additional_properties = d
        return plantypes_deploy_plan

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
