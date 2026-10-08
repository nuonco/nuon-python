from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_deployment_policy_summary import ServiceInstallDeploymentPolicySummary


T = TypeVar("T", bound="ServiceInstallDeploymentStep")


@_attrs_define
class ServiceInstallDeploymentStep:
    """
    Attributes:
        approval_response_id (str | Unset):
        component_name (str | Unset):
        execution_type (str | Unset):
        group_idx (int | Unset):
        group_retry_idx (int | Unset):
        id (str | Unset):
        idx (int | Unset):
        name (str | Unset):
        policy (ServiceInstallDeploymentPolicySummary | Unset):
        retried (bool | Unset):
        status (str | Unset):
        step_target_type (str | Unset):
    """

    approval_response_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    execution_type: str | Unset = UNSET
    group_idx: int | Unset = UNSET
    group_retry_idx: int | Unset = UNSET
    id: str | Unset = UNSET
    idx: int | Unset = UNSET
    name: str | Unset = UNSET
    policy: ServiceInstallDeploymentPolicySummary | Unset = UNSET
    retried: bool | Unset = UNSET
    status: str | Unset = UNSET
    step_target_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_response_id = self.approval_response_id

        component_name = self.component_name

        execution_type = self.execution_type

        group_idx = self.group_idx

        group_retry_idx = self.group_retry_idx

        id = self.id

        idx = self.idx

        name = self.name

        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        retried = self.retried

        status = self.status

        step_target_type = self.step_target_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_response_id is not UNSET:
            field_dict["approval_response_id"] = approval_response_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if execution_type is not UNSET:
            field_dict["execution_type"] = execution_type
        if group_idx is not UNSET:
            field_dict["group_idx"] = group_idx
        if group_retry_idx is not UNSET:
            field_dict["group_retry_idx"] = group_retry_idx
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if retried is not UNSET:
            field_dict["retried"] = retried
        if status is not UNSET:
            field_dict["status"] = status
        if step_target_type is not UNSET:
            field_dict["step_target_type"] = step_target_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_deployment_policy_summary import (
            ServiceInstallDeploymentPolicySummary,  # noqa: PLC0415
        )

        d = dict(src_dict)
        approval_response_id = d.pop("approval_response_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        execution_type = d.pop("execution_type", UNSET)

        group_idx = d.pop("group_idx", UNSET)

        group_retry_idx = d.pop("group_retry_idx", UNSET)

        id = d.pop("id", UNSET)

        idx = d.pop("idx", UNSET)

        name = d.pop("name", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: ServiceInstallDeploymentPolicySummary | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ServiceInstallDeploymentPolicySummary.from_dict(_policy)

        retried = d.pop("retried", UNSET)

        status = d.pop("status", UNSET)

        step_target_type = d.pop("step_target_type", UNSET)

        service_install_deployment_step = cls(
            approval_response_id=approval_response_id,
            component_name=component_name,
            execution_type=execution_type,
            group_idx=group_idx,
            group_retry_idx=group_retry_idx,
            id=id,
            idx=idx,
            name=name,
            policy=policy,
            retried=retried,
            status=status,
            step_target_type=step_target_type,
        )

        service_install_deployment_step.additional_properties = d
        return service_install_deployment_step

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
