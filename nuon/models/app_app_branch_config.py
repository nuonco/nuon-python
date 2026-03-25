from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch_install_group import AppAppBranchInstallGroup
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig
    from ..models.app_workflow import AppWorkflow


T = TypeVar("T", bound="AppAppBranchConfig")


@_attrs_define
class AppAppBranchConfig:
    """
    Attributes:
        action_ids (list[str] | Unset):
        app_branch_id (str | Unset):
        component_ids (list[str] | Unset):
        config_number (int | Unset): generated view field
        connected_github_vcs_config (AppConnectedGithubVCSConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        install_groups (list[AppAppBranchInstallGroup] | Unset):
        org_id (str | Unset):
        public_git_vcs_config (AppPublicGitVCSConfig | Unset):
        updated_at (str | Unset):
        workflows (list[AppWorkflow] | Unset):
    """

    action_ids: list[str] | Unset = UNSET
    app_branch_id: str | Unset = UNSET
    component_ids: list[str] | Unset = UNSET
    config_number: int | Unset = UNSET
    connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    install_groups: list[AppAppBranchInstallGroup] | Unset = UNSET
    org_id: str | Unset = UNSET
    public_git_vcs_config: AppPublicGitVCSConfig | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflows: list[AppWorkflow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_ids: list[str] | Unset = UNSET
        if not isinstance(self.action_ids, Unset):
            action_ids = self.action_ids

        app_branch_id = self.app_branch_id

        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = self.component_ids

        config_number = self.config_number

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_groups, Unset):
            install_groups = []
            for install_groups_item_data in self.install_groups:
                install_groups_item = install_groups_item_data.to_dict()
                install_groups.append(install_groups_item)

        org_id = self.org_id

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        updated_at = self.updated_at

        workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_ids is not UNSET:
            field_dict["action_ids"] = action_ids
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if config_number is not UNSET:
            field_dict["config_number"] = config_number
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_groups is not UNSET:
            field_dict["install_groups"] = install_groups
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch_install_group import AppAppBranchInstallGroup
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig
        from ..models.app_workflow import AppWorkflow

        d = dict(src_dict)
        action_ids = cast(list[str], d.pop("action_ids", UNSET))

        app_branch_id = d.pop("app_branch_id", UNSET)

        component_ids = cast(list[str], d.pop("component_ids", UNSET))

        config_number = d.pop("config_number", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: AppConnectedGithubVCSConfig | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _install_groups = d.pop("install_groups", UNSET)
        install_groups: list[AppAppBranchInstallGroup] | Unset = UNSET
        if _install_groups is not UNSET:
            install_groups = []
            for install_groups_item_data in _install_groups:
                install_groups_item = AppAppBranchInstallGroup.from_dict(install_groups_item_data)

                install_groups.append(install_groups_item)

        org_id = d.pop("org_id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: AppPublicGitVCSConfig | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        updated_at = d.pop("updated_at", UNSET)

        _workflows = d.pop("workflows", UNSET)
        workflows: list[AppWorkflow] | Unset = UNSET
        if _workflows is not UNSET:
            workflows = []
            for workflows_item_data in _workflows:
                workflows_item = AppWorkflow.from_dict(workflows_item_data)

                workflows.append(workflows_item)

        app_app_branch_config = cls(
            action_ids=action_ids,
            app_branch_id=app_branch_id,
            component_ids=component_ids,
            config_number=config_number,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_groups=install_groups,
            org_id=org_id,
            public_git_vcs_config=public_git_vcs_config,
            updated_at=updated_at,
            workflows=workflows,
        )

        app_app_branch_config.additional_properties = d
        return app_app_branch_config

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
