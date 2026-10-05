from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_activity_type import ServiceInstallActivityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_activity_action import ServiceInstallActivityAction
    from ..models.service_install_activity_policy import ServiceInstallActivityPolicy
    from ..models.service_install_activity_runbook import ServiceInstallActivityRunbook
    from ..models.service_install_activity_workflow_ref import ServiceInstallActivityWorkflowRef


T = TypeVar("T", bound="ServiceInstallActivity")


@_attrs_define
class ServiceInstallActivity:
    """
    Attributes:
        action (ServiceInstallActivityAction | Unset):
        created_at (str | Unset):
        id (str | Unset):
        policy (ServiceInstallActivityPolicy | Unset):
        runbook (ServiceInstallActivityRunbook | Unset):
        status (str | Unset):
        summary (str | Unset):
        title (str | Unset):
        type_ (ServiceInstallActivityType | Unset):
        workflow (ServiceInstallActivityWorkflowRef | Unset):
    """

    action: ServiceInstallActivityAction | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    policy: ServiceInstallActivityPolicy | Unset = UNSET
    runbook: ServiceInstallActivityRunbook | Unset = UNSET
    status: str | Unset = UNSET
    summary: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: ServiceInstallActivityType | Unset = UNSET
    workflow: ServiceInstallActivityWorkflowRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        created_at = self.created_at

        id = self.id

        policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.to_dict()

        runbook: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runbook, Unset):
            runbook = self.runbook.to_dict()

        status = self.status

        summary = self.summary

        title = self.title

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if policy is not UNSET:
            field_dict["policy"] = policy
        if runbook is not UNSET:
            field_dict["runbook"] = runbook
        if status is not UNSET:
            field_dict["status"] = status
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_activity_action import ServiceInstallActivityAction  # noqa: PLC0415
        from ..models.service_install_activity_policy import ServiceInstallActivityPolicy  # noqa: PLC0415
        from ..models.service_install_activity_runbook import ServiceInstallActivityRunbook  # noqa: PLC0415
        from ..models.service_install_activity_workflow_ref import ServiceInstallActivityWorkflowRef  # noqa: PLC0415

        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: ServiceInstallActivityAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ServiceInstallActivityAction.from_dict(_action)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        _policy = d.pop("policy", UNSET)
        policy: ServiceInstallActivityPolicy | Unset
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ServiceInstallActivityPolicy.from_dict(_policy)

        _runbook = d.pop("runbook", UNSET)
        runbook: ServiceInstallActivityRunbook | Unset
        if isinstance(_runbook, Unset):
            runbook = UNSET
        else:
            runbook = ServiceInstallActivityRunbook.from_dict(_runbook)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServiceInstallActivityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServiceInstallActivityType(_type_)

        _workflow = d.pop("workflow", UNSET)
        workflow: ServiceInstallActivityWorkflowRef | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = ServiceInstallActivityWorkflowRef.from_dict(_workflow)

        service_install_activity = cls(
            action=action,
            created_at=created_at,
            id=id,
            policy=policy,
            runbook=runbook,
            status=status,
            summary=summary,
            title=title,
            type_=type_,
            workflow=workflow,
        )

        service_install_activity.additional_properties = d
        return service_install_activity

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
