from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAwsECRImageConfigRequest")


@_attrs_define
class ServiceAwsECRImageConfigRequest:
    """
    Attributes:
        aws_region (Union[Unset, str]):
        iam_role_arn (Union[Unset, str]):
    """

    aws_region: Union[Unset, str] = UNSET
    iam_role_arn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_region = self.aws_region

        iam_role_arn = self.iam_role_arn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_region is not UNSET:
            field_dict["aws_region"] = aws_region
        if iam_role_arn is not UNSET:
            field_dict["iam_role_arn"] = iam_role_arn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_region = d.pop("aws_region", UNSET)

        iam_role_arn = d.pop("iam_role_arn", UNSET)

        service_aws_ecr_image_config_request = cls(
            aws_region=aws_region,
            iam_role_arn=iam_role_arn,
        )

        service_aws_ecr_image_config_request.additional_properties = d
        return service_aws_ecr_image_config_request

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
