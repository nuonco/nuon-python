from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runbook_step_config import AppRunbookStepConfig


T = TypeVar("T", bound="AppRunbookConfig")


@_attrs_define
class AppRunbookConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        readme (str | Unset):
        runbook_id (str | Unset):
        steps (list[AppRunbookStepConfig] | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    readme: str | Unset = UNSET
    runbook_id: str | Unset = UNSET
    steps: list[AppRunbookStepConfig] | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        readme = self.readme

        runbook_id = self.runbook_id

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if readme is not UNSET:
            field_dict["readme"] = readme
        if runbook_id is not UNSET:
            field_dict["runbook_id"] = runbook_id
        if steps is not UNSET:
            field_dict["steps"] = steps
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runbook_step_config import AppRunbookStepConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        readme = d.pop("readme", UNSET)

        runbook_id = d.pop("runbook_id", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: list[AppRunbookStepConfig] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = AppRunbookStepConfig.from_dict(steps_item_data)

                steps.append(steps_item)

        updated_at = d.pop("updated_at", UNSET)

        app_runbook_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            readme=readme,
            runbook_id=runbook_id,
            steps=steps,
            updated_at=updated_at,
        )

        app_runbook_config.additional_properties = d
        return app_runbook_config

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
