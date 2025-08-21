from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAWSAccount")


@_attrs_define
class AppAWSAccount:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        iam_role_arn (Union[Unset, str]):
        id (Union[Unset, str]):
        region (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    iam_role_arn: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        iam_role_arn = self.iam_role_arn

        id = self.id

        region = self.region

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if iam_role_arn is not UNSET:
            field_dict["iam_role_arn"] = iam_role_arn
        if id is not UNSET:
            field_dict["id"] = id
        if region is not UNSET:
            field_dict["region"] = region
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        iam_role_arn = d.pop("iam_role_arn", UNSET)

        id = d.pop("id", UNSET)

        region = d.pop("region", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_aws_account = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            iam_role_arn=iam_role_arn,
            id=id,
            region=region,
            updated_at=updated_at,
        )

        app_aws_account.additional_properties = d
        return app_aws_account

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
