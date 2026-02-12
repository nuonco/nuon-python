from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_policy_report_owner_type import AppPolicyReportOwnerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_policy_input_ref import AppPolicyInputRef
    from ..models.app_policy_result import AppPolicyResult
    from ..models.app_policy_violation import AppPolicyViolation


T = TypeVar("T", bound="AppPolicyReport")


@_attrs_define
class AppPolicyReport:
    """
    Attributes:
        app_id (str | Unset): Denormalized context for filtering
        app_name (str | Unset):
        component_id (str | Unset):
        component_name (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        deny_count (int | Unset): Summary counts for list views
        evaluated_at (str | Unset): Canonical policy evaluation data
        id (str | Unset):
        inputs (list[AppPolicyInputRef] | Unset):
        install_id (str | Unset):
        install_name (str | Unset):
        org_name (str | Unset): Denormalized display names for human-readable reports
        owner_id (str | Unset): Polymorphic relationship to the impacted Nuon resource (indexes defined in Indexes())
        owner_type (AppPolicyReportOwnerType | Unset):
        pass_count (int | Unset):
        policies (list[AppPolicyResult] | Unset):
        policy_ids (list[str] | Unset):
        runner_job_id (str | Unset):
        status (AppCompositeStatus | Unset):
        updated_at (str | Unset):
        violations (list[AppPolicyViolation] | Unset):
        warn_count (int | Unset):
        workflow_step_policy_validation_id (str | Unset): Optional context references (indexes defined in Indexes())
    """

    app_id: str | Unset = UNSET
    app_name: str | Unset = UNSET
    component_id: str | Unset = UNSET
    component_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    deny_count: int | Unset = UNSET
    evaluated_at: str | Unset = UNSET
    id: str | Unset = UNSET
    inputs: list[AppPolicyInputRef] | Unset = UNSET
    install_id: str | Unset = UNSET
    install_name: str | Unset = UNSET
    org_name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: AppPolicyReportOwnerType | Unset = UNSET
    pass_count: int | Unset = UNSET
    policies: list[AppPolicyResult] | Unset = UNSET
    policy_ids: list[str] | Unset = UNSET
    runner_job_id: str | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    updated_at: str | Unset = UNSET
    violations: list[AppPolicyViolation] | Unset = UNSET
    warn_count: int | Unset = UNSET
    workflow_step_policy_validation_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_name = self.app_name

        component_id = self.component_id

        component_name = self.component_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        deny_count = self.deny_count

        evaluated_at = self.evaluated_at

        id = self.id

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        install_id = self.install_id

        install_name = self.install_name

        org_name = self.org_name

        owner_id = self.owner_id

        owner_type: str | Unset = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type.value

        pass_count = self.pass_count

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)

        policy_ids: list[str] | Unset = UNSET
        if not isinstance(self.policy_ids, Unset):
            policy_ids = self.policy_ids

        runner_job_id = self.runner_job_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at = self.updated_at

        violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.violations, Unset):
            violations = []
            for violations_item_data in self.violations:
                violations_item = violations_item_data.to_dict()
                violations.append(violations_item)

        warn_count = self.warn_count

        workflow_step_policy_validation_id = self.workflow_step_policy_validation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if deny_count is not UNSET:
            field_dict["deny_count"] = deny_count
        if evaluated_at is not UNSET:
            field_dict["evaluated_at"] = evaluated_at
        if id is not UNSET:
            field_dict["id"] = id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_name is not UNSET:
            field_dict["install_name"] = install_name
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if pass_count is not UNSET:
            field_dict["pass_count"] = pass_count
        if policies is not UNSET:
            field_dict["policies"] = policies
        if policy_ids is not UNSET:
            field_dict["policy_ids"] = policy_ids
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if violations is not UNSET:
            field_dict["violations"] = violations
        if warn_count is not UNSET:
            field_dict["warn_count"] = warn_count
        if workflow_step_policy_validation_id is not UNSET:
            field_dict["workflow_step_policy_validation_id"] = workflow_step_policy_validation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_policy_input_ref import AppPolicyInputRef
        from ..models.app_policy_result import AppPolicyResult
        from ..models.app_policy_violation import AppPolicyViolation

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        app_name = d.pop("app_name", UNSET)

        component_id = d.pop("component_id", UNSET)

        component_name = d.pop("component_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        deny_count = d.pop("deny_count", UNSET)

        evaluated_at = d.pop("evaluated_at", UNSET)

        id = d.pop("id", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: list[AppPolicyInputRef] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = AppPolicyInputRef.from_dict(inputs_item_data)

                inputs.append(inputs_item)

        install_id = d.pop("install_id", UNSET)

        install_name = d.pop("install_name", UNSET)

        org_name = d.pop("org_name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        _owner_type = d.pop("owner_type", UNSET)
        owner_type: AppPolicyReportOwnerType | Unset
        if isinstance(_owner_type, Unset):
            owner_type = UNSET
        else:
            owner_type = AppPolicyReportOwnerType(_owner_type)

        pass_count = d.pop("pass_count", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[AppPolicyResult] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = AppPolicyResult.from_dict(policies_item_data)

                policies.append(policies_item)

        policy_ids = cast(list[str], d.pop("policy_ids", UNSET))

        runner_job_id = d.pop("runner_job_id", UNSET)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        _violations = d.pop("violations", UNSET)
        violations: list[AppPolicyViolation] | Unset = UNSET
        if _violations is not UNSET:
            violations = []
            for violations_item_data in _violations:
                violations_item = AppPolicyViolation.from_dict(violations_item_data)

                violations.append(violations_item)

        warn_count = d.pop("warn_count", UNSET)

        workflow_step_policy_validation_id = d.pop("workflow_step_policy_validation_id", UNSET)

        app_policy_report = cls(
            app_id=app_id,
            app_name=app_name,
            component_id=component_id,
            component_name=component_name,
            created_at=created_at,
            created_by_id=created_by_id,
            deny_count=deny_count,
            evaluated_at=evaluated_at,
            id=id,
            inputs=inputs,
            install_id=install_id,
            install_name=install_name,
            org_name=org_name,
            owner_id=owner_id,
            owner_type=owner_type,
            pass_count=pass_count,
            policies=policies,
            policy_ids=policy_ids,
            runner_job_id=runner_job_id,
            status=status,
            updated_at=updated_at,
            violations=violations,
            warn_count=warn_count,
            workflow_step_policy_validation_id=workflow_step_policy_validation_id,
        )

        app_policy_report.additional_properties = d
        return app_policy_report

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
