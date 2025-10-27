from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository


T = TypeVar("T", bound="PlantypesContainerImagePullPlan")


@_attrs_define
class PlantypesContainerImagePullPlan:
    """
    Attributes:
        image (Union[Unset, str]):
        repo_config (Union[Unset, ConfigsOCIRegistryRepository]):
        tag (Union[Unset, str]):
    """

    image: Union[Unset, str] = UNSET
    repo_config: Union[Unset, "ConfigsOCIRegistryRepository"] = UNSET
    tag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        repo_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.repo_config, Unset):
            repo_config = self.repo_config.to_dict()

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if repo_config is not UNSET:
            field_dict["repo_config"] = repo_config
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository

        d = dict(src_dict)
        image = d.pop("image", UNSET)

        _repo_config = d.pop("repo_config", UNSET)
        repo_config: Union[Unset, ConfigsOCIRegistryRepository]
        if isinstance(_repo_config, Unset):
            repo_config = UNSET
        else:
            repo_config = ConfigsOCIRegistryRepository.from_dict(_repo_config)

        tag = d.pop("tag", UNSET)

        plantypes_container_image_pull_plan = cls(
            image=image,
            repo_config=repo_config,
            tag=tag,
        )

        plantypes_container_image_pull_plan.additional_properties = d
        return plantypes_container_image_pull_plan

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
