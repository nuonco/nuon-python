from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow_step_config import AppActionWorkflowStepConfig
    from ..models.app_action_workflow_trigger_config import AppActionWorkflowTriggerConfig
    from ..models.refs_ref import RefsRef


T = TypeVar("T", bound="AppActionWorkflowConfig")


@_attrs_define
class AppActionWorkflowConfig:
    """
    Attributes:
        action_workflow_id (Union[Unset, str]):
        app_config_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        break_glass_role_arn (Union[Unset, str]):
        component_dependency_ids (Union[Unset, list[str]]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        refs (Union[Unset, list['RefsRef']]):
        steps (Union[Unset, list['AppActionWorkflowStepConfig']]):
        timeout (Union[Unset, int]):
        triggers (Union[Unset, list['AppActionWorkflowTriggerConfig']]): INFO: if adding new associations here, ensure
            they are added to the batch delete activity
        updated_at (Union[Unset, str]):
    """

    action_workflow_id: Union[Unset, str] = UNSET
    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    break_glass_role_arn: Union[Unset, str] = UNSET
    component_dependency_ids: Union[Unset, list[str]] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    refs: Union[Unset, list["RefsRef"]] = UNSET
    steps: Union[Unset, list["AppActionWorkflowStepConfig"]] = UNSET
    timeout: Union[Unset, int] = UNSET
    triggers: Union[Unset, list["AppActionWorkflowTriggerConfig"]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_id = self.action_workflow_id

        app_config_id = self.app_config_id

        app_id = self.app_id

        break_glass_role_arn = self.break_glass_role_arn

        component_dependency_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.component_dependency_ids, Unset):
            component_dependency_ids = self.component_dependency_ids

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        refs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()
                refs.append(refs_item)

        steps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        timeout = self.timeout

        triggers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item = triggers_item_data.to_dict()
                triggers.append(triggers_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_id is not UNSET:
            field_dict["action_workflow_id"] = action_workflow_id
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if break_glass_role_arn is not UNSET:
            field_dict["break_glass_role_arn"] = break_glass_role_arn
        if component_dependency_ids is not UNSET:
            field_dict["component_dependency_ids"] = component_dependency_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if references is not UNSET:
            field_dict["references"] = references
        if refs is not UNSET:
            field_dict["refs"] = refs
        if steps is not UNSET:
            field_dict["steps"] = steps
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_action_workflow_step_config import AppActionWorkflowStepConfig
        from ..models.app_action_workflow_trigger_config import AppActionWorkflowTriggerConfig
        from ..models.refs_ref import RefsRef

        d = dict(src_dict)
        action_workflow_id = d.pop("action_workflow_id", UNSET)

        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        break_glass_role_arn = d.pop("break_glass_role_arn", UNSET)

        component_dependency_ids = cast(list[str], d.pop("component_dependency_ids", UNSET))

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        refs = []
        _refs = d.pop("refs", UNSET)
        for refs_item_data in _refs or []:
            refs_item = RefsRef.from_dict(refs_item_data)

            refs.append(refs_item)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = AppActionWorkflowStepConfig.from_dict(steps_item_data)

            steps.append(steps_item)

        timeout = d.pop("timeout", UNSET)

        triggers = []
        _triggers = d.pop("triggers", UNSET)
        for triggers_item_data in _triggers or []:
            triggers_item = AppActionWorkflowTriggerConfig.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        updated_at = d.pop("updated_at", UNSET)

        app_action_workflow_config = cls(
            action_workflow_id=action_workflow_id,
            app_config_id=app_config_id,
            app_id=app_id,
            break_glass_role_arn=break_glass_role_arn,
            component_dependency_ids=component_dependency_ids,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            references=references,
            refs=refs,
            steps=steps,
            timeout=timeout,
            triggers=triggers,
            updated_at=updated_at,
        )

        app_action_workflow_config.additional_properties = d
        return app_action_workflow_config

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
