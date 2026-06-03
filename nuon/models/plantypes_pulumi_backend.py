from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_pulumi_backend_config import PlantypesPulumiBackendConfig


T = TypeVar("T", bound="PlantypesPulumiBackend")


@_attrs_define
class PlantypesPulumiBackend:
    """
    Attributes:
        runtime (str):
        stack_name (str):
        workspace_id (str):
        config (PlantypesPulumiBackendConfig | Unset):
        pulumi_version (str | Unset):
        update_plans (bool | Unset):
    """

    runtime: str
    stack_name: str
    workspace_id: str
    config: PlantypesPulumiBackendConfig | Unset = UNSET
    pulumi_version: str | Unset = UNSET
    update_plans: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime = self.runtime

        stack_name = self.stack_name

        workspace_id = self.workspace_id

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        pulumi_version = self.pulumi_version

        update_plans = self.update_plans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runtime": runtime,
                "stack_name": stack_name,
                "workspace_id": workspace_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if pulumi_version is not UNSET:
            field_dict["pulumi_version"] = pulumi_version
        if update_plans is not UNSET:
            field_dict["update_plans"] = update_plans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_pulumi_backend_config import PlantypesPulumiBackendConfig

        d = dict(src_dict)
        runtime = d.pop("runtime")

        stack_name = d.pop("stack_name")

        workspace_id = d.pop("workspace_id")

        _config = d.pop("config", UNSET)
        config: PlantypesPulumiBackendConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PlantypesPulumiBackendConfig.from_dict(_config)

        pulumi_version = d.pop("pulumi_version", UNSET)

        update_plans = d.pop("update_plans", UNSET)

        plantypes_pulumi_backend = cls(
            runtime=runtime,
            stack_name=stack_name,
            workspace_id=workspace_id,
            config=config,
            pulumi_version=pulumi_version,
            update_plans=update_plans,
        )

        plantypes_pulumi_backend.additional_properties = d
        return plantypes_pulumi_backend

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
