from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_terraform_build_plan_labels import PlantypesTerraformBuildPlanLabels


T = TypeVar("T", bound="PlantypesTerraformBuildPlan")


@_attrs_define
class PlantypesTerraformBuildPlan:
    """
    Attributes:
        labels (PlantypesTerraformBuildPlanLabels | Unset):
        terraform_version (str | Unset): TerraformVersion is the version of the terraform CLI the build runner
            should install in order to vendor providers via
            `terraform providers mirror`. When empty the build runner falls back
            to a sane default. Should mirror the version configured for the
            component's deploy plan so init resolves the same provider bytes the
            build vendored. Only consulted when VendorProviders is true.
        vendor_providers (bool | Unset): VendorProviders enables build-time vendoring of terraform providers
            via `terraform providers mirror`. Gated by the
            `terraform-provider-mirror` org feature flag in ctl-api so we can
            roll the change out gradually without coupling install-runner
            behaviour to the flag (the install runner auto-detects whether a
            mirror is present in the OCI artifact).
    """

    labels: PlantypesTerraformBuildPlanLabels | Unset = UNSET
    terraform_version: str | Unset = UNSET
    vendor_providers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        terraform_version = self.terraform_version

        vendor_providers = self.vendor_providers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if terraform_version is not UNSET:
            field_dict["terraform_version"] = terraform_version
        if vendor_providers is not UNSET:
            field_dict["vendor_providers"] = vendor_providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_terraform_build_plan_labels import PlantypesTerraformBuildPlanLabels

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: PlantypesTerraformBuildPlanLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PlantypesTerraformBuildPlanLabels.from_dict(_labels)

        terraform_version = d.pop("terraform_version", UNSET)

        vendor_providers = d.pop("vendor_providers", UNSET)

        plantypes_terraform_build_plan = cls(
            labels=labels,
            terraform_version=terraform_version,
            vendor_providers=vendor_providers,
        )

        plantypes_terraform_build_plan.additional_properties = d
        return plantypes_terraform_build_plan

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
