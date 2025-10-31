from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode


T = TypeVar("T", bound="PlantypesSyncOCIPlan")


@_attrs_define
class PlantypesSyncOCIPlan:
    """
    Attributes:
        dst_registry (ConfigsOCIRegistryRepository):
        dst_tag (str):
        src_registry (ConfigsOCIRegistryRepository):
        src_tag (str):
        sandbox_mode (PlantypesSandboxMode | Unset):
    """

    dst_registry: ConfigsOCIRegistryRepository
    dst_tag: str
    src_registry: ConfigsOCIRegistryRepository
    src_tag: str
    sandbox_mode: PlantypesSandboxMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dst_registry = self.dst_registry.to_dict()

        dst_tag = self.dst_tag

        src_registry = self.src_registry.to_dict()

        src_tag = self.src_tag

        sandbox_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dst_registry": dst_registry,
                "dst_tag": dst_tag,
                "src_registry": src_registry,
                "src_tag": src_tag,
            }
        )
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configs_oci_registry_repository import ConfigsOCIRegistryRepository
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode

        d = dict(src_dict)
        dst_registry = ConfigsOCIRegistryRepository.from_dict(d.pop("dst_registry"))

        dst_tag = d.pop("dst_tag")

        src_registry = ConfigsOCIRegistryRepository.from_dict(d.pop("src_registry"))

        src_tag = d.pop("src_tag")

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: PlantypesSandboxMode | Unset
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        plantypes_sync_oci_plan = cls(
            dst_registry=dst_registry,
            dst_tag=dst_tag,
            src_registry=src_registry,
            src_tag=src_tag,
            sandbox_mode=sandbox_mode,
        )

        plantypes_sync_oci_plan.additional_properties = d
        return plantypes_sync_oci_plan

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
