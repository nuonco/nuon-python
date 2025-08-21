from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component import AppComponent


T = TypeVar("T", bound="AppActionWorkflowTriggerConfig")


@_attrs_define
class AppActionWorkflowTriggerConfig:
    """
    Attributes:
        action_workflow_config_id (Union[Unset, str]):
        app_config_id (Union[Unset, str]): this belongs to an app config id
        app_id (Union[Unset, str]):
        component (Union[Unset, AppComponent]):
        component_id (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        cron_schedule (Union[Unset, str]):
        id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    action_workflow_config_id: Union[Unset, str] = UNSET
    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    component: Union[Unset, "AppComponent"] = UNSET
    component_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    cron_schedule: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_config_id = self.action_workflow_config_id

        app_config_id = self.app_config_id

        app_id = self.app_id

        component: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        component_id = self.component_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        cron_schedule = self.cron_schedule

        id = self.id

        type_ = self.type_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_config_id is not UNSET:
            field_dict["action_workflow_config_id"] = action_workflow_config_id
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if component is not UNSET:
            field_dict["component"] = component
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if cron_schedule is not UNSET:
            field_dict["cron_schedule"] = cron_schedule
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component import AppComponent

        d = dict(src_dict)
        action_workflow_config_id = d.pop("action_workflow_config_id", UNSET)

        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        _component = d.pop("component", UNSET)
        component: Union[Unset, AppComponent]
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = AppComponent.from_dict(_component)

        component_id = d.pop("component_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        cron_schedule = d.pop("cron_schedule", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_action_workflow_trigger_config = cls(
            action_workflow_config_id=action_workflow_config_id,
            app_config_id=app_config_id,
            app_id=app_id,
            component=component,
            component_id=component_id,
            created_at=created_at,
            created_by_id=created_by_id,
            cron_schedule=cron_schedule,
            id=id,
            type_=type_,
            updated_at=updated_at,
        )

        app_action_workflow_trigger_config.additional_properties = d
        return app_action_workflow_trigger_config

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
