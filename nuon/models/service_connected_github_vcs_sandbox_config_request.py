from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceConnectedGithubVCSSandboxConfigRequest")


@_attrs_define
class ServiceConnectedGithubVCSSandboxConfigRequest:
    """
    Attributes:
        directory (str):
        repo (str):
        branch (Union[Unset, str]):
        git_ref (Union[Unset, str]):
    """

    directory: str
    repo: str
    branch: Union[Unset, str] = UNSET
    git_ref: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory = self.directory

        repo = self.repo

        branch = self.branch

        git_ref = self.git_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "directory": directory,
                "repo": repo,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if git_ref is not UNSET:
            field_dict["gitRef"] = git_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory = d.pop("directory")

        repo = d.pop("repo")

        branch = d.pop("branch", UNSET)

        git_ref = d.pop("gitRef", UNSET)

        service_connected_github_vcs_sandbox_config_request = cls(
            directory=directory,
            repo=repo,
            branch=branch,
            git_ref=git_ref,
        )

        service_connected_github_vcs_sandbox_config_request.additional_properties = d
        return service_connected_github_vcs_sandbox_config_request

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
