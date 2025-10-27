from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_action_workflow_run_step_plan_attrs import PlantypesActionWorkflowRunStepPlanAttrs
    from ..models.plantypes_action_workflow_run_step_plan_interpolated_env_vars import (
        PlantypesActionWorkflowRunStepPlanInterpolatedEnvVars,
    )
    from ..models.plantypes_git_source import PlantypesGitSource


T = TypeVar("T", bound="PlantypesActionWorkflowRunStepPlan")


@_attrs_define
class PlantypesActionWorkflowRunStepPlan:
    """
    Attributes:
        attrs (Union[Unset, PlantypesActionWorkflowRunStepPlanAttrs]):
        git_source (Union[Unset, PlantypesGitSource]):
        interpolated_command (Union[Unset, str]):
        interpolated_env_vars (Union[Unset, PlantypesActionWorkflowRunStepPlanInterpolatedEnvVars]):
        interpolated_inline_contents (Union[Unset, str]):
        run_id (Union[Unset, str]):
    """

    attrs: Union[Unset, "PlantypesActionWorkflowRunStepPlanAttrs"] = UNSET
    git_source: Union[Unset, "PlantypesGitSource"] = UNSET
    interpolated_command: Union[Unset, str] = UNSET
    interpolated_env_vars: Union[Unset, "PlantypesActionWorkflowRunStepPlanInterpolatedEnvVars"] = UNSET
    interpolated_inline_contents: Union[Unset, str] = UNSET
    run_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attrs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attrs, Unset):
            attrs = self.attrs.to_dict()

        git_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.git_source, Unset):
            git_source = self.git_source.to_dict()

        interpolated_command = self.interpolated_command

        interpolated_env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interpolated_env_vars, Unset):
            interpolated_env_vars = self.interpolated_env_vars.to_dict()

        interpolated_inline_contents = self.interpolated_inline_contents

        run_id = self.run_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attrs is not UNSET:
            field_dict["attrs"] = attrs
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if interpolated_command is not UNSET:
            field_dict["interpolated_command"] = interpolated_command
        if interpolated_env_vars is not UNSET:
            field_dict["interpolated_env_vars"] = interpolated_env_vars
        if interpolated_inline_contents is not UNSET:
            field_dict["interpolated_inline_contents"] = interpolated_inline_contents
        if run_id is not UNSET:
            field_dict["run_id"] = run_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_action_workflow_run_step_plan_attrs import PlantypesActionWorkflowRunStepPlanAttrs
        from ..models.plantypes_action_workflow_run_step_plan_interpolated_env_vars import (
            PlantypesActionWorkflowRunStepPlanInterpolatedEnvVars,
        )
        from ..models.plantypes_git_source import PlantypesGitSource

        d = dict(src_dict)
        _attrs = d.pop("attrs", UNSET)
        attrs: Union[Unset, PlantypesActionWorkflowRunStepPlanAttrs]
        if isinstance(_attrs, Unset):
            attrs = UNSET
        else:
            attrs = PlantypesActionWorkflowRunStepPlanAttrs.from_dict(_attrs)

        _git_source = d.pop("git_source", UNSET)
        git_source: Union[Unset, PlantypesGitSource]
        if isinstance(_git_source, Unset):
            git_source = UNSET
        else:
            git_source = PlantypesGitSource.from_dict(_git_source)

        interpolated_command = d.pop("interpolated_command", UNSET)

        _interpolated_env_vars = d.pop("interpolated_env_vars", UNSET)
        interpolated_env_vars: Union[Unset, PlantypesActionWorkflowRunStepPlanInterpolatedEnvVars]
        if isinstance(_interpolated_env_vars, Unset):
            interpolated_env_vars = UNSET
        else:
            interpolated_env_vars = PlantypesActionWorkflowRunStepPlanInterpolatedEnvVars.from_dict(
                _interpolated_env_vars
            )

        interpolated_inline_contents = d.pop("interpolated_inline_contents", UNSET)

        run_id = d.pop("run_id", UNSET)

        plantypes_action_workflow_run_step_plan = cls(
            attrs=attrs,
            git_source=git_source,
            interpolated_command=interpolated_command,
            interpolated_env_vars=interpolated_env_vars,
            interpolated_inline_contents=interpolated_inline_contents,
            run_id=run_id,
        )

        plantypes_action_workflow_run_step_plan.additional_properties = d
        return plantypes_action_workflow_run_step_plan

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
