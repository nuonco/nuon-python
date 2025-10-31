from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iam_static_credentials import IamStaticCredentials


T = TypeVar("T", bound="IamTwoStepConfig")


@_attrs_define
class IamTwoStepConfig:
    """
    Attributes:
        iam_role_arn (str | Unset):
        src_iam_role_arn (str | Unset):
        src_static_credentials (IamStaticCredentials | Unset):
    """

    iam_role_arn: str | Unset = UNSET
    src_iam_role_arn: str | Unset = UNSET
    src_static_credentials: IamStaticCredentials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iam_role_arn = self.iam_role_arn

        src_iam_role_arn = self.src_iam_role_arn

        src_static_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_static_credentials, Unset):
            src_static_credentials = self.src_static_credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iam_role_arn is not UNSET:
            field_dict["iam_role_arn"] = iam_role_arn
        if src_iam_role_arn is not UNSET:
            field_dict["src_iam_role_arn"] = src_iam_role_arn
        if src_static_credentials is not UNSET:
            field_dict["src_static_credentials"] = src_static_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iam_static_credentials import IamStaticCredentials

        d = dict(src_dict)
        iam_role_arn = d.pop("iam_role_arn", UNSET)

        src_iam_role_arn = d.pop("src_iam_role_arn", UNSET)

        _src_static_credentials = d.pop("src_static_credentials", UNSET)
        src_static_credentials: IamStaticCredentials | Unset
        if isinstance(_src_static_credentials, Unset):
            src_static_credentials = UNSET
        else:
            src_static_credentials = IamStaticCredentials.from_dict(_src_static_credentials)

        iam_two_step_config = cls(
            iam_role_arn=iam_role_arn,
            src_iam_role_arn=src_iam_role_arn,
            src_static_credentials=src_static_credentials,
        )

        iam_two_step_config.additional_properties = d
        return iam_two_step_config

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
