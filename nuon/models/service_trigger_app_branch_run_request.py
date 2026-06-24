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
        config_id (str | Unset): optional - use latest if not provided
        force (bool | Unset): force run even if no changes detected
        plan_only (bool | Unset): plan-only preview mode (no apply)
        skip_builds (bool | Unset): skip builds step (e.g. rollback to existing config with existing builds)
    """

    app_config_id: str | Unset = UNSET
    config_id: str | Unset = UNSET
    force: bool | Unset = UNSET
    plan_only: bool | Unset = UNSET
    skip_builds: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        config_id = self.config_id

        force = self.force

        plan_only = self.plan_only

        skip_builds = self.skip_builds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if config_id is not UNSET:
            field_dict["config_id"] = config_id
        if force is not UNSET:
            field_dict["force"] = force
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if skip_builds is not UNSET:
            field_dict["skip_builds"] = skip_builds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        config_id = d.pop("config_id", UNSET)

        force = d.pop("force", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        skip_builds = d.pop("skip_builds", UNSET)

        service_trigger_app_branch_run_request = cls(
            app_config_id=app_config_id,
            config_id=config_id,
            force=force,
            plan_only=plan_only,
            skip_builds=skip_builds,
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
