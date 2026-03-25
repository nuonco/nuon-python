from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_connected_github_vcs_config_request import HelpersConnectedGithubVCSConfigRequest
    from ..models.helpers_public_git_vcs_config_request import HelpersPublicGitVCSConfigRequest
    from ..models.service_install_group_request import ServiceInstallGroupRequest


T = TypeVar("T", bound="ServiceCreateAppBranchConfigRequest")


@_attrs_define
class ServiceCreateAppBranchConfigRequest:
    """
    Attributes:
        connected_github_vcs_config (HelpersConnectedGithubVCSConfigRequest | Unset):
        install_groups (list[ServiceInstallGroupRequest] | Unset):
        public_git_vcs_config (HelpersPublicGitVCSConfigRequest | Unset):
    """

    connected_github_vcs_config: HelpersConnectedGithubVCSConfigRequest | Unset = UNSET
    install_groups: list[ServiceInstallGroupRequest] | Unset = UNSET
    public_git_vcs_config: HelpersPublicGitVCSConfigRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        install_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_groups, Unset):
            install_groups = []
            for install_groups_item_data in self.install_groups:
                install_groups_item = install_groups_item_data.to_dict()
                install_groups.append(install_groups_item)

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if install_groups is not UNSET:
            field_dict["install_groups"] = install_groups
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_connected_github_vcs_config_request import HelpersConnectedGithubVCSConfigRequest
        from ..models.helpers_public_git_vcs_config_request import HelpersPublicGitVCSConfigRequest
        from ..models.service_install_group_request import ServiceInstallGroupRequest

        d = dict(src_dict)
        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: HelpersConnectedGithubVCSConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = HelpersConnectedGithubVCSConfigRequest.from_dict(_connected_github_vcs_config)

        _install_groups = d.pop("install_groups", UNSET)
        install_groups: list[ServiceInstallGroupRequest] | Unset = UNSET
        if _install_groups is not UNSET:
            install_groups = []
            for install_groups_item_data in _install_groups:
                install_groups_item = ServiceInstallGroupRequest.from_dict(install_groups_item_data)

                install_groups.append(install_groups_item)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: HelpersPublicGitVCSConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = HelpersPublicGitVCSConfigRequest.from_dict(_public_git_vcs_config)

        service_create_app_branch_config_request = cls(
            connected_github_vcs_config=connected_github_vcs_config,
            install_groups=install_groups,
            public_git_vcs_config=public_git_vcs_config,
        )

        service_create_app_branch_config_request.additional_properties = d
        return service_create_app_branch_config_request

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
