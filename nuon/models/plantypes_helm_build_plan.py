from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_helm_repo_config import ConfigHelmRepoConfig
    from ..models.plantypes_helm_build_plan_labels import PlantypesHelmBuildPlanLabels


T = TypeVar("T", bound="PlantypesHelmBuildPlan")


@_attrs_define
class PlantypesHelmBuildPlan:
    """
    Attributes:
        helm_repo_config (Union[Unset, ConfigHelmRepoConfig]):
        labels (Union[Unset, PlantypesHelmBuildPlanLabels]):
    """

    helm_repo_config: Union[Unset, "ConfigHelmRepoConfig"] = UNSET
    labels: Union[Unset, "PlantypesHelmBuildPlanLabels"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        helm_repo_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.helm_repo_config, Unset):
            helm_repo_config = self.helm_repo_config.to_dict()

        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if helm_repo_config is not UNSET:
            field_dict["helmRepoConfig"] = helm_repo_config
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_helm_repo_config import ConfigHelmRepoConfig
        from ..models.plantypes_helm_build_plan_labels import PlantypesHelmBuildPlanLabels

        d = dict(src_dict)
        _helm_repo_config = d.pop("helmRepoConfig", UNSET)
        helm_repo_config: Union[Unset, ConfigHelmRepoConfig]
        if isinstance(_helm_repo_config, Unset):
            helm_repo_config = UNSET
        else:
            helm_repo_config = ConfigHelmRepoConfig.from_dict(_helm_repo_config)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, PlantypesHelmBuildPlanLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PlantypesHelmBuildPlanLabels.from_dict(_labels)

        plantypes_helm_build_plan = cls(
            helm_repo_config=helm_repo_config,
            labels=labels,
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
