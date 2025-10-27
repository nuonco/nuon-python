from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
        labels (Union[Unset, PlantypesTerraformBuildPlanLabels]):
    """

    labels: Union[Unset, "PlantypesTerraformBuildPlanLabels"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_terraform_build_plan_labels import PlantypesTerraformBuildPlanLabels

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, PlantypesTerraformBuildPlanLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PlantypesTerraformBuildPlanLabels.from_dict(_labels)

        plantypes_terraform_build_plan = cls(
            labels=labels,
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
