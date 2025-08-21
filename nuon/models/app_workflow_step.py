from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_workflow_step_execution_type import AppWorkflowStepExecutionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_workflow_step_approval import AppWorkflowStepApproval
    from ..models.app_workflow_step_links import AppWorkflowStepLinks
    from ..models.app_workflow_step_metadata import AppWorkflowStepMetadata
    from ..models.app_workflow_step_policy_validation import AppWorkflowStepPolicyValidation


T = TypeVar("T", bound="AppWorkflowStep")


@_attrs_define
class AppWorkflowStep:
    """
    Attributes:
        approval (Union[Unset, AppWorkflowStepApproval]):
        created_at (Union[Unset, str]):
        created_by (Union[Unset, AppAccount]):
        created_by_id (Union[Unset, str]):
        execution_time (Union[Unset, int]):
        execution_type (Union[Unset, AppWorkflowStepExecutionType]):
        finished (Union[Unset, bool]):
        finished_at (Union[Unset, str]):
        group_idx (Union[Unset, int]): to group steps which belong to same logical group, eg, plan/apply
        group_retry_idx (Union[Unset, int]): counter for every retry attempted on a group
        id (Union[Unset, str]):
        idx (Union[Unset, int]):
        install_workflow_id (Union[Unset, str]): DEPRECATED: this is the install workflow ID, which is now the workflow
            ID.
        links (Union[Unset, AppWorkflowStepLinks]):
        metadata (Union[Unset, AppWorkflowStepMetadata]):
        name (Union[Unset, str]):
        owner_id (Union[Unset, str]):
        owner_type (Union[Unset, str]):
        policy_validation (Union[Unset, AppWorkflowStepPolicyValidation]):
        retried (Union[Unset, bool]):
        retryable (Union[Unset, bool]):
        skippable (Union[Unset, bool]):
        started_at (Union[Unset, str]):
        status (Union[Unset, AppCompositeStatus]):
        step_target_id (Union[Unset, str]): the following fields are set _once_ a step is in flight, and are
            orchestrated via the step's signal.

            this is a polymorphic gorm relationship to one of the following objects:

            install_cloudformation_stack
            install_sandbox_run
            install_runner_update
            install_deploy
            install_action_workflow_run (can be many of these)
        step_target_type (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        workflow_id (Union[Unset, str]): Fields that are de-nested at read time using AfterQuery
    """

    approval: Union[Unset, "AppWorkflowStepApproval"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, "AppAccount"] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    execution_time: Union[Unset, int] = UNSET
    execution_type: Union[Unset, AppWorkflowStepExecutionType] = UNSET
    finished: Union[Unset, bool] = UNSET
    finished_at: Union[Unset, str] = UNSET
    group_idx: Union[Unset, int] = UNSET
    group_retry_idx: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    install_workflow_id: Union[Unset, str] = UNSET
    links: Union[Unset, "AppWorkflowStepLinks"] = UNSET
    metadata: Union[Unset, "AppWorkflowStepMetadata"] = UNSET
    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_type: Union[Unset, str] = UNSET
    policy_validation: Union[Unset, "AppWorkflowStepPolicyValidation"] = UNSET
    retried: Union[Unset, bool] = UNSET
    retryable: Union[Unset, bool] = UNSET
    skippable: Union[Unset, bool] = UNSET
    started_at: Union[Unset, str] = UNSET
    status: Union[Unset, "AppCompositeStatus"] = UNSET
    step_target_id: Union[Unset, str] = UNSET
    step_target_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.to_dict()

        created_at = self.created_at

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        execution_time = self.execution_time

        execution_type: Union[Unset, str] = UNSET
        if not isinstance(self.execution_type, Unset):
            execution_type = self.execution_type.value

        finished = self.finished

        finished_at = self.finished_at

        group_idx = self.group_idx

        group_retry_idx = self.group_retry_idx

        id = self.id

        idx = self.idx

        install_workflow_id = self.install_workflow_id

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        owner_id = self.owner_id

        owner_type = self.owner_type

        policy_validation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.policy_validation, Unset):
            policy_validation = self.policy_validation.to_dict()

        retried = self.retried

        retryable = self.retryable

        skippable = self.skippable

        started_at = self.started_at

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        step_target_id = self.step_target_id

        step_target_type = self.step_target_type

        updated_at = self.updated_at

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval is not UNSET:
            field_dict["approval"] = approval
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if execution_time is not UNSET:
            field_dict["execution_time"] = execution_time
        if execution_type is not UNSET:
            field_dict["execution_type"] = execution_type
        if finished is not UNSET:
            field_dict["finished"] = finished
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if group_idx is not UNSET:
            field_dict["group_idx"] = group_idx
        if group_retry_idx is not UNSET:
            field_dict["group_retry_idx"] = group_retry_idx
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if install_workflow_id is not UNSET:
            field_dict["install_workflow_id"] = install_workflow_id
        if links is not UNSET:
            field_dict["links"] = links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if policy_validation is not UNSET:
            field_dict["policy_validation"] = policy_validation
        if retried is not UNSET:
            field_dict["retried"] = retried
        if retryable is not UNSET:
            field_dict["retryable"] = retryable
        if skippable is not UNSET:
            field_dict["skippable"] = skippable
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if step_target_id is not UNSET:
            field_dict["step_target_id"] = step_target_id
        if step_target_type is not UNSET:
            field_dict["step_target_type"] = step_target_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_workflow_step_approval import AppWorkflowStepApproval
        from ..models.app_workflow_step_links import AppWorkflowStepLinks
        from ..models.app_workflow_step_metadata import AppWorkflowStepMetadata
        from ..models.app_workflow_step_policy_validation import AppWorkflowStepPolicyValidation

        d = dict(src_dict)
        _approval = d.pop("approval", UNSET)
        approval: Union[Unset, AppWorkflowStepApproval]
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = AppWorkflowStepApproval.from_dict(_approval)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: Union[Unset, AppAccount]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        execution_time = d.pop("execution_time", UNSET)

        _execution_type = d.pop("execution_type", UNSET)
        execution_type: Union[Unset, AppWorkflowStepExecutionType]
        if isinstance(_execution_type, Unset):
            execution_type = UNSET
        else:
            execution_type = AppWorkflowStepExecutionType(_execution_type)

        finished = d.pop("finished", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        group_idx = d.pop("group_idx", UNSET)

        group_retry_idx = d.pop("group_retry_idx", UNSET)

        id = d.pop("id", UNSET)

        idx = d.pop("idx", UNSET)

        install_workflow_id = d.pop("install_workflow_id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, AppWorkflowStepLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppWorkflowStepLinks.from_dict(_links)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AppWorkflowStepMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppWorkflowStepMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        _policy_validation = d.pop("policy_validation", UNSET)
        policy_validation: Union[Unset, AppWorkflowStepPolicyValidation]
        if isinstance(_policy_validation, Unset):
            policy_validation = UNSET
        else:
            policy_validation = AppWorkflowStepPolicyValidation.from_dict(_policy_validation)

        retried = d.pop("retried", UNSET)

        retryable = d.pop("retryable", UNSET)

        skippable = d.pop("skippable", UNSET)

        started_at = d.pop("started_at", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AppCompositeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        step_target_id = d.pop("step_target_id", UNSET)

        step_target_type = d.pop("step_target_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        app_workflow_step = cls(
            approval=approval,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            execution_time=execution_time,
            execution_type=execution_type,
            finished=finished,
            finished_at=finished_at,
            group_idx=group_idx,
            group_retry_idx=group_retry_idx,
            id=id,
            idx=idx,
            install_workflow_id=install_workflow_id,
            links=links,
            metadata=metadata,
            name=name,
            owner_id=owner_id,
            owner_type=owner_type,
            policy_validation=policy_validation,
            retried=retried,
            retryable=retryable,
            skippable=skippable,
            started_at=started_at,
            status=status,
            step_target_id=step_target_id,
            step_target_type=step_target_type,
            updated_at=updated_at,
            workflow_id=workflow_id,
        )

        app_workflow_step.additional_properties = d
        return app_workflow_step

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
