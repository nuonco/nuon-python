from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_helm_repo_config import ConfigHelmRepoConfig
    from ..models.plantypes_helm_build_plan_labels import PlantypesHelmBuildPlanLabels
    from ..models.plantypes_helm_value import PlantypesHelmValue


T = TypeVar("T", bound="PlantypesHelmBuildPlan")


@_attrs_define
class PlantypesHelmBuildPlan:
    """
    Attributes:
        helm_repo_config (ConfigHelmRepoConfig | Unset):
        labels (PlantypesHelmBuildPlanLabels | Unset):
        values (list[PlantypesHelmValue] | Unset):
        values_files (list[str] | Unset):
    """

    helm_repo_config: ConfigHelmRepoConfig | Unset = UNSET
    labels: PlantypesHelmBuildPlanLabels | Unset = UNSET
    values: list[PlantypesHelmValue] | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        helm_repo_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm_repo_config, Unset):
            helm_repo_config = self.helm_repo_config.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if helm_repo_config is not UNSET:
            field_dict["helmRepoConfig"] = helm_repo_config
        if labels is not UNSET:
            field_dict["labels"] = labels
        if values is not UNSET:
            field_dict["values"] = values
        if values_files is not UNSET:
            field_dict["valuesFiles"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_helm_repo_config import ConfigHelmRepoConfig
        from ..models.plantypes_helm_build_plan_labels import PlantypesHelmBuildPlanLabels
        from ..models.plantypes_helm_value import PlantypesHelmValue

        d = dict(src_dict)
        _helm_repo_config = d.pop("helmRepoConfig", UNSET)
        helm_repo_config: ConfigHelmRepoConfig | Unset
        if isinstance(_helm_repo_config, Unset):
            helm_repo_config = UNSET
        else:
            helm_repo_config = ConfigHelmRepoConfig.from_dict(_helm_repo_config)

        _labels = d.pop("labels", UNSET)
        labels: PlantypesHelmBuildPlanLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PlantypesHelmBuildPlanLabels.from_dict(_labels)

        _values = d.pop("values", UNSET)
        values: list[PlantypesHelmValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = PlantypesHelmValue.from_dict(values_item_data)

                values.append(values_item)

        values_files = cast(list[str], d.pop("valuesFiles", UNSET))

        plantypes_helm_build_plan = cls(
            helm_repo_config=helm_repo_config,
            labels=labels,
            values=values,
            values_files=values_files,
        )

        plantypes_helm_build_plan.additional_properties = d
        return plantypes_helm_build_plan

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
