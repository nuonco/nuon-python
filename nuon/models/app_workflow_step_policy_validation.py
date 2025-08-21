from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus


T = TypeVar("T", bound="AppWorkflowStepPolicyValidation")


@_attrs_define
class AppWorkflowStepPolicyValidation:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_workflow_step_id (Union[Unset, str]): install workflow step is the install step that this was performed
            within
        response (Union[Unset, str]): response is the kyverno response
        runner_job_id (Union[Unset, str]): runnerJobID is the runner job that this was performed within
        status (Union[Unset, AppCompositeStatus]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_workflow_step_id: Union[Unset, str] = UNSET
    response: Union[Unset, str] = UNSET
    runner_job_id: Union[Unset, str] = UNSET
    status: Union[Unset, "AppCompositeStatus"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_workflow_step_id = self.install_workflow_step_id

        response = self.response

        runner_job_id = self.runner_job_id

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_workflow_step_id is not UNSET:
            field_dict["install_workflow_step_id"] = install_workflow_step_id
        if response is not UNSET:
            field_dict["response"] = response
        if runner_job_id is not UNSET:
            field_dict["runner_job_id"] = runner_job_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_workflow_step_id = d.pop("install_workflow_step_id", UNSET)

        response = d.pop("response", UNSET)

        runner_job_id = d.pop("runner_job_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppCompositeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        updated_at = d.pop("updated_at", UNSET)

        app_workflow_step_policy_validation = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_workflow_step_id=install_workflow_step_id,
            response=response,
            runner_job_id=runner_job_id,
            status=status,
            updated_at=updated_at,
        )

        app_workflow_step_policy_validation.additional_properties = d
        return app_workflow_step_policy_validation

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
