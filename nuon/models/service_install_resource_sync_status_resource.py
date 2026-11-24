from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_resource_sync_status_category import ServiceInstallResourceSyncStatusCategory
from ..models.service_install_resource_sync_status_resource_kind import ServiceInstallResourceSyncStatusResourceKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_resource_sync_status_attempt import ServiceInstallResourceSyncStatusAttempt
    from ..models.service_install_resource_sync_status_explanation import ServiceInstallResourceSyncStatusExplanation
    from ..models.service_install_resource_sync_status_open_deployment import (
        ServiceInstallResourceSyncStatusOpenDeployment,
    )
    from ..models.service_install_resource_sync_status_origin import ServiceInstallResourceSyncStatusOrigin
    from ..models.service_install_resource_sync_status_plan import ServiceInstallResourceSyncStatusPlan


T = TypeVar("T", bound="ServiceInstallResourceSyncStatusResource")


@_attrs_define
class ServiceInstallResourceSyncStatusResource:
    """
    Attributes:
        applied_build_id (str | Unset):
        applied_by (ServiceInstallResourceSyncStatusOrigin | Unset):
        applied_config_id (str | Unset):
        applied_deploy_at (str | Unset):
        applied_deploy_id (str | Unset):
        category (ServiceInstallResourceSyncStatusCategory | Unset):
        component_id (str | Unset):
        component_type (str | Unset):
        expected_build_id (str | Unset):
        expected_config_id (str | Unset):
        explanation (ServiceInstallResourceSyncStatusExplanation | Unset):
        id (str | Unset):
        kind (ServiceInstallResourceSyncStatusResourceKind | Unset):
        last_attempt (ServiceInstallResourceSyncStatusAttempt | Unset):
        name (str | Unset):
        newer_branch_runs (int | None | Unset):
        open_deployment (ServiceInstallResourceSyncStatusOpenDeployment | Unset):
        plan (ServiceInstallResourceSyncStatusPlan | Unset):
        reason (str | Unset):
        status (str | Unset):
    """

    applied_build_id: str | Unset = UNSET
    applied_by: ServiceInstallResourceSyncStatusOrigin | Unset = UNSET
    applied_config_id: str | Unset = UNSET
    applied_deploy_at: str | Unset = UNSET
    applied_deploy_id: str | Unset = UNSET
    category: ServiceInstallResourceSyncStatusCategory | Unset = UNSET
    component_id: str | Unset = UNSET
    component_type: str | Unset = UNSET
    expected_build_id: str | Unset = UNSET
    expected_config_id: str | Unset = UNSET
    explanation: ServiceInstallResourceSyncStatusExplanation | Unset = UNSET
    id: str | Unset = UNSET
    kind: ServiceInstallResourceSyncStatusResourceKind | Unset = UNSET
    last_attempt: ServiceInstallResourceSyncStatusAttempt | Unset = UNSET
    name: str | Unset = UNSET
    newer_branch_runs: int | None | Unset = UNSET
    open_deployment: ServiceInstallResourceSyncStatusOpenDeployment | Unset = UNSET
    plan: ServiceInstallResourceSyncStatusPlan | Unset = UNSET
    reason: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_build_id = self.applied_build_id

        applied_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applied_by, Unset):
            applied_by = self.applied_by.to_dict()

        applied_config_id = self.applied_config_id

        applied_deploy_at = self.applied_deploy_at

        applied_deploy_id = self.applied_deploy_id

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        component_id = self.component_id

        component_type = self.component_type

        expected_build_id = self.expected_build_id

        expected_config_id = self.expected_config_id

        explanation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.explanation, Unset):
            explanation = self.explanation.to_dict()

        id = self.id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        last_attempt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_attempt, Unset):
            last_attempt = self.last_attempt.to_dict()

        name = self.name

        newer_branch_runs: int | None | Unset
        if isinstance(self.newer_branch_runs, Unset):
            newer_branch_runs = UNSET
        else:
            newer_branch_runs = self.newer_branch_runs

        open_deployment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_deployment, Unset):
            open_deployment = self.open_deployment.to_dict()

        plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        reason = self.reason

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_build_id is not UNSET:
            field_dict["applied_build_id"] = applied_build_id
        if applied_by is not UNSET:
            field_dict["applied_by"] = applied_by
        if applied_config_id is not UNSET:
            field_dict["applied_config_id"] = applied_config_id
        if applied_deploy_at is not UNSET:
            field_dict["applied_deploy_at"] = applied_deploy_at
        if applied_deploy_id is not UNSET:
            field_dict["applied_deploy_id"] = applied_deploy_id
        if category is not UNSET:
            field_dict["category"] = category
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if expected_build_id is not UNSET:
            field_dict["expected_build_id"] = expected_build_id
        if expected_config_id is not UNSET:
            field_dict["expected_config_id"] = expected_config_id
        if explanation is not UNSET:
            field_dict["explanation"] = explanation
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if last_attempt is not UNSET:
            field_dict["last_attempt"] = last_attempt
        if name is not UNSET:
            field_dict["name"] = name
        if newer_branch_runs is not UNSET:
            field_dict["newer_branch_runs"] = newer_branch_runs
        if open_deployment is not UNSET:
            field_dict["open_deployment"] = open_deployment
        if plan is not UNSET:
            field_dict["plan"] = plan
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_resource_sync_status_attempt import ServiceInstallResourceSyncStatusAttempt  # noqa: PLC0415
        from ..models.service_install_resource_sync_status_explanation import (
            ServiceInstallResourceSyncStatusExplanation,  # noqa: PLC0415
        )
        from ..models.service_install_resource_sync_status_open_deployment import (
            ServiceInstallResourceSyncStatusOpenDeployment,  # noqa: PLC0415
        )
        from ..models.service_install_resource_sync_status_origin import ServiceInstallResourceSyncStatusOrigin  # noqa: PLC0415
        from ..models.service_install_resource_sync_status_plan import ServiceInstallResourceSyncStatusPlan  # noqa: PLC0415

        d = dict(src_dict)
        applied_build_id = d.pop("applied_build_id", UNSET)

        _applied_by = d.pop("applied_by", UNSET)
        applied_by: ServiceInstallResourceSyncStatusOrigin | Unset
        if isinstance(_applied_by, Unset):
            applied_by = UNSET
        else:
            applied_by = ServiceInstallResourceSyncStatusOrigin.from_dict(_applied_by)

        applied_config_id = d.pop("applied_config_id", UNSET)

        applied_deploy_at = d.pop("applied_deploy_at", UNSET)

        applied_deploy_id = d.pop("applied_deploy_id", UNSET)

        _category = d.pop("category", UNSET)
        category: ServiceInstallResourceSyncStatusCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ServiceInstallResourceSyncStatusCategory(_category)

        component_id = d.pop("component_id", UNSET)

        component_type = d.pop("component_type", UNSET)

        expected_build_id = d.pop("expected_build_id", UNSET)

        expected_config_id = d.pop("expected_config_id", UNSET)

        _explanation = d.pop("explanation", UNSET)
        explanation: ServiceInstallResourceSyncStatusExplanation | Unset
        if isinstance(_explanation, Unset):
            explanation = UNSET
        else:
            explanation = ServiceInstallResourceSyncStatusExplanation.from_dict(_explanation)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: ServiceInstallResourceSyncStatusResourceKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ServiceInstallResourceSyncStatusResourceKind(_kind)

        _last_attempt = d.pop("last_attempt", UNSET)
        last_attempt: ServiceInstallResourceSyncStatusAttempt | Unset
        if isinstance(_last_attempt, Unset):
            last_attempt = UNSET
        else:
            last_attempt = ServiceInstallResourceSyncStatusAttempt.from_dict(_last_attempt)

        name = d.pop("name", UNSET)

        def _parse_newer_branch_runs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        newer_branch_runs = _parse_newer_branch_runs(d.pop("newer_branch_runs", UNSET))

        _open_deployment = d.pop("open_deployment", UNSET)
        open_deployment: ServiceInstallResourceSyncStatusOpenDeployment | Unset
        if isinstance(_open_deployment, Unset):
            open_deployment = UNSET
        else:
            open_deployment = ServiceInstallResourceSyncStatusOpenDeployment.from_dict(_open_deployment)

        _plan = d.pop("plan", UNSET)
        plan: ServiceInstallResourceSyncStatusPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = ServiceInstallResourceSyncStatusPlan.from_dict(_plan)

        reason = d.pop("reason", UNSET)

        status = d.pop("status", UNSET)

        service_install_resource_sync_status_resource = cls(
            applied_build_id=applied_build_id,
            applied_by=applied_by,
            applied_config_id=applied_config_id,
            applied_deploy_at=applied_deploy_at,
            applied_deploy_id=applied_deploy_id,
            category=category,
            component_id=component_id,
            component_type=component_type,
            expected_build_id=expected_build_id,
            expected_config_id=expected_config_id,
            explanation=explanation,
            id=id,
            kind=kind,
            last_attempt=last_attempt,
            name=name,
            newer_branch_runs=newer_branch_runs,
            open_deployment=open_deployment,
            plan=plan,
            reason=reason,
            status=status,
        )

        service_install_resource_sync_status_resource.additional_properties = d
        return service_install_resource_sync_status_resource

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
