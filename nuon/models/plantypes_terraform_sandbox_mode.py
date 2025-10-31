from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlantypesTerraformSandboxMode")


@_attrs_define
class PlantypesTerraformSandboxMode:
    """
    Attributes:
        plan_contents (str | Unset): create the plan output
        plan_display_contents (str | Unset):
        state_json (list[int] | Unset): needs to be the outputs of `terraform show -json`
        workspace_id (str | Unset):
    """

    plan_contents: str | Unset = UNSET
    plan_display_contents: str | Unset = UNSET
    state_json: list[int] | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_contents = self.plan_contents

        plan_display_contents = self.plan_display_contents

        state_json: list[int] | Unset = UNSET
        if not isinstance(self.state_json, Unset):
            state_json = self.state_json

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_contents is not UNSET:
            field_dict["plan_contents"] = plan_contents
        if plan_display_contents is not UNSET:
            field_dict["plan_display_contents"] = plan_display_contents
        if state_json is not UNSET:
            field_dict["state_json"] = state_json
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_contents = d.pop("plan_contents", UNSET)

        plan_display_contents = d.pop("plan_display_contents", UNSET)

        state_json = cast(list[int], d.pop("state_json", UNSET))

        workspace_id = d.pop("workspace_id", UNSET)

        plantypes_terraform_sandbox_mode = cls(
            plan_contents=plan_contents,
            plan_display_contents=plan_display_contents,
            state_json=state_json,
            workspace_id=workspace_id,
        )

        plantypes_terraform_sandbox_mode.additional_properties = d
        return plantypes_terraform_sandbox_mode

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
