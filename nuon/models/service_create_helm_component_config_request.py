from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
    from ..models.service_create_helm_component_config_request_values import (
        ServiceCreateHelmComponentConfigRequestValues,
    )
    from ..models.service_helm_repo_config_request import ServiceHelmRepoConfigRequest
    from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest


T = TypeVar("T", bound="ServiceCreateHelmComponentConfigRequest")


@_attrs_define
class ServiceCreateHelmComponentConfigRequest:
    """
    Attributes:
        chart_name (str):
        values (ServiceCreateHelmComponentConfigRequestValues):
        app_config_id (str | Unset):
        checksum (str | Unset):
        connected_github_vcs_config (ServiceConnectedGithubVCSConfigRequest | Unset):
        dependencies (list[str] | Unset):
        drift_schedule (str | Unset):
        helm_repo_config (ServiceHelmRepoConfigRequest | Unset):
        namespace (str | Unset):
        public_git_vcs_config (ServicePublicGitVCSConfigRequest | Unset):
        references (list[str] | Unset):
        storage_driver (str | Unset):
        take_ownership (bool | Unset):
        values_files (list[str] | Unset):
    """

    chart_name: str
    values: ServiceCreateHelmComponentConfigRequestValues
    app_config_id: str | Unset = UNSET
    checksum: str | Unset = UNSET
    connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    drift_schedule: str | Unset = UNSET
    helm_repo_config: ServiceHelmRepoConfigRequest | Unset = UNSET
    namespace: str | Unset = UNSET
    public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset = UNSET
    references: list[str] | Unset = UNSET
    storage_driver: str | Unset = UNSET
    take_ownership: bool | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chart_name = self.chart_name

        values = self.values.to_dict()

        app_config_id = self.app_config_id

        checksum = self.checksum

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        drift_schedule = self.drift_schedule

        helm_repo_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm_repo_config, Unset):
            helm_repo_config = self.helm_repo_config.to_dict()

        namespace = self.namespace

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        storage_driver = self.storage_driver

        take_ownership = self.take_ownership

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chart_name": chart_name,
                "values": values,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if drift_schedule is not UNSET:
            field_dict["drift_schedule"] = drift_schedule
        if helm_repo_config is not UNSET:
            field_dict["helm_repo_config"] = helm_repo_config
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references
        if storage_driver is not UNSET:
            field_dict["storage_driver"] = storage_driver
        if take_ownership is not UNSET:
            field_dict["take_ownership"] = take_ownership
        if values_files is not UNSET:
            field_dict["values_files"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_connected_github_vcs_config_request import ServiceConnectedGithubVCSConfigRequest
        from ..models.service_create_helm_component_config_request_values import (
            ServiceCreateHelmComponentConfigRequestValues,
        )
        from ..models.service_helm_repo_config_request import ServiceHelmRepoConfigRequest
        from ..models.service_public_git_vcs_config_request import ServicePublicGitVCSConfigRequest

        d = dict(src_dict)
        chart_name = d.pop("chart_name")

        values = ServiceCreateHelmComponentConfigRequestValues.from_dict(d.pop("values"))

        app_config_id = d.pop("app_config_id", UNSET)

        checksum = d.pop("checksum", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: ServiceConnectedGithubVCSConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        drift_schedule = d.pop("drift_schedule", UNSET)

        _helm_repo_config = d.pop("helm_repo_config", UNSET)
        helm_repo_config: ServiceHelmRepoConfigRequest | Unset
        if isinstance(_helm_repo_config, Unset):
            helm_repo_config = UNSET
        else:
            helm_repo_config = ServiceHelmRepoConfigRequest.from_dict(_helm_repo_config)

        namespace = d.pop("namespace", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: ServicePublicGitVCSConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = ServicePublicGitVCSConfigRequest.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        storage_driver = d.pop("storage_driver", UNSET)

        take_ownership = d.pop("take_ownership", UNSET)

        values_files = cast(list[str], d.pop("values_files", UNSET))

        service_create_helm_component_config_request = cls(
            chart_name=chart_name,
            values=values,
            app_config_id=app_config_id,
            checksum=checksum,
            connected_github_vcs_config=connected_github_vcs_config,
            dependencies=dependencies,
            drift_schedule=drift_schedule,
            helm_repo_config=helm_repo_config,
            namespace=namespace,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
            storage_driver=storage_driver,
            take_ownership=take_ownership,
            values_files=values_files,
        )

        service_create_helm_component_config_request.additional_properties = d
        return service_create_helm_component_config_request

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
