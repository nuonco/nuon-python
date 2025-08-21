from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow import AppActionWorkflow
    from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun


T = TypeVar("T", bound="AppInstallActionWorkflow")


@_attrs_define
class AppInstallActionWorkflow:
    """
    Attributes:
        action_workflow (Union[Unset, AppActionWorkflow]):
        action_workflow_id (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_id (Union[Unset, str]):
        runs (Union[Unset, list['AppInstallActionWorkflowRun']]):
        status (Union[Unset, str]): after query fields filled in after querying
        updated_at (Union[Unset, str]):
    """

    action_workflow: Union[Unset, "AppActionWorkflow"] = UNSET
    action_workflow_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_id: Union[Unset, str] = UNSET
    runs: Union[Unset, list["AppInstallActionWorkflowRun"]] = UNSET
    status: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.action_workflow, Unset):
            action_workflow = self.action_workflow.to_dict()

        action_workflow_id = self.action_workflow_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        runs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()
                runs.append(runs_item)

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow is not UNSET:
            field_dict["action_workflow"] = action_workflow
        if action_workflow_id is not UNSET:
            field_dict["action_workflow_id"] = action_workflow_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if runs is not UNSET:
            field_dict["runs"] = runs
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_action_workflow import AppActionWorkflow
        from ..models.app_install_action_workflow_run import AppInstallActionWorkflowRun

        d = dict(src_dict)
        _action_workflow = d.pop("action_workflow", UNSET)
        action_workflow: Union[Unset, AppActionWorkflow]
        if isinstance(_action_workflow, Unset):
            action_workflow = UNSET
        else:
            action_workflow = AppActionWorkflow.from_dict(_action_workflow)

        action_workflow_id = d.pop("action_workflow_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        runs = []
        _runs = d.pop("runs", UNSET)
        for runs_item_data in _runs or []:
            runs_item = AppInstallActionWorkflowRun.from_dict(runs_item_data)

            runs.append(runs_item)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_action_workflow = cls(
            action_workflow=action_workflow,
            action_workflow_id=action_workflow_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            runs=runs,
            status=status,
            updated_at=updated_at,
        )

        app_install_action_workflow.additional_properties = d
        return app_install_action_workflow

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
