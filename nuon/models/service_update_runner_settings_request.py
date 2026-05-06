from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_update_runner_settings_request_aws_auth_method import (
    ServiceUpdateRunnerSettingsRequestAwsAuthMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_update_runner_settings_request_job_group_parallelism import (
        ServiceUpdateRunnerSettingsRequestJobGroupParallelism,
    )


T = TypeVar("T", bound="ServiceUpdateRunnerSettingsRequest")


@_attrs_define
class ServiceUpdateRunnerSettingsRequest:
    """
    Attributes:
        aws_auth_method (ServiceUpdateRunnerSettingsRequestAwsAuthMethod | Unset):
        aws_max_instance_lifetime (int | Unset): Deprecated: no longer used. Instance refresh is handled by a backend
            cron.
        binary_version (str | Unset):
        container_image_tag (str | Unset):
        container_image_url (str | Unset):
        container_max_uptime (int | Unset):
        job_group_parallelism (ServiceUpdateRunnerSettingsRequestJobGroupParallelism | Unset): JobGroupParallelism maps
            job group names to max-in-flight values for parallel job execution.
            e.g., {"build": 2, "deploy": 1}. Only effective when parallel-runner-jobs feature flag is enabled.
        org_awsiam_role_arn (str | Unset):
        org_k8s_service_account_name (str | Unset):
        runner_api_url (str | Unset):
        vm_max_uptime (int | Unset):
    """

    aws_auth_method: ServiceUpdateRunnerSettingsRequestAwsAuthMethod | Unset = UNSET
    aws_max_instance_lifetime: int | Unset = UNSET
    binary_version: str | Unset = UNSET
    container_image_tag: str | Unset = UNSET
    container_image_url: str | Unset = UNSET
    container_max_uptime: int | Unset = UNSET
    job_group_parallelism: ServiceUpdateRunnerSettingsRequestJobGroupParallelism | Unset = UNSET
    org_awsiam_role_arn: str | Unset = UNSET
    org_k8s_service_account_name: str | Unset = UNSET
    runner_api_url: str | Unset = UNSET
    vm_max_uptime: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_auth_method: str | Unset = UNSET
        if not isinstance(self.aws_auth_method, Unset):
            aws_auth_method = self.aws_auth_method.value

        aws_max_instance_lifetime = self.aws_max_instance_lifetime

        binary_version = self.binary_version

        container_image_tag = self.container_image_tag

        container_image_url = self.container_image_url

        container_max_uptime = self.container_max_uptime

        job_group_parallelism: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_group_parallelism, Unset):
            job_group_parallelism = self.job_group_parallelism.to_dict()

        org_awsiam_role_arn = self.org_awsiam_role_arn

        org_k8s_service_account_name = self.org_k8s_service_account_name

        runner_api_url = self.runner_api_url

        vm_max_uptime = self.vm_max_uptime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_auth_method is not UNSET:
            field_dict["aws_auth_method"] = aws_auth_method
        if aws_max_instance_lifetime is not UNSET:
            field_dict["aws_max_instance_lifetime"] = aws_max_instance_lifetime
        if binary_version is not UNSET:
            field_dict["binary_version"] = binary_version
        if container_image_tag is not UNSET:
            field_dict["container_image_tag"] = container_image_tag
        if container_image_url is not UNSET:
            field_dict["container_image_url"] = container_image_url
        if container_max_uptime is not UNSET:
            field_dict["container_max_uptime"] = container_max_uptime
        if job_group_parallelism is not UNSET:
            field_dict["job_group_parallelism"] = job_group_parallelism
        if org_awsiam_role_arn is not UNSET:
            field_dict["org_awsiam_role_arn"] = org_awsiam_role_arn
        if org_k8s_service_account_name is not UNSET:
            field_dict["org_k8s_service_account_name"] = org_k8s_service_account_name
        if runner_api_url is not UNSET:
            field_dict["runner_api_url"] = runner_api_url
        if vm_max_uptime is not UNSET:
            field_dict["vm_max_uptime"] = vm_max_uptime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_update_runner_settings_request_job_group_parallelism import (
            ServiceUpdateRunnerSettingsRequestJobGroupParallelism,
        )

        d = dict(src_dict)
        _aws_auth_method = d.pop("aws_auth_method", UNSET)
        aws_auth_method: ServiceUpdateRunnerSettingsRequestAwsAuthMethod | Unset
        if isinstance(_aws_auth_method, Unset):
            aws_auth_method = UNSET
        else:
            aws_auth_method = ServiceUpdateRunnerSettingsRequestAwsAuthMethod(_aws_auth_method)

        aws_max_instance_lifetime = d.pop("aws_max_instance_lifetime", UNSET)

        binary_version = d.pop("binary_version", UNSET)

        container_image_tag = d.pop("container_image_tag", UNSET)

        container_image_url = d.pop("container_image_url", UNSET)

        container_max_uptime = d.pop("container_max_uptime", UNSET)

        _job_group_parallelism = d.pop("job_group_parallelism", UNSET)
        job_group_parallelism: ServiceUpdateRunnerSettingsRequestJobGroupParallelism | Unset
        if isinstance(_job_group_parallelism, Unset):
            job_group_parallelism = UNSET
        else:
            job_group_parallelism = ServiceUpdateRunnerSettingsRequestJobGroupParallelism.from_dict(
                _job_group_parallelism
            )

        org_awsiam_role_arn = d.pop("org_awsiam_role_arn", UNSET)

        org_k8s_service_account_name = d.pop("org_k8s_service_account_name", UNSET)

        runner_api_url = d.pop("runner_api_url", UNSET)

        vm_max_uptime = d.pop("vm_max_uptime", UNSET)

        service_update_runner_settings_request = cls(
            aws_auth_method=aws_auth_method,
            aws_max_instance_lifetime=aws_max_instance_lifetime,
            binary_version=binary_version,
            container_image_tag=container_image_tag,
            container_image_url=container_image_url,
            container_max_uptime=container_max_uptime,
            job_group_parallelism=job_group_parallelism,
            org_awsiam_role_arn=org_awsiam_role_arn,
            org_k8s_service_account_name=org_k8s_service_account_name,
            runner_api_url=runner_api_url,
            vm_max_uptime=vm_max_uptime,
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
