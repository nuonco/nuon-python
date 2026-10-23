from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_type import AppWorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_overview_commit import ServiceInstallOverviewCommit


T = TypeVar("T", bound="ServiceInstallAlignmentAttempt")


@_attrs_define
class ServiceInstallAlignmentAttempt:
    """
    Attributes:
        branch_run (ServiceInstallOverviewCommit | Unset):
        created_at (str | Unset):
        id (str | Unset):
        status (str | Unset):
        type_ (AppWorkflowType | Unset):
        workflow_id (str | Unset):
    """

    branch_run: ServiceInstallOverviewCommit | Unset = UNSET
    created_at: str | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    type_: AppWorkflowType | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch_run, Unset):
            branch_run = self.branch_run.to_dict()

        created_at = self.created_at

        id = self.id

        status = self.status

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_run is not UNSET:
            field_dict["branch_run"] = branch_run
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_overview_commit import ServiceInstallOverviewCommit  # noqa: PLC0415

        d = dict(src_dict)
        _branch_run = d.pop("branch_run", UNSET)
        branch_run: ServiceInstallOverviewCommit | Unset
        if isinstance(_branch_run, Unset):
            branch_run = UNSET
        else:
            branch_run = ServiceInstallOverviewCommit.from_dict(_branch_run)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AppWorkflowType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppWorkflowType(_type_)

        workflow_id = d.pop("workflow_id", UNSET)

        service_install_alignment_attempt = cls(
            branch_run=branch_run,
            created_at=created_at,
            id=id,
            status=status,
            type_=type_,
            workflow_id=workflow_id,
        )

        service_install_alignment_attempt.additional_properties = d
        return service_install_alignment_attempt

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
