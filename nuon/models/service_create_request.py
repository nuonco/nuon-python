from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_cloud_connection_preset import AppCloudConnectionPreset
from ..models.service_create_request_platform import ServiceCreateRequestPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateRequest")


@_attrs_define
class ServiceCreateRequest:
    """
    Attributes:
        acr_repositories (list[str] | Unset):
        azure_registry_id (str | Unset):
        azure_registry_login_server (str | Unset):
        azure_tenant_id (str | Unset):
        default_region (str | Unset):
        ecr_repository_arns (list[str] | Unset):
        gar_repositories (list[str] | Unset):
        gcp_project_number (str | Unset):
        name (str | Unset):
        platform (ServiceCreateRequestPlatform | Unset):
        preset (AppCloudConnectionPreset | Unset):
        principal (str | Unset):
        target_id (str | Unset):
    """

    acr_repositories: list[str] | Unset = UNSET
    azure_registry_id: str | Unset = UNSET
    azure_registry_login_server: str | Unset = UNSET
    azure_tenant_id: str | Unset = UNSET
    default_region: str | Unset = UNSET
    ecr_repository_arns: list[str] | Unset = UNSET
    gar_repositories: list[str] | Unset = UNSET
    gcp_project_number: str | Unset = UNSET
    name: str | Unset = UNSET
    platform: ServiceCreateRequestPlatform | Unset = UNSET
    preset: AppCloudConnectionPreset | Unset = UNSET
    principal: str | Unset = UNSET
    target_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acr_repositories: list[str] | Unset = UNSET
        if not isinstance(self.acr_repositories, Unset):
            acr_repositories = self.acr_repositories

        azure_registry_id = self.azure_registry_id

        azure_registry_login_server = self.azure_registry_login_server

        azure_tenant_id = self.azure_tenant_id

        default_region = self.default_region

        ecr_repository_arns: list[str] | Unset = UNSET
        if not isinstance(self.ecr_repository_arns, Unset):
            ecr_repository_arns = self.ecr_repository_arns

        gar_repositories: list[str] | Unset = UNSET
        if not isinstance(self.gar_repositories, Unset):
            gar_repositories = self.gar_repositories

        gcp_project_number = self.gcp_project_number

        name = self.name

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset.value

        principal = self.principal

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acr_repositories is not UNSET:
            field_dict["acr_repositories"] = acr_repositories
        if azure_registry_id is not UNSET:
            field_dict["azure_registry_id"] = azure_registry_id
        if azure_registry_login_server is not UNSET:
            field_dict["azure_registry_login_server"] = azure_registry_login_server
        if azure_tenant_id is not UNSET:
            field_dict["azure_tenant_id"] = azure_tenant_id
        if default_region is not UNSET:
            field_dict["default_region"] = default_region
        if ecr_repository_arns is not UNSET:
            field_dict["ecr_repository_arns"] = ecr_repository_arns
        if gar_repositories is not UNSET:
            field_dict["gar_repositories"] = gar_repositories
        if gcp_project_number is not UNSET:
            field_dict["gcp_project_number"] = gcp_project_number
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if preset is not UNSET:
            field_dict["preset"] = preset
        if principal is not UNSET:
            field_dict["principal"] = principal
        if target_id is not UNSET:
            field_dict["target_id"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acr_repositories = cast(list[str], d.pop("acr_repositories", UNSET))

        azure_registry_id = d.pop("azure_registry_id", UNSET)

        azure_registry_login_server = d.pop("azure_registry_login_server", UNSET)

        azure_tenant_id = d.pop("azure_tenant_id", UNSET)

        default_region = d.pop("default_region", UNSET)

        ecr_repository_arns = cast(list[str], d.pop("ecr_repository_arns", UNSET))

        gar_repositories = cast(list[str], d.pop("gar_repositories", UNSET))

        gcp_project_number = d.pop("gcp_project_number", UNSET)

        name = d.pop("name", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ServiceCreateRequestPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ServiceCreateRequestPlatform(_platform)

        _preset = d.pop("preset", UNSET)
        preset: AppCloudConnectionPreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = AppCloudConnectionPreset(_preset)

        principal = d.pop("principal", UNSET)

        target_id = d.pop("target_id", UNSET)

        service_create_request = cls(
            acr_repositories=acr_repositories,
            azure_registry_id=azure_registry_id,
            azure_registry_login_server=azure_registry_login_server,
            azure_tenant_id=azure_tenant_id,
            default_region=default_region,
            ecr_repository_arns=ecr_repository_arns,
            gar_repositories=gar_repositories,
            gcp_project_number=gcp_project_number,
            name=name,
            platform=platform,
            preset=preset,
            principal=principal,
            target_id=target_id,
        )

        service_create_request.additional_properties = d
        return service_create_request

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
