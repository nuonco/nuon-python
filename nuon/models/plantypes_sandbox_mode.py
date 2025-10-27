from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_helm_sandbox_mode import PlantypesHelmSandboxMode
    from ..models.plantypes_kubernetes_sandbox_mode import PlantypesKubernetesSandboxMode
    from ..models.plantypes_sandbox_mode_outputs import PlantypesSandboxModeOutputs
    from ..models.plantypes_terraform_sandbox_mode import PlantypesTerraformSandboxMode


T = TypeVar("T", bound="PlantypesSandboxMode")


@_attrs_define
class PlantypesSandboxMode:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        helm (Union[Unset, PlantypesHelmSandboxMode]):
        kubernetes_manifest (Union[Unset, PlantypesKubernetesSandboxMode]):
        outputs (Union[Unset, PlantypesSandboxModeOutputs]):
        terraform (Union[Unset, PlantypesTerraformSandboxMode]):
    """

    enabled: Union[Unset, bool] = UNSET
    helm: Union[Unset, "PlantypesHelmSandboxMode"] = UNSET
    kubernetes_manifest: Union[Unset, "PlantypesKubernetesSandboxMode"] = UNSET
    outputs: Union[Unset, "PlantypesSandboxModeOutputs"] = UNSET
    terraform: Union[Unset, "PlantypesTerraformSandboxMode"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        helm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        kubernetes_manifest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kubernetes_manifest, Unset):
            kubernetes_manifest = self.kubernetes_manifest.to_dict()

        outputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        terraform: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.terraform, Unset):
            terraform = self.terraform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if helm is not UNSET:
            field_dict["helm"] = helm
        if kubernetes_manifest is not UNSET:
            field_dict["kubernetes_manifest"] = kubernetes_manifest
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if terraform is not UNSET:
            field_dict["terraform"] = terraform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_helm_sandbox_mode import PlantypesHelmSandboxMode
        from ..models.plantypes_kubernetes_sandbox_mode import PlantypesKubernetesSandboxMode
        from ..models.plantypes_sandbox_mode_outputs import PlantypesSandboxModeOutputs
        from ..models.plantypes_terraform_sandbox_mode import PlantypesTerraformSandboxMode

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _helm = d.pop("helm", UNSET)
        helm: Union[Unset, PlantypesHelmSandboxMode]
        if isinstance(_helm, Unset):
            helm = UNSET
        else:
            helm = PlantypesHelmSandboxMode.from_dict(_helm)

        _kubernetes_manifest = d.pop("kubernetes_manifest", UNSET)
        kubernetes_manifest: Union[Unset, PlantypesKubernetesSandboxMode]
        if isinstance(_kubernetes_manifest, Unset):
            kubernetes_manifest = UNSET
        else:
            kubernetes_manifest = PlantypesKubernetesSandboxMode.from_dict(_kubernetes_manifest)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, PlantypesSandboxModeOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = PlantypesSandboxModeOutputs.from_dict(_outputs)

        _terraform = d.pop("terraform", UNSET)
        terraform: Union[Unset, PlantypesTerraformSandboxMode]
        if isinstance(_terraform, Unset):
            terraform = UNSET
        else:
            terraform = PlantypesTerraformSandboxMode.from_dict(_terraform)

        plantypes_sandbox_mode = cls(
            enabled=enabled,
            helm=helm,
            kubernetes_manifest=kubernetes_manifest,
            outputs=outputs,
            terraform=terraform,
        )

        plantypes_sandbox_mode.additional_properties = d
        return plantypes_sandbox_mode

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
