from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUpdateRunnerSettingsRequest")


@_attrs_define
class ServiceUpdateRunnerSettingsRequest:
    """
    Attributes:
        aws_max_instance_lifetime (Union[Unset, int]):
        container_image_tag (Union[Unset, str]):
        container_image_url (Union[Unset, str]):
        org_awsiam_role_arn (Union[Unset, str]):
        org_k8s_service_account_name (Union[Unset, str]):
        runner_api_url (Union[Unset, str]):
    """

    aws_max_instance_lifetime: Union[Unset, int] = UNSET
    container_image_tag: Union[Unset, str] = UNSET
    container_image_url: Union[Unset, str] = UNSET
    org_awsiam_role_arn: Union[Unset, str] = UNSET
    org_k8s_service_account_name: Union[Unset, str] = UNSET
    runner_api_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_max_instance_lifetime = self.aws_max_instance_lifetime

        container_image_tag = self.container_image_tag

        container_image_url = self.container_image_url

        org_awsiam_role_arn = self.org_awsiam_role_arn

        org_k8s_service_account_name = self.org_k8s_service_account_name

        runner_api_url = self.runner_api_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_max_instance_lifetime is not UNSET:
            field_dict["aws_max_instance_lifetime"] = aws_max_instance_lifetime
        if container_image_tag is not UNSET:
            field_dict["container_image_tag"] = container_image_tag
        if container_image_url is not UNSET:
            field_dict["container_image_url"] = container_image_url
        if org_awsiam_role_arn is not UNSET:
            field_dict["org_awsiam_role_arn"] = org_awsiam_role_arn
        if org_k8s_service_account_name is not UNSET:
            field_dict["org_k8s_service_account_name"] = org_k8s_service_account_name
        if runner_api_url is not UNSET:
            field_dict["runner_api_url"] = runner_api_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_max_instance_lifetime = d.pop("aws_max_instance_lifetime", UNSET)

        container_image_tag = d.pop("container_image_tag", UNSET)

        container_image_url = d.pop("container_image_url", UNSET)

        org_awsiam_role_arn = d.pop("org_awsiam_role_arn", UNSET)

        org_k8s_service_account_name = d.pop("org_k8s_service_account_name", UNSET)

        runner_api_url = d.pop("runner_api_url", UNSET)

        service_update_runner_settings_request = cls(
            aws_max_instance_lifetime=aws_max_instance_lifetime,
            container_image_tag=container_image_tag,
            container_image_url=container_image_url,
            org_awsiam_role_arn=org_awsiam_role_arn,
            org_k8s_service_account_name=org_k8s_service_account_name,
            runner_api_url=runner_api_url,
        )

        service_update_runner_settings_request.additional_properties = d
        return service_update_runner_settings_request

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
