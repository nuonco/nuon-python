from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_runner_group_settings_aws_tags import AppRunnerGroupSettingsAwsTags
    from ..models.app_runner_group_settings_metadata import AppRunnerGroupSettingsMetadata


T = TypeVar("T", bound="AppRunnerGroupSettings")


@_attrs_define
class AppRunnerGroupSettings:
    """
    Attributes:
        aws_cloudformation_stack_type (Union[Unset, str]):
        aws_instance_type (Union[Unset, str]): aws runner specifics runner-v2
        aws_max_instance_lifetime (Union[Unset, int]): Default: 7 days
        aws_tags (Union[Unset, AppRunnerGroupSettingsAwsTags]):
        container_image_tag (Union[Unset, str]):
        container_image_url (Union[Unset, str]): configuration for deploying the runner
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        enable_logging (Union[Unset, bool]):
        enable_metrics (Union[Unset, bool]):
        enable_sentry (Union[Unset, bool]):
        groups (Union[Unset, list[str]]): the job loop groups the runner should poll for
        heart_beat_timeout (Union[Unset, int]): Various settings for the runner to handle internally
        id (Union[Unset, str]):
        local_aws_iam_role_arn (Union[Unset, str]):
        logging_level (Union[Unset, str]):
        metadata (Union[Unset, AppRunnerGroupSettingsMetadata]): Metadata is used as both log and metric tags/attributes
            in the runner when emitting data
        org_aws_iam_role_arn (Union[Unset, str]): org runner specifics
        org_id (Union[Unset, str]):
        org_k8s_service_account_name (Union[Unset, str]):
        otel_collector_config (Union[Unset, str]):
        platform (Union[Unset, str]): platform variable for use in the runner
        runner_api_url (Union[Unset, str]):
        runner_group_id (Union[Unset, str]):
        sandbox_mode (Union[Unset, bool]): configuration for managing the runner server side
        updated_at (Union[Unset, str]):
    """

    aws_cloudformation_stack_type: Union[Unset, str] = UNSET
    aws_instance_type: Union[Unset, str] = UNSET
    aws_max_instance_lifetime: Union[Unset, int] = UNSET
    aws_tags: Union[Unset, "AppRunnerGroupSettingsAwsTags"] = UNSET
    container_image_tag: Union[Unset, str] = UNSET
    container_image_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    enable_logging: Union[Unset, bool] = UNSET
    enable_metrics: Union[Unset, bool] = UNSET
    enable_sentry: Union[Unset, bool] = UNSET
    groups: Union[Unset, list[str]] = UNSET
    heart_beat_timeout: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    local_aws_iam_role_arn: Union[Unset, str] = UNSET
    logging_level: Union[Unset, str] = UNSET
    metadata: Union[Unset, "AppRunnerGroupSettingsMetadata"] = UNSET
    org_aws_iam_role_arn: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    org_k8s_service_account_name: Union[Unset, str] = UNSET
    otel_collector_config: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    runner_api_url: Union[Unset, str] = UNSET
    runner_group_id: Union[Unset, str] = UNSET
    sandbox_mode: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_cloudformation_stack_type = self.aws_cloudformation_stack_type

        aws_instance_type = self.aws_instance_type

        aws_max_instance_lifetime = self.aws_max_instance_lifetime

        aws_tags: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws_tags, Unset):
            aws_tags = self.aws_tags.to_dict()

        container_image_tag = self.container_image_tag

        container_image_url = self.container_image_url

        created_at = self.created_at

        created_by_id = self.created_by_id

        enable_logging = self.enable_logging

        enable_metrics = self.enable_metrics

        enable_sentry = self.enable_sentry

        groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        heart_beat_timeout = self.heart_beat_timeout

        id = self.id

        local_aws_iam_role_arn = self.local_aws_iam_role_arn

        logging_level = self.logging_level

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        org_aws_iam_role_arn = self.org_aws_iam_role_arn

        org_id = self.org_id

        org_k8s_service_account_name = self.org_k8s_service_account_name

        otel_collector_config = self.otel_collector_config

        platform = self.platform

        runner_api_url = self.runner_api_url

        runner_group_id = self.runner_group_id

        sandbox_mode = self.sandbox_mode

        updated_at = self.updated_at

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
        if container_image_tag is not UNSET:
            field_dict["container_image_tag"] = container_image_tag
        if container_image_url is not UNSET:
            field_dict["container_image_url"] = container_image_url
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
        if local_aws_iam_role_arn is not UNSET:
            field_dict["local_aws_iam_role_arn"] = local_aws_iam_role_arn
        if logging_level is not UNSET:
            field_dict["logging_level"] = logging_level
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if org_aws_iam_role_arn is not UNSET:
            field_dict["org_aws_iam_role_arn"] = org_aws_iam_role_arn
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
        if runner_group_id is not UNSET:
            field_dict["runner_group_id"] = runner_group_id
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_runner_group_settings_aws_tags import AppRunnerGroupSettingsAwsTags
        from ..models.app_runner_group_settings_metadata import AppRunnerGroupSettingsMetadata

        d = dict(src_dict)
        aws_cloudformation_stack_type = d.pop("aws_cloudformation_stack_type", UNSET)

        aws_instance_type = d.pop("aws_instance_type", UNSET)

        aws_max_instance_lifetime = d.pop("aws_max_instance_lifetime", UNSET)

        _aws_tags = d.pop("aws_tags", UNSET)
        aws_tags: Union[Unset, AppRunnerGroupSettingsAwsTags]
        if isinstance(_aws_tags, Unset):
            aws_tags = UNSET
        else:
            aws_tags = AppRunnerGroupSettingsAwsTags.from_dict(_aws_tags)

        container_image_tag = d.pop("container_image_tag", UNSET)

        container_image_url = d.pop("container_image_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        enable_logging = d.pop("enable_logging", UNSET)

        enable_metrics = d.pop("enable_metrics", UNSET)

        enable_sentry = d.pop("enable_sentry", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))

        heart_beat_timeout = d.pop("heart_beat_timeout", UNSET)

        id = d.pop("id", UNSET)

        local_aws_iam_role_arn = d.pop("local_aws_iam_role_arn", UNSET)

        logging_level = d.pop("logging_level", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AppRunnerGroupSettingsMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppRunnerGroupSettingsMetadata.from_dict(_metadata)

        org_aws_iam_role_arn = d.pop("org_aws_iam_role_arn", UNSET)

        org_id = d.pop("org_id", UNSET)

        org_k8s_service_account_name = d.pop("org_k8s_service_account_name", UNSET)

        otel_collector_config = d.pop("otel_collector_config", UNSET)

        platform = d.pop("platform", UNSET)

        runner_api_url = d.pop("runner_api_url", UNSET)

        runner_group_id = d.pop("runner_group_id", UNSET)

        sandbox_mode = d.pop("sandbox_mode", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_runner_group_settings = cls(
            aws_cloudformation_stack_type=aws_cloudformation_stack_type,
            aws_instance_type=aws_instance_type,
            aws_max_instance_lifetime=aws_max_instance_lifetime,
            aws_tags=aws_tags,
            container_image_tag=container_image_tag,
            container_image_url=container_image_url,
            created_at=created_at,
            created_by_id=created_by_id,
            enable_logging=enable_logging,
            enable_metrics=enable_metrics,
            enable_sentry=enable_sentry,
            groups=groups,
            heart_beat_timeout=heart_beat_timeout,
            id=id,
            local_aws_iam_role_arn=local_aws_iam_role_arn,
            logging_level=logging_level,
            metadata=metadata,
            org_aws_iam_role_arn=org_aws_iam_role_arn,
            org_id=org_id,
            org_k8s_service_account_name=org_k8s_service_account_name,
            otel_collector_config=otel_collector_config,
            platform=platform,
            runner_api_url=runner_api_url,
            runner_group_id=runner_group_id,
            sandbox_mode=sandbox_mode,
            updated_at=updated_at,
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
