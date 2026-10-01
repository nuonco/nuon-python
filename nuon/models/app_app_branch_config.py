from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch_install_group import AppAppBranchInstallGroup
    from ..models.app_app_branch_preview_config import AppAppBranchPreviewConfig
    from ..models.app_app_branch_run_config import AppAppBranchRunConfig
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
        config_number (int | Unset):
        connected_github_vcs_config (AppConnectedGithubVCSConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        ignore_changes_regex (str | Unset): IgnoreChangesRegex is an RE2 pattern matched against every changed file path
            in a git-run or git-preview run. When every changed file matches, the run is
            marked not-attempted instead of building and deploying. Empty disables the
            check, and a forced run bypasses it.
        install_groups (list[AppAppBranchInstallGroup] | Unset):
        org_id (str | Unset):
        post_deploy_runbook_ids (list[str] | Unset): PostDeployRunbookIDs are runbooks run on each install, in order,
            after its
            deploy succeeds. Distinct from RunbookIDs, which tracks the runbooks the
            branch's synced app config produced.
        preview_config (AppAppBranchPreviewConfig | Unset):
        public_git_vcs_config (AppPublicGitVCSConfig | Unset):
        run_config (AppAppBranchRunConfig | Unset):
        runbook_ids (list[str] | Unset):
        send_statuses_on_ignore (bool | Unset): SendStatusesOnIgnore posts a successful commit status when a run is
            ignored
            by IgnoreChangesRegex, so a required check does not block the pull request.
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
    ignore_changes_regex: str | Unset = UNSET
    install_groups: list[AppAppBranchInstallGroup] | Unset = UNSET
    org_id: str | Unset = UNSET
    post_deploy_runbook_ids: list[str] | Unset = UNSET
    preview_config: AppAppBranchPreviewConfig | Unset = UNSET
    public_git_vcs_config: AppPublicGitVCSConfig | Unset = UNSET
    run_config: AppAppBranchRunConfig | Unset = UNSET
    runbook_ids: list[str] | Unset = UNSET
    send_statuses_on_ignore: bool | Unset = UNSET
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

        ignore_changes_regex = self.ignore_changes_regex

        install_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.install_groups, Unset):
            install_groups = []
            for install_groups_item_data in self.install_groups:
                install_groups_item = install_groups_item_data.to_dict()
                install_groups.append(install_groups_item)

        org_id = self.org_id

        post_deploy_runbook_ids: list[str] | Unset = UNSET
        if not isinstance(self.post_deploy_runbook_ids, Unset):
            post_deploy_runbook_ids = self.post_deploy_runbook_ids

        preview_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview_config, Unset):
            preview_config = self.preview_config.to_dict()

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        run_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_config, Unset):
            run_config = self.run_config.to_dict()

        runbook_ids: list[str] | Unset = UNSET
        if not isinstance(self.runbook_ids, Unset):
            runbook_ids = self.runbook_ids

        send_statuses_on_ignore = self.send_statuses_on_ignore

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
        if ignore_changes_regex is not UNSET:
            field_dict["ignore_changes_regex"] = ignore_changes_regex
        if install_groups is not UNSET:
            field_dict["install_groups"] = install_groups
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if post_deploy_runbook_ids is not UNSET:
            field_dict["post_deploy_runbook_ids"] = post_deploy_runbook_ids
        if preview_config is not UNSET:
            field_dict["preview_config"] = preview_config
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if run_config is not UNSET:
            field_dict["run_config"] = run_config
        if runbook_ids is not UNSET:
            field_dict["runbook_ids"] = runbook_ids
        if send_statuses_on_ignore is not UNSET:
            field_dict["send_statuses_on_ignore"] = send_statuses_on_ignore
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflows is not UNSET:
            field_dict["workflows"] = workflows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch_install_group import AppAppBranchInstallGroup  # noqa: PLC0415
        from ..models.app_app_branch_preview_config import AppAppBranchPreviewConfig  # noqa: PLC0415
        from ..models.app_app_branch_run_config import AppAppBranchRunConfig  # noqa: PLC0415
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig  # noqa: PLC0415
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig  # noqa: PLC0415
        from ..models.app_workflow import AppWorkflow  # noqa: PLC0415

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

        ignore_changes_regex = d.pop("ignore_changes_regex", UNSET)

        _install_groups = d.pop("install_groups", UNSET)
        install_groups: list[AppAppBranchInstallGroup] | Unset = UNSET
        if _install_groups is not UNSET:
            install_groups = []
            for install_groups_item_data in _install_groups:
                install_groups_item = AppAppBranchInstallGroup.from_dict(install_groups_item_data)

                install_groups.append(install_groups_item)

        org_id = d.pop("org_id", UNSET)

        post_deploy_runbook_ids = cast(list[str], d.pop("post_deploy_runbook_ids", UNSET))

        _preview_config = d.pop("preview_config", UNSET)
        preview_config: AppAppBranchPreviewConfig | Unset
        if isinstance(_preview_config, Unset):
            preview_config = UNSET
        else:
            preview_config = AppAppBranchPreviewConfig.from_dict(_preview_config)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: AppPublicGitVCSConfig | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        _run_config = d.pop("run_config", UNSET)
        run_config: AppAppBranchRunConfig | Unset
        if isinstance(_run_config, Unset):
            run_config = UNSET
        else:
            run_config = AppAppBranchRunConfig.from_dict(_run_config)

        runbook_ids = cast(list[str], d.pop("runbook_ids", UNSET))

        send_statuses_on_ignore = d.pop("send_statuses_on_ignore", UNSET)

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
            ignore_changes_regex=ignore_changes_regex,
            install_groups=install_groups,
            org_id=org_id,
            post_deploy_runbook_ids=post_deploy_runbook_ids,
            preview_config=preview_config,
            public_git_vcs_config=public_git_vcs_config,
            run_config=run_config,
            runbook_ids=runbook_ids,
            send_statuses_on_ignore=send_statuses_on_ignore,
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
