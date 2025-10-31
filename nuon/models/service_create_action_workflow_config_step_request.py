from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_connected_github_vcs_action_workflow_config_request import (
        ServiceConnectedGithubVCSActionWorkflowConfigRequest,
    )
    from ..models.service_create_action_workflow_config_step_request_env_vars import (
        ServiceCreateActionWorkflowConfigStepRequestEnvVars,
    )
    from ..models.service_public_git_vcs_action_workflow_config_request import (
        ServicePublicGitVCSActionWorkflowConfigRequest,
    )


T = TypeVar("T", bound="ServiceCreateActionWorkflowConfigStepRequest")


@_attrs_define
class ServiceCreateActionWorkflowConfigStepRequest:
    """
    Attributes:
        name (str):
        command (str | Unset):
        connected_github_vcs_config (ServiceConnectedGithubVCSActionWorkflowConfigRequest | Unset):
        env_vars (ServiceCreateActionWorkflowConfigStepRequestEnvVars | Unset):
        inline_contents (str | Unset):
        public_git_vcs_config (ServicePublicGitVCSActionWorkflowConfigRequest | Unset):
        references (list[str] | Unset):
    """

    name: str
    command: str | Unset = UNSET
    connected_github_vcs_config: ServiceConnectedGithubVCSActionWorkflowConfigRequest | Unset = UNSET
    env_vars: ServiceCreateActionWorkflowConfigStepRequestEnvVars | Unset = UNSET
    inline_contents: str | Unset = UNSET
    public_git_vcs_config: ServicePublicGitVCSActionWorkflowConfigRequest | Unset = UNSET
    references: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        command = self.command

        connected_github_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        inline_contents = self.inline_contents

        public_git_vcs_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_connected_github_vcs_action_workflow_config_request import (
            ServiceConnectedGithubVCSActionWorkflowConfigRequest,
        )
        from ..models.service_create_action_workflow_config_step_request_env_vars import (
            ServiceCreateActionWorkflowConfigStepRequestEnvVars,
        )
        from ..models.service_public_git_vcs_action_workflow_config_request import (
            ServicePublicGitVCSActionWorkflowConfigRequest,
        )

        d = dict(src_dict)
        name = d.pop("name")

        command = d.pop("command", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: ServiceConnectedGithubVCSActionWorkflowConfigRequest | Unset
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = ServiceConnectedGithubVCSActionWorkflowConfigRequest.from_dict(
                _connected_github_vcs_config
            )

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: ServiceCreateActionWorkflowConfigStepRequestEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateActionWorkflowConfigStepRequestEnvVars.from_dict(_env_vars)

        inline_contents = d.pop("inline_contents", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: ServicePublicGitVCSActionWorkflowConfigRequest | Unset
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = ServicePublicGitVCSActionWorkflowConfigRequest.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        service_create_action_workflow_config_step_request = cls(
            name=name,
            command=command,
            connected_github_vcs_config=connected_github_vcs_config,
            env_vars=env_vars,
            inline_contents=inline_contents,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
        )

        service_create_action_workflow_config_step_request.additional_properties = d
        return service_create_action_workflow_config_step_request

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
