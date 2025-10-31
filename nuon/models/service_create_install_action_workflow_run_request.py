from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_install_action_workflow_run_request_run_env_vars import (
        ServiceCreateInstallActionWorkflowRunRequestRunEnvVars,
    )


T = TypeVar("T", bound="ServiceCreateInstallActionWorkflowRunRequest")


@_attrs_define
class ServiceCreateInstallActionWorkflowRunRequest:
    """
    Attributes:
        action_workflow_config_id (str | Unset):
        run_env_vars (ServiceCreateInstallActionWorkflowRunRequestRunEnvVars | Unset):
    """

    action_workflow_config_id: str | Unset = UNSET
    run_env_vars: ServiceCreateInstallActionWorkflowRunRequestRunEnvVars | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_config_id = self.action_workflow_config_id

        run_env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_env_vars, Unset):
            run_env_vars = self.run_env_vars.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_config_id is not UNSET:
            field_dict["action_workflow_config_id"] = action_workflow_config_id
        if run_env_vars is not UNSET:
            field_dict["run_env_vars"] = run_env_vars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_install_action_workflow_run_request_run_env_vars import (
            ServiceCreateInstallActionWorkflowRunRequestRunEnvVars,
        )

        d = dict(src_dict)
        action_workflow_config_id = d.pop("action_workflow_config_id", UNSET)

        _run_env_vars = d.pop("run_env_vars", UNSET)
        run_env_vars: ServiceCreateInstallActionWorkflowRunRequestRunEnvVars | Unset
        if isinstance(_run_env_vars, Unset):
            run_env_vars = UNSET
        else:
            run_env_vars = ServiceCreateInstallActionWorkflowRunRequestRunEnvVars.from_dict(_run_env_vars)

        service_create_install_action_workflow_run_request = cls(
            action_workflow_config_id=action_workflow_config_id,
            run_env_vars=run_env_vars,
        )

        service_create_install_action_workflow_run_request.additional_properties = d
        return service_create_install_action_workflow_run_request

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
