from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_group_settings_aws_tags import AppRunnerGroupSettingsAwsTags
    from ..models.app_runner_group_settings_job_group_parallelism import AppRunnerGroupSettingsJobGroupParallelism
    from ..models.app_runner_group_settings_metadata import AppRunnerGroupSettingsMetadata


T = TypeVar("T", bound="AppRunnerGroupSettings")


@_attrs_define
class AppRunnerGroupSettings:
    """
    Attributes:
        aws_cloudformation_stack_type (str | Unset):
        aws_instance_type (str | Unset): aws runner specifics runner-v2
        aws_max_instance_lifetime (int | Unset): Deprecated: instance refresh is now handled by a backend cron, not ASG
            MaxInstanceLifetime.
        aws_tags (AppRunnerGroupSettingsAwsTags | Unset):
        binary_version (str | Unset): configuration for managing the runner binary version (for mng mode, not the
            install runner)
        container_image_tag (str | Unset):
        container_image_url (str | Unset): configuration for deploying the runner
        container_max_uptime (int | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        enable_logging (bool | Unset):
        enable_metrics (bool | Unset):
        enable_sentry (bool | Unset):
        groups (list[str] | Unset): the job loop groups the runner should poll for
        heart_beat_timeout (int | Unset): Various settings for the runner to handle internally
        id (str | Unset):
        job_group_parallelism (AppRunnerGroupSettingsJobGroupParallelism | Unset): JobGroupParallelism maps
            RunnerJobGroup names to max-in-flight counts for queue-based job routing.
            e.g., {"build": "2", "deploy": "1"}. Only used when parallel-runner-jobs feature flag is on.
        local_aws_iam_role_arn (str | Unset):
        logging_level (str | Unset):
        metadata (AppRunnerGroupSettingsMetadata | Unset): Metadata is used as both log and metric tags/attributes in
            the runner when emitting data
        org_aws_iam_role_arn (str | Unset): org runner specifics
        org_azure_client_id (str | Unset):
        org_gcp_service_account (str | Unset):
        org_id (str | Unset):
        org_k8s_service_account_name (str | Unset):
        otel_collector_config (str | Unset):
        platform (str | Unset): platform variable for use in the runner
        runner_api_url (str | Unset):
        runner_binary_url (str | Unset): RunnerBinaryURL overrides the URL used to download the runner binary onto the
            host for mng mode. When empty, defaults to the S3 artifacts URL.
        runner_group_id (str | Unset):
        sandbox_mode (bool | Unset): configuration for managing the runner server side
        updated_at (str | Unset):
        vm_max_uptime (int | Unset):
    """

    aws_cloudformation_stack_type: str | Unset = UNSET
    aws_instance_type: str | Unset = UNSET
    aws_max_instance_lifetime: int | Unset = UNSET
    aws_tags: AppRunnerGroupSettingsAwsTags | Unset = UNSET
    binary_version: str | Unset = UNSET
    container_image_tag: str | Unset = UNSET
    container_image_url: str | Unset = UNSET
    container_max_uptime: int | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    enable_logging: bool | Unset = UNSET
    enable_metrics: bool | Unset = UNSET
    enable_sentry: bool | Unset = UNSET
    groups: list[str] | Unset = UNSET
    heart_beat_timeout: int | Unset = UNSET
    id: str | Unset = UNSET
    job_group_parallelism: AppRunnerGroupSettingsJobGroupParallelism | Unset = UNSET
    local_aws_iam_role_arn: str | Unset = UNSET
    logging_level: str | Unset = UNSET
    metadata: AppRunnerGroupSettingsMetadata | Unset = UNSET
    org_aws_iam_role_arn: str | Unset = UNSET
    org_azure_client_id: str | Unset = UNSET
    org_gcp_service_account: str | Unset = UNSET
    org_id: str | Unset = UNSET
    org_k8s_service_account_name: str | Unset = UNSET
    otel_collector_config: str | Unset = UNSET
    platform: str | Unset = UNSET
    runner_api_url: str | Unset = UNSET
    runner_binary_url: str | Unset = UNSET
    runner_group_id: str | Unset = UNSET
    sandbox_mode: bool | Unset = UNSET
    updated_at: str | Unset = UNSET
    vm_max_uptime: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_cloudformation_stack_type = self.aws_cloudformation_stack_type

        aws_instance_type = self.aws_instance_type

        aws_max_instance_lifetime = self.aws_max_instance_lifetime

        aws_tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_tags, Unset):
            aws_tags = self.aws_tags.to_dict()

        binary_version = self.binary_version

        container_image_tag = self.container_image_tag

        container_image_url = self.container_image_url

        container_max_uptime = self.container_max_uptime

        created_at = self.created_at

        created_by_id = self.created_by_id

        enable_logging = self.enable_logging

        enable_metrics = self.enable_metrics

        enable_sentry = self.enable_sentry

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        heart_beat_timeout = self.heart_beat_timeout

        id = self.id

        job_group_parallelism: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_group_parallelism, Unset):
            job_group_parallelism = self.job_group_parallelism.to_dict()

        local_aws_iam_role_arn = self.local_aws_iam_role_arn

        logging_level = self.logging_level

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_aws_iam_role_arn = self.org_aws_iam_role_arn

        org_azure_client_id = self.org_azure_client_id

        org_gcp_service_account = self.org_gcp_service_account

        org_id = self.org_id

        org_k8s_service_account_name = self.org_k8s_service_account_name

        otel_collector_config = self.otel_collector_config

        platform = self.platform

        runner_api_url = self.runner_api_url

        runner_binary_url = self.runner_binary_url

        runner_group_id = self.runner_group_id

        sandbox_mode = self.sandbox_mode

        updated_at = self.updated_at

        vm_max_uptime = self.vm_max_uptime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_cloudformation_stack_type is not UNSET:
            field_dict["aws_cloudformation_stack_type"] = aws_cloudformation_stack_type
        if aws_instance_type is not UNSET:
            field_dict["aws_instance_type"] = aws_instance_type
        if aws_max_instance_lifetime is not UNSET:
            field_dict["aws_max_instance_lifetime"] = aws_max_instance_lifetime
        if aws_tags is not UNSET:
            field_dict["aws_tags"] = aws_tags
        if binary_version is not UNSET:
            field_dict["binary_version"] = binary_version
        if container_image_tag is not UNSET:
            field_dict["container_image_tag"] = container_image_tag
        if container_image_url is not UNSET:
            field_dict["container_image_url"] = container_image_url
        if container_max_uptime is not UNSET:
            field_dict["container_max_uptime"] = container_max_uptime
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if enable_logging is not UNSET:
            field_dict["enable_logging"] = enable_logging
        if enable_metrics is not UNSET:
            field_dict["enable_metrics"] = enable_metrics
        if enable_sentry is not UNSET:
            field_dict["enable_sentry"] = enable_sentry
        if groups is not UNSET:
            field_dict["groups"] = groups
        if heart_beat_timeout is not UNSET:
            field_dict["heart_beat_timeout"] = heart_beat_timeout
        if id is not UNSET:
            field_dict["id"] = id
        if job_group_parallelism is not UNSET:
            field_dict["job_group_parallelism"] = job_group_parallelism
        if local_aws_iam_role_arn is not UNSET:
            field_dict["local_aws_iam_role_arn"] = local_aws_iam_role_arn
        if logging_level is not UNSET:
            field_dict["logging_level"] = logging_level
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_aws_iam_role_arn is not UNSET:
            field_dict["org_aws_iam_role_arn"] = org_aws_iam_role_arn
        if org_azure_client_id is not UNSET:
            field_dict["org_azure_client_id"] = org_azure_client_id
        if org_gcp_service_account is not UNSET:
            field_dict["org_gcp_service_account"] = org_gcp_service_account
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if org_k8s_service_account_name is not UNSET:
            field_dict["org_k8s_service_account_name"] = org_k8s_service_account_name
        if otel_collector_config is not UNSET:
            field_dict["otel_collector_config"] = otel_collector_config
        if platform is not UNSET:
            field_dict["platform"] = platform
        if runner_api_url is not UNSET:
            field_dict["runner_api_url"] = runner_api_url
        if runner_binary_url is not UNSET:
            field_dict["runner_binary_url"] = runner_binary_url
        if runner_group_id is not UNSET:
            field_dict["runner_group_id"] = runner_group_id
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if vm_max_uptime is not UNSET:
            field_dict["vm_max_uptime"] = vm_max_uptime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_group_settings_aws_tags import AppRunnerGroupSettingsAwsTags
        from ..models.app_runner_group_settings_job_group_parallelism import AppRunnerGroupSettingsJobGroupParallelism
        from ..models.app_runner_group_settings_metadata import AppRunnerGroupSettingsMetadata

        d = dict(src_dict)
        aws_cloudformation_stack_type = d.pop("aws_cloudformation_stack_type", UNSET)

        aws_instance_type = d.pop("aws_instance_type", UNSET)

        aws_max_instance_lifetime = d.pop("aws_max_instance_lifetime", UNSET)

        _aws_tags = d.pop("aws_tags", UNSET)
        aws_tags: AppRunnerGroupSettingsAwsTags | Unset
        if isinstance(_aws_tags, Unset):
            aws_tags = UNSET
        else:
            aws_tags = AppRunnerGroupSettingsAwsTags.from_dict(_aws_tags)

        binary_version = d.pop("binary_version", UNSET)

        container_image_tag = d.pop("container_image_tag", UNSET)

        container_image_url = d.pop("container_image_url", UNSET)

        container_max_uptime = d.pop("container_max_uptime", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        enable_logging = d.pop("enable_logging", UNSET)

        enable_metrics = d.pop("enable_metrics", UNSET)

        enable_sentry = d.pop("enable_sentry", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        heart_beat_timeout = d.pop("heart_beat_timeout", UNSET)

        id = d.pop("id", UNSET)

        _job_group_parallelism = d.pop("job_group_parallelism", UNSET)
        job_group_parallelism: AppRunnerGroupSettingsJobGroupParallelism | Unset
        if isinstance(_job_group_parallelism, Unset):
            job_group_parallelism = UNSET
        else:
            job_group_parallelism = AppRunnerGroupSettingsJobGroupParallelism.from_dict(_job_group_parallelism)

        local_aws_iam_role_arn = d.pop("local_aws_iam_role_arn", UNSET)

        logging_level = d.pop("logging_level", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: AppRunnerGroupSettingsMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppRunnerGroupSettingsMetadata.from_dict(_metadata)

        org_aws_iam_role_arn = d.pop("org_aws_iam_role_arn", UNSET)

        org_azure_client_id = d.pop("org_azure_client_id", UNSET)

        org_gcp_service_account = d.pop("org_gcp_service_account", UNSET)

        org_id = d.pop("org_id", UNSET)

        org_k8s_service_account_name = d.pop("org_k8s_service_account_name", UNSET)

        otel_collector_config = d.pop("otel_collector_config", UNSET)

        platform = d.pop("platform", UNSET)

        runner_api_url = d.pop("runner_api_url", UNSET)

        runner_binary_url = d.pop("runner_binary_url", UNSET)

        runner_group_id = d.pop("runner_group_id", UNSET)

        sandbox_mode = d.pop("sandbox_mode", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        vm_max_uptime = d.pop("vm_max_uptime", UNSET)

        app_runner_group_settings = cls(
            aws_cloudformation_stack_type=aws_cloudformation_stack_type,
            aws_instance_type=aws_instance_type,
            aws_max_instance_lifetime=aws_max_instance_lifetime,
            aws_tags=aws_tags,
            binary_version=binary_version,
            container_image_tag=container_image_tag,
            container_image_url=container_image_url,
            container_max_uptime=container_max_uptime,
            created_at=created_at,
            created_by_id=created_by_id,
            enable_logging=enable_logging,
            enable_metrics=enable_metrics,
            enable_sentry=enable_sentry,
            groups=groups,
            heart_beat_timeout=heart_beat_timeout,
            id=id,
            job_group_parallelism=job_group_parallelism,
            local_aws_iam_role_arn=local_aws_iam_role_arn,
            logging_level=logging_level,
            metadata=metadata,
            org_aws_iam_role_arn=org_aws_iam_role_arn,
            org_azure_client_id=org_azure_client_id,
            org_gcp_service_account=org_gcp_service_account,
            org_id=org_id,
            org_k8s_service_account_name=org_k8s_service_account_name,
            otel_collector_config=otel_collector_config,
            platform=platform,
            runner_api_url=runner_api_url,
            runner_binary_url=runner_binary_url,
            runner_group_id=runner_group_id,
            sandbox_mode=sandbox_mode,
            updated_at=updated_at,
            vm_max_uptime=vm_max_uptime,
        )

        app_runner_group_settings.additional_properties = d
        return app_runner_group_settings

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
