from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAWSECRImageConfig")


@_attrs_define
class AppAWSECRImageConfig:
    """
    Attributes:
        aws_region (str | Unset):
        component_config_id (str | Unset): connection to parent model
        component_config_type (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        iam_role_arn (str | Unset): actual configuration
        id (str | Unset):
        updated_at (str | Unset):
    """

    aws_region: str | Unset = UNSET
    component_config_id: str | Unset = UNSET
    component_config_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    iam_role_arn: str | Unset = UNSET
    id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_region = self.aws_region

        component_config_id = self.component_config_id

        component_config_type = self.component_config_type

        created_at = self.created_at

        created_by_id = self.created_by_id

        iam_role_arn = self.iam_role_arn

        id = self.id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_region is not UNSET:
            field_dict["aws_region"] = aws_region
        if component_config_id is not UNSET:
            field_dict["component_config_id"] = component_config_id
        if component_config_type is not UNSET:
            field_dict["component_config_type"] = component_config_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if iam_role_arn is not UNSET:
            field_dict["iam_role_arn"] = iam_role_arn
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_region = d.pop("aws_region", UNSET)

        component_config_id = d.pop("component_config_id", UNSET)

        component_config_type = d.pop("component_config_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        iam_role_arn = d.pop("iam_role_arn", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_awsecr_image_config = cls(
            aws_region=aws_region,
            component_config_id=component_config_id,
            component_config_type=component_config_type,
            created_at=created_at,
            created_by_id=created_by_id,
            iam_role_arn=iam_role_arn,
            id=id,
            updated_at=updated_at,
        )

        app_awsecr_image_config.additional_properties = d
        return app_awsecr_image_config

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
