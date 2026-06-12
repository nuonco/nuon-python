from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        image (str | Unset):
        previous_source_digest (str | Unset): PreviousSourceDigest is the SourceDigest of the most recent prior Active
            ComponentBuild for the same component, used by the runner as a dedup
            hint. When the resolver returns a manifest descriptor whose digest matches
            this value, the runner skips the Copy step and reports NoOp=true.

            Empty when there is no prior active build, or when the prior build has
            no SourceDigest recorded (legacy builds).
        repo_config (ConfigsOCIRegistryRepository | Unset):
        tag (str | Unset):
        update_policy (str | Unset): UpdatePolicy is an optional Masterminds-compatible semver constraint
            (e.g. "~1.25.0") propagated from the user's component config. When
            non-empty, the runner lists tags from the source registry, filters to
            those satisfying the constraint, and selects the highest matching
            tag at build time. Tag is then ignored as the source ref.

            Empty for components that don't use update_policy.
    """

    image: str | Unset = UNSET
    previous_source_digest: str | Unset = UNSET
    repo_config: ConfigsOCIRegistryRepository | Unset = UNSET
    tag: str | Unset = UNSET
    update_policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        previous_source_digest = self.previous_source_digest

        repo_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo_config, Unset):
            repo_config = self.repo_config.to_dict()

        tag = self.tag

        update_policy = self.update_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if previous_source_digest is not UNSET:
            field_dict["previous_source_digest"] = previous_source_digest
        if repo_config is not UNSET:
            field_dict["repo_config"] = repo_config
        if tag is not UNSET:
            field_dict["tag"] = tag
        if update_policy is not UNSET:
            field_dict["update_policy"] = update_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository

        d = dict(src_dict)
        image = d.pop("image", UNSET)

        previous_source_digest = d.pop("previous_source_digest", UNSET)

        _repo_config = d.pop("repo_config", UNSET)
        repo_config: ConfigsOCIRegistryRepository | Unset
        if isinstance(_repo_config, Unset):
            repo_config = UNSET
        else:
            repo_config = ConfigsOCIRegistryRepository.from_dict(_repo_config)

        tag = d.pop("tag", UNSET)

        update_policy = d.pop("update_policy", UNSET)

        plantypes_container_image_pull_plan = cls(
            image=image,
            previous_source_digest=previous_source_digest,
            repo_config=repo_config,
            tag=tag,
            update_policy=update_policy,
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
