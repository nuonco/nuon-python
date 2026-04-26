from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRetryWorkflowStepResponse")


@_attrs_define
class ServiceRetryWorkflowStepResponse:
    """
    Attributes:
        retryable (bool | Unset):
        workflow_id (str | Unset):
    """

    retryable: bool | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retryable = self.retryable

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retryable is not UNSET:
            field_dict["retryable"] = retryable
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retryable = d.pop("retryable", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        service_retry_workflow_step_response = cls(
            retryable=retryable,
            workflow_id=workflow_id,
        )

        service_retry_workflow_step_response.additional_properties = d
        return service_retry_workflow_step_response

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
