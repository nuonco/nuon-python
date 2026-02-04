from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode


T = TypeVar("T", bound="PlantypesFetchImageMetadataPlan")


@_attrs_define
class PlantypesFetchImageMetadataPlan:
    """
    Attributes:
        registry (ConfigsOCIRegistryRepository):
        tag (str): Tag is the image tag to fetch metadata for
        include_attestation_layers (bool | Unset):
        include_attestation_manifests (bool | Unset):
        include_index (bool | Unset): Options for metadata fetching
        sandbox_mode (PlantypesSandboxMode | Unset):
    """

    registry: ConfigsOCIRegistryRepository
    tag: str
    include_attestation_layers: bool | Unset = UNSET
    include_attestation_manifests: bool | Unset = UNSET
    include_index: bool | Unset = UNSET
    sandbox_mode: PlantypesSandboxMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registry = self.registry.to_dict()

        tag = self.tag

        include_attestation_layers = self.include_attestation_layers

        include_attestation_manifests = self.include_attestation_manifests

        include_index = self.include_index

        sandbox_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registry": registry,
                "tag": tag,
            }
        )
        if include_attestation_layers is not UNSET:
            field_dict["include_attestation_layers"] = include_attestation_layers
        if include_attestation_manifests is not UNSET:
            field_dict["include_attestation_manifests"] = include_attestation_manifests
        if include_index is not UNSET:
            field_dict["include_index"] = include_index
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode

        d = dict(src_dict)
        registry = ConfigsOCIRegistryRepository.from_dict(d.pop("registry"))

        tag = d.pop("tag")

        include_attestation_layers = d.pop("include_attestation_layers", UNSET)

        include_attestation_manifests = d.pop("include_attestation_manifests", UNSET)

        include_index = d.pop("include_index", UNSET)

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: PlantypesSandboxMode | Unset
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        plantypes_fetch_image_metadata_plan = cls(
            registry=registry,
            tag=tag,
            include_attestation_layers=include_attestation_layers,
            include_attestation_manifests=include_attestation_manifests,
            include_index=include_index,
            sandbox_mode=sandbox_mode,
        )

        plantypes_fetch_image_metadata_plan.additional_properties = d
        return plantypes_fetch_image_metadata_plan

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
