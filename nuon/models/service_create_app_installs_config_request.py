from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_create_app_installs_config_request_vcs_type import ServiceCreateAppInstallsConfigRequestVcsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateAppInstallsConfigRequest")


@_attrs_define
class ServiceCreateAppInstallsConfigRequest:
    """
    Attributes:
        branch (str):
        repo (str):
        vcs_type (ServiceCreateAppInstallsConfigRequestVcsType):
        directory (str | Unset):
        vcs_connection_id (str | Unset):
    """

    branch: str
    repo: str
    vcs_type: ServiceCreateAppInstallsConfigRequestVcsType
    directory: str | Unset = UNSET
    vcs_connection_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        repo = self.repo

        vcs_type = self.vcs_type.value

        directory = self.directory

        vcs_connection_id = self.vcs_connection_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
                "repo": repo,
                "vcs_type": vcs_type,
            }
        )
        if directory is not UNSET:
            field_dict["directory"] = directory
        if vcs_connection_id is not UNSET:
            field_dict["vcs_connection_id"] = vcs_connection_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch")

        repo = d.pop("repo")

        vcs_type = ServiceCreateAppInstallsConfigRequestVcsType(d.pop("vcs_type"))

        directory = d.pop("directory", UNSET)

        vcs_connection_id = d.pop("vcs_connection_id", UNSET)

        service_create_app_installs_config_request = cls(
            branch=branch,
            repo=repo,
            vcs_type=vcs_type,
            directory=directory,
            vcs_connection_id=vcs_connection_id,
        )

        service_create_app_installs_config_request.additional_properties = d
        return service_create_app_installs_config_request

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
