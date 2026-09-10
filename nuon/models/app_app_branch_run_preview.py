from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_branch_run_preview_mode import AppAppBranchRunPreviewMode
from ..models.app_app_branch_run_preview_source import AppAppBranchRunPreviewSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch_preview_config import AppAppBranchPreviewConfig
    from ..models.app_app_branch_preview_override import AppAppBranchPreviewOverride


T = TypeVar("T", bound="AppAppBranchRunPreview")


@_attrs_define
class AppAppBranchRunPreview:
    """
    Attributes:
        app_branch_run_id (str | Unset):
        branch_preview_config (AppAppBranchPreviewConfig | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        git_ref (str | Unset):
        id (str | Unset):
        ignore_changes_regex (str | Unset):
        input_app_config_id (str | Unset):
        install_id (str | Unset):
        install_name (str | Unset):
        mode (AppAppBranchRunPreviewMode | Unset):
        org_id (str | Unset):
        override_preview_config (AppAppBranchPreviewOverride | Unset):
        resolved_preview_config (AppAppBranchPreviewConfig | Unset):
        send_statuses_on_ignore (bool | Unset):
        source (AppAppBranchRunPreviewSource | Unset):
        updated_at (str | Unset):
    """

    app_branch_run_id: str | Unset = UNSET
    branch_preview_config: AppAppBranchPreviewConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    git_ref: str | Unset = UNSET
    id: str | Unset = UNSET
    ignore_changes_regex: str | Unset = UNSET
    input_app_config_id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_name: str | Unset = UNSET
    mode: AppAppBranchRunPreviewMode | Unset = UNSET
    org_id: str | Unset = UNSET
    override_preview_config: AppAppBranchPreviewOverride | Unset = UNSET
    resolved_preview_config: AppAppBranchPreviewConfig | Unset = UNSET
    send_statuses_on_ignore: bool | Unset = UNSET
    source: AppAppBranchRunPreviewSource | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_run_id = self.app_branch_run_id

        branch_preview_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_preview_config, Unset):
            branch_preview_config = self.branch_preview_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        git_ref = self.git_ref

        id = self.id

        ignore_changes_regex = self.ignore_changes_regex

        input_app_config_id = self.input_app_config_id

        install_id = self.install_id

        install_name = self.install_name

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        org_id = self.org_id

        override_preview_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_preview_config, Unset):
            override_preview_config = self.override_preview_config.to_dict()

        resolved_preview_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_preview_config, Unset):
            resolved_preview_config = self.resolved_preview_config.to_dict()

        send_statuses_on_ignore = self.send_statuses_on_ignore

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_run_id is not UNSET:
            field_dict["app_branch_run_id"] = app_branch_run_id
        if branch_preview_config is not UNSET:
            field_dict["branch_preview_config"] = branch_preview_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if git_ref is not UNSET:
            field_dict["git_ref"] = git_ref
        if id is not UNSET:
            field_dict["id"] = id
        if ignore_changes_regex is not UNSET:
            field_dict["ignore_changes_regex"] = ignore_changes_regex
        if input_app_config_id is not UNSET:
            field_dict["input_app_config_id"] = input_app_config_id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if override_preview_config is not UNSET:
            field_dict["override_preview_config"] = override_preview_config
        if resolved_preview_config is not UNSET:
            field_dict["resolved_preview_config"] = resolved_preview_config
        if send_statuses_on_ignore is not UNSET:
            field_dict["send_statuses_on_ignore"] = send_statuses_on_ignore
        if source is not UNSET:
            field_dict["source"] = source
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch_preview_config import AppAppBranchPreviewConfig  # noqa: PLC0415
        from ..models.app_app_branch_preview_override import AppAppBranchPreviewOverride  # noqa: PLC0415

        d = dict(src_dict)
        app_branch_run_id = d.pop("app_branch_run_id", UNSET)

        _branch_preview_config = d.pop("branch_preview_config", UNSET)
        branch_preview_config: AppAppBranchPreviewConfig | Unset
        if isinstance(_branch_preview_config, Unset):
            branch_preview_config = UNSET
        else:
            branch_preview_config = AppAppBranchPreviewConfig.from_dict(_branch_preview_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        git_ref = d.pop("git_ref", UNSET)

        id = d.pop("id", UNSET)

        ignore_changes_regex = d.pop("ignore_changes_regex", UNSET)

        input_app_config_id = d.pop("input_app_config_id", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_name = d.pop("install_name", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AppAppBranchRunPreviewMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = AppAppBranchRunPreviewMode(_mode)

        org_id = d.pop("org_id", UNSET)

        _override_preview_config = d.pop("override_preview_config", UNSET)
        override_preview_config: AppAppBranchPreviewOverride | Unset
        if isinstance(_override_preview_config, Unset):
            override_preview_config = UNSET
        else:
            override_preview_config = AppAppBranchPreviewOverride.from_dict(_override_preview_config)

        _resolved_preview_config = d.pop("resolved_preview_config", UNSET)
        resolved_preview_config: AppAppBranchPreviewConfig | Unset
        if isinstance(_resolved_preview_config, Unset):
            resolved_preview_config = UNSET
        else:
            resolved_preview_config = AppAppBranchPreviewConfig.from_dict(_resolved_preview_config)

        send_statuses_on_ignore = d.pop("send_statuses_on_ignore", UNSET)

        _source = d.pop("source", UNSET)
        source: AppAppBranchRunPreviewSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AppAppBranchRunPreviewSource(_source)

        updated_at = d.pop("updated_at", UNSET)

        app_app_branch_run_preview = cls(
            app_branch_run_id=app_branch_run_id,
            branch_preview_config=branch_preview_config,
            created_at=created_at,
            created_by_id=created_by_id,
            git_ref=git_ref,
            id=id,
            ignore_changes_regex=ignore_changes_regex,
            input_app_config_id=input_app_config_id,
            install_id=install_id,
            install_name=install_name,
            mode=mode,
            org_id=org_id,
            override_preview_config=override_preview_config,
            resolved_preview_config=resolved_preview_config,
            send_statuses_on_ignore=send_statuses_on_ignore,
            source=source,
            updated_at=updated_at,
        )

        app_app_branch_run_preview.additional_properties = d
        return app_app_branch_run_preview

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
