from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRetryWorkflowRequest")


@_attrs_define
class ServiceRetryWorkflowRequest:
    """
    Attributes:
        operation (str | Unset): Retry indicates whether to retry the current step or not
        step_id (str | Unset): StepID is the ID of the step to start the retry from
        workflow_id (str | Unset):
    """

    operation: str | Unset = UNSET
    step_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        step_id = self.step_id

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation is not UNSET:
            field_dict["operation"] = operation
        if step_id is not UNSET:
            field_dict["step_id"] = step_id
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = d.pop("operation", UNSET)

        step_id = d.pop("step_id", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        service_retry_workflow_request = cls(
            operation=operation,
            step_id=step_id,
            workflow_id=workflow_id,
        )

        service_retry_workflow_request.additional_properties = d
        return service_retry_workflow_request

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
