from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_trigger_target_type import AppTriggerTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_trigger_filter import AppTriggerFilter
    from ..models.app_trigger_rule_input_mappings import AppTriggerRuleInputMappings


T = TypeVar("T", bound="AppTriggerRule")


@_attrs_define
class AppTriggerRule:
    """
    Attributes:
        app_branch_id (str | Unset):
        app_config_id (str | Unset):
        app_id (str | Unset):
        config_hash (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        enabled (bool | Unset):
        event_types (list[str] | Unset):
        filters (list[AppTriggerFilter] | Unset):
        force (bool | Unset):
        id (str | Unset):
        input_mappings (AppTriggerRuleInputMappings | Unset):
        install_name (str | Unset):
        name (str | Unset):
        org_id (str | Unset):
        plan_only (bool | Unset):
        runbook_id (str | Unset):
        suspended_at (str | Unset):
        suspended_by_id (str | Unset):
        target_type (AppTriggerTargetType | Unset):
        trigger_id (str | Unset):
        updated_at (str | Unset):
        valid_from (str | Unset):
        valid_to (str | Unset):
    """

    app_branch_id: str | Unset = UNSET
    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    config_hash: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    filters: list[AppTriggerFilter] | Unset = UNSET
    force: bool | Unset = UNSET
    id: str | Unset = UNSET
    input_mappings: AppTriggerRuleInputMappings | Unset = UNSET
    install_name: str | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    plan_only: bool | Unset = UNSET
    runbook_id: str | Unset = UNSET
    suspended_at: str | Unset = UNSET
    suspended_by_id: str | Unset = UNSET
    target_type: AppTriggerTargetType | Unset = UNSET
    trigger_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    valid_from: str | Unset = UNSET
    valid_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_branch_id = self.app_branch_id

        app_config_id = self.app_config_id

        app_id = self.app_id

        config_hash = self.config_hash

        created_at = self.created_at

        created_by_id = self.created_by_id

        enabled = self.enabled

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        force = self.force

        id = self.id

        input_mappings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_mappings, Unset):
            input_mappings = self.input_mappings.to_dict()

        install_name = self.install_name

        name = self.name

        org_id = self.org_id

        plan_only = self.plan_only

        runbook_id = self.runbook_id

        suspended_at = self.suspended_at

        suspended_by_id = self.suspended_by_id

        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        trigger_id = self.trigger_id

        updated_at = self.updated_at

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if config_hash is not UNSET:
            field_dict["config_hash"] = config_hash
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if filters is not UNSET:
            field_dict["filters"] = filters
        if force is not UNSET:
            field_dict["force"] = force
        if id is not UNSET:
            field_dict["id"] = id
        if input_mappings is not UNSET:
            field_dict["input_mappings"] = input_mappings
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if plan_only is not UNSET:
            field_dict["plan_only"] = plan_only
        if runbook_id is not UNSET:
            field_dict["runbook_id"] = runbook_id
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at
        if suspended_by_id is not UNSET:
            field_dict["suspended_by_id"] = suspended_by_id
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if trigger_id is not UNSET:
            field_dict["trigger_id"] = trigger_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_trigger_filter import AppTriggerFilter
        from ..models.app_trigger_rule_input_mappings import AppTriggerRuleInputMappings

        d = dict(src_dict)
        app_branch_id = d.pop("app_branch_id", UNSET)

        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        config_hash = d.pop("config_hash", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        enabled = d.pop("enabled", UNSET)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: list[AppTriggerFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = AppTriggerFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        force = d.pop("force", UNSET)

        id = d.pop("id", UNSET)

        _input_mappings = d.pop("input_mappings", UNSET)
        input_mappings: AppTriggerRuleInputMappings | Unset
        if isinstance(_input_mappings, Unset):
            input_mappings = UNSET
        else:
            input_mappings = AppTriggerRuleInputMappings.from_dict(_input_mappings)

        install_name = d.pop("install_name", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        plan_only = d.pop("plan_only", UNSET)

        runbook_id = d.pop("runbook_id", UNSET)

        suspended_at = d.pop("suspended_at", UNSET)

        suspended_by_id = d.pop("suspended_by_id", UNSET)

        _target_type = d.pop("target_type", UNSET)
        target_type: AppTriggerTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = AppTriggerTargetType(_target_type)

        trigger_id = d.pop("trigger_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        valid_from = d.pop("valid_from", UNSET)

        valid_to = d.pop("valid_to", UNSET)

        app_trigger_rule = cls(
            app_branch_id=app_branch_id,
            app_config_id=app_config_id,
            app_id=app_id,
            config_hash=config_hash,
            created_at=created_at,
            created_by_id=created_by_id,
            enabled=enabled,
            event_types=event_types,
            filters=filters,
            force=force,
            id=id,
            input_mappings=input_mappings,
            install_name=install_name,
            name=name,
            org_id=org_id,
            plan_only=plan_only,
            runbook_id=runbook_id,
            suspended_at=suspended_at,
            suspended_by_id=suspended_by_id,
            target_type=target_type,
            trigger_id=trigger_id,
            updated_at=updated_at,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        app_trigger_rule.additional_properties = d
        return app_trigger_rule

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
