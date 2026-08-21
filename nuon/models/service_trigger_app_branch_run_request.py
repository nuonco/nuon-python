from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceTriggerAppBranchRunRequest")


@_attrs_define
class ServiceTriggerAppBranchRunRequest:
    """
    Attributes:
        app_config_id (str | Unset): optional - use pre-existing app config (skips VCS fetch + config parse)
        auto_approve (bool | Unset): AutoApprove skips the approval gate on the plan steps. Without it the
            approval option is derived from the installs the branch targets.
        base_branch (str | Unset):
        config_id (str | Unset): optional - use latest if not provided
        force (bool | Unset): force run even if no changes detected
        head_sha (str | Unset):
        plan_only (bool | Unset): plan-only preview mode (no apply)
        pr_number (int | Unset): PR context, for previews triggered from CI rather than a GitHub webhook.
            Supplying PRNumber is what lets the run report back onto the pull request.
        skip_builds (bool | Unset): skip builds step (e.g. rollback to existing config with existing builds)
        sync_app_config (bool | Unset): SyncAppConfig syncs AppConfigID inside the run rather than assuming it was
            already synced. Set by callers that compiled the config themselves, such
            as `nuon apps sync`.
    """

    app_config_id: str | Unset = UNSET
    auto_approve: bool | Unset = UNSET
    base_branch: str | Unset = UNSET
    config_id: str | Unset = UNSET
    force: bool | Unset = UNSET
    head_sha: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    pr_number: int | Unset = UNSET
    skip_builds: bool | Unset = UNSET
    sync_app_config: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        auto_approve = self.auto_approve

        base_branch = self.base_branch

        config_id = self.config_id

        force = self.force

        head_sha = self.head_sha

        plan_only = self.plan_only

        pr_number = self.pr_number

        skip_builds = self.skip_builds

        sync_app_config = self.sync_app_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if auto_approve is not UNSET:
            field_dict["auto_approve"] = auto_approve
        if base_branch is not UNSET:
            field_dict["base_branch"] = base_branch
        if config_id is not UNSET:
            field_dict["config_id"] = config_id
        if force is not UNSET:
            field_dict["force"] = force
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if pr_number is not UNSET:
            field_dict["pr_number"] = pr_number
        if skip_builds is not UNSET:
            field_dict["skip_builds"] = skip_builds
        if sync_app_config is not UNSET:
            field_dict["sync_app_config"] = sync_app_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        auto_approve = d.pop("auto_approve", UNSET)

        base_branch = d.pop("base_branch", UNSET)

        config_id = d.pop("config_id", UNSET)

        force = d.pop("force", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        pr_number = d.pop("pr_number", UNSET)

        skip_builds = d.pop("skip_builds", UNSET)

        sync_app_config = d.pop("sync_app_config", UNSET)

        service_trigger_app_branch_run_request = cls(
            app_config_id=app_config_id,
            auto_approve=auto_approve,
            base_branch=base_branch,
            config_id=config_id,
            force=force,
            head_sha=head_sha,
            plan_only=plan_only,
            pr_number=pr_number,
            skip_builds=skip_builds,
            sync_app_config=sync_app_config,
        )

        service_trigger_app_branch_run_request.additional_properties = d
        return service_trigger_app_branch_run_request

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
