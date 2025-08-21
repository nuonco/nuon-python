from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow_step_config_env_vars import AppActionWorkflowStepConfigEnvVars
    from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
    from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig


T = TypeVar("T", bound="AppActionWorkflowStepConfig")


@_attrs_define
class AppActionWorkflowStepConfig:
    """
    Attributes:
        action_workflow_config_id (Union[Unset, str]):
        app_config_id (Union[Unset, str]): this belongs to an app config id
        app_id (Union[Unset, str]):
        command (Union[Unset, str]):
        connected_github_vcs_config (Union[Unset, AppConnectedGithubVCSConfig]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        env_vars (Union[Unset, AppActionWorkflowStepConfigEnvVars]):
        id (Union[Unset, str]):
        idx (Union[Unset, int]):
        inline_contents (Union[Unset, str]):
        name (Union[Unset, str]): metadata
        previous_step_id (Union[Unset, str]):
        public_git_vcs_config (Union[Unset, AppPublicGitVCSConfig]):
        references (Union[Unset, list[str]]):
        updated_at (Union[Unset, str]):
    """

    action_workflow_config_id: Union[Unset, str] = UNSET
    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    command: Union[Unset, str] = UNSET
    connected_github_vcs_config: Union[Unset, "AppConnectedGithubVCSConfig"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "AppActionWorkflowStepConfigEnvVars"] = UNSET
    id: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    inline_contents: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    previous_step_id: Union[Unset, str] = UNSET
    public_git_vcs_config: Union[Unset, "AppPublicGitVCSConfig"] = UNSET
    references: Union[Unset, list[str]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_workflow_config_id = self.action_workflow_config_id

        app_config_id = self.app_config_id

        app_id = self.app_id

        command = self.command

        connected_github_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connected_github_vcs_config, Unset):
            connected_github_vcs_config = self.connected_github_vcs_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        idx = self.idx

        inline_contents = self.inline_contents

        name = self.name

        previous_step_id = self.previous_step_id

        public_git_vcs_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_git_vcs_config, Unset):
            public_git_vcs_config = self.public_git_vcs_config.to_dict()

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_workflow_config_id is not UNSET:
            field_dict["action_workflow_config_id"] = action_workflow_config_id
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if command is not UNSET:
            field_dict["command"] = command
        if connected_github_vcs_config is not UNSET:
            field_dict["connected_github_vcs_config"] = connected_github_vcs_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if inline_contents is not UNSET:
            field_dict["inline_contents"] = inline_contents
        if name is not UNSET:
            field_dict["name"] = name
        if previous_step_id is not UNSET:
            field_dict["previous_step_id"] = previous_step_id
        if public_git_vcs_config is not UNSET:
            field_dict["public_git_vcs_config"] = public_git_vcs_config
        if references is not UNSET:
            field_dict["references"] = references
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_action_workflow_step_config_env_vars import AppActionWorkflowStepConfigEnvVars
        from ..models.app_connected_github_vcs_config import AppConnectedGithubVCSConfig
        from ..models.app_public_git_vcs_config import AppPublicGitVCSConfig

        d = dict(src_dict)
        action_workflow_config_id = d.pop("action_workflow_config_id", UNSET)

        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        command = d.pop("command", UNSET)

        _connected_github_vcs_config = d.pop("connected_github_vcs_config", UNSET)
        connected_github_vcs_config: Union[Unset, AppConnectedGithubVCSConfig]
        if isinstance(_connected_github_vcs_config, Unset):
            connected_github_vcs_config = UNSET
        else:
            connected_github_vcs_config = AppConnectedGithubVCSConfig.from_dict(_connected_github_vcs_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, AppActionWorkflowStepConfigEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = AppActionWorkflowStepConfigEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        idx = d.pop("idx", UNSET)

        inline_contents = d.pop("inline_contents", UNSET)

        name = d.pop("name", UNSET)

        previous_step_id = d.pop("previous_step_id", UNSET)

        _public_git_vcs_config = d.pop("public_git_vcs_config", UNSET)
        public_git_vcs_config: Union[Unset, AppPublicGitVCSConfig]
        if isinstance(_public_git_vcs_config, Unset):
            public_git_vcs_config = UNSET
        else:
            public_git_vcs_config = AppPublicGitVCSConfig.from_dict(_public_git_vcs_config)

        references = cast(list[str], d.pop("references", UNSET))

        updated_at = d.pop("updated_at", UNSET)

        app_action_workflow_step_config = cls(
            action_workflow_config_id=action_workflow_config_id,
            app_config_id=app_config_id,
            app_id=app_id,
            command=command,
            connected_github_vcs_config=connected_github_vcs_config,
            created_at=created_at,
            created_by_id=created_by_id,
            env_vars=env_vars,
            id=id,
            idx=idx,
            inline_contents=inline_contents,
            name=name,
            previous_step_id=previous_step_id,
            public_git_vcs_config=public_git_vcs_config,
            references=references,
            updated_at=updated_at,
        )

        app_action_workflow_step_config.additional_properties = d
        return app_action_workflow_step_config

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
