from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iam_two_step_config import IamTwoStepConfig


T = TypeVar("T", bound="CredentialsAssumeRoleConfig")


@_attrs_define
class CredentialsAssumeRoleConfig:
    """
    Attributes:
        role_arn (str):
        session_name (str):
        session_duration_seconds (int | Unset):
        two_step_config (IamTwoStepConfig | Unset):
        use_github_oidc (bool | Unset):
    """

    role_arn: str
    session_name: str
    session_duration_seconds: int | Unset = UNSET
    two_step_config: IamTwoStepConfig | Unset = UNSET
    use_github_oidc: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_arn = self.role_arn

        session_name = self.session_name

        session_duration_seconds = self.session_duration_seconds

        two_step_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.two_step_config, Unset):
            two_step_config = self.two_step_config.to_dict()

        use_github_oidc = self.use_github_oidc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_arn": role_arn,
                "session_name": session_name,
            }
        )
        if session_duration_seconds is not UNSET:
            field_dict["session_duration_seconds"] = session_duration_seconds
        if two_step_config is not UNSET:
            field_dict["two_step_config"] = two_step_config
        if use_github_oidc is not UNSET:
            field_dict["use_github_oidc"] = use_github_oidc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iam_two_step_config import IamTwoStepConfig

        d = dict(src_dict)
        role_arn = d.pop("role_arn")

        session_name = d.pop("session_name")

        session_duration_seconds = d.pop("session_duration_seconds", UNSET)

        _two_step_config = d.pop("two_step_config", UNSET)
        two_step_config: IamTwoStepConfig | Unset
        if isinstance(_two_step_config, Unset):
            two_step_config = UNSET
        else:
            two_step_config = IamTwoStepConfig.from_dict(_two_step_config)

        use_github_oidc = d.pop("use_github_oidc", UNSET)

        credentials_assume_role_config = cls(
            role_arn=role_arn,
            session_name=session_name,
            session_duration_seconds=session_duration_seconds,
            two_step_config=two_step_config,
            use_github_oidc=use_github_oidc,
        )

        credentials_assume_role_config.additional_properties = d
        return credentials_assume_role_config

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
