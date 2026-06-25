from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_aws_ecr_image_config_request import ServiceAwsECRImageConfigRequest
    from ..models.service_azure_acr_image_config_request import ServiceAzureACRImageConfigRequest
    from ..models.service_create_external_image_component_config_request_operation_roles import (
        ServiceCreateExternalImageComponentConfigRequestOperationRoles,
    )
    from ..models.service_gcp_gar_image_config_request import ServiceGcpGARImageConfigRequest


T = TypeVar("T", bound="ServiceCreateExternalImageComponentConfigRequest")


@_attrs_define
class ServiceCreateExternalImageComponentConfigRequest:
    """
    Attributes:
        image_url (str):
        app_config_id (str | Unset):
        auto_approve_on_policies_passing (bool | Unset):
        aws_ecr_image_config (ServiceAwsECRImageConfigRequest | Unset):
        azure_acr_image_config (ServiceAzureACRImageConfigRequest | Unset):
        build_timeout (str | Unset): Duration string for build operations (e.g., "30m", "1h")
        checksum (str | Unset):
        default_enabled (bool | Unset):
        dependencies (list[str] | Unset):
        deploy_timeout (str | Unset): Duration string for deploy operations (e.g., "30m", "1h")
        gcp_gar_image_config (ServiceGcpGARImageConfigRequest | Unset):
        max_auto_retries (int | Unset):
        operation_roles (ServiceCreateExternalImageComponentConfigRequestOperationRoles | Unset):
        references (list[str] | Unset):
        skip_noops (bool | Unset):
        tag (str | Unset):
        toggleable (bool | Unset):
        update_policy (str | Unset): UpdatePolicy is an optional Masterminds-compatible semver constraint
            (e.g. "~1.25.0", "^2"). When set, the runner lists tags from the
            source registry, filters to those satisfying the constraint, and
            uses the highest matching tag. Tag becomes optional in this case.
    """

    image_url: str
    app_config_id: str | Unset = UNSET
    auto_approve_on_policies_passing: bool | Unset = UNSET
    aws_ecr_image_config: ServiceAwsECRImageConfigRequest | Unset = UNSET
    azure_acr_image_config: ServiceAzureACRImageConfigRequest | Unset = UNSET
    build_timeout: str | Unset = UNSET
    checksum: str | Unset = UNSET
    default_enabled: bool | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    deploy_timeout: str | Unset = UNSET
    gcp_gar_image_config: ServiceGcpGARImageConfigRequest | Unset = UNSET
    max_auto_retries: int | Unset = UNSET
    operation_roles: ServiceCreateExternalImageComponentConfigRequestOperationRoles | Unset = UNSET
    references: list[str] | Unset = UNSET
    skip_noops: bool | Unset = UNSET
    tag: str | Unset = UNSET
    toggleable: bool | Unset = UNSET
    update_policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        app_config_id = self.app_config_id

        auto_approve_on_policies_passing = self.auto_approve_on_policies_passing

        aws_ecr_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_ecr_image_config, Unset):
            aws_ecr_image_config = self.aws_ecr_image_config.to_dict()

        azure_acr_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_acr_image_config, Unset):
            azure_acr_image_config = self.azure_acr_image_config.to_dict()

        build_timeout = self.build_timeout

        checksum = self.checksum

        default_enabled = self.default_enabled

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        deploy_timeout = self.deploy_timeout

        gcp_gar_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_gar_image_config, Unset):
            gcp_gar_image_config = self.gcp_gar_image_config.to_dict()

        max_auto_retries = self.max_auto_retries

        operation_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operation_roles, Unset):
            operation_roles = self.operation_roles.to_dict()

        references: list[str] | Unset = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        skip_noops = self.skip_noops

        tag = self.tag

        toggleable = self.toggleable

        update_policy = self.update_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_url": image_url,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if auto_approve_on_policies_passing is not UNSET:
            field_dict["auto_approve_on_policies_passing"] = auto_approve_on_policies_passing
        if aws_ecr_image_config is not UNSET:
            field_dict["aws_ecr_image_config"] = aws_ecr_image_config
        if azure_acr_image_config is not UNSET:
            field_dict["azure_acr_image_config"] = azure_acr_image_config
        if build_timeout is not UNSET:
            field_dict["build_timeout"] = build_timeout
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if default_enabled is not UNSET:
            field_dict["default_enabled"] = default_enabled
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if deploy_timeout is not UNSET:
            field_dict["deploy_timeout"] = deploy_timeout
        if gcp_gar_image_config is not UNSET:
            field_dict["gcp_gar_image_config"] = gcp_gar_image_config
        if max_auto_retries is not UNSET:
            field_dict["max_auto_retries"] = max_auto_retries
        if operation_roles is not UNSET:
            field_dict["operation_roles"] = operation_roles
        if references is not UNSET:
            field_dict["references"] = references
        if skip_noops is not UNSET:
            field_dict["skip_noops"] = skip_noops
        if tag is not UNSET:
            field_dict["tag"] = tag
        if toggleable is not UNSET:
            field_dict["toggleable"] = toggleable
        if update_policy is not UNSET:
            field_dict["update_policy"] = update_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_aws_ecr_image_config_request import ServiceAwsECRImageConfigRequest
        from ..models.service_azure_acr_image_config_request import ServiceAzureACRImageConfigRequest
        from ..models.service_create_external_image_component_config_request_operation_roles import (
            ServiceCreateExternalImageComponentConfigRequestOperationRoles,
        )
        from ..models.service_gcp_gar_image_config_request import ServiceGcpGARImageConfigRequest

        d = dict(src_dict)
        image_url = d.pop("image_url")

        app_config_id = d.pop("app_config_id", UNSET)

        auto_approve_on_policies_passing = d.pop("auto_approve_on_policies_passing", UNSET)

        _aws_ecr_image_config = d.pop("aws_ecr_image_config", UNSET)
        aws_ecr_image_config: ServiceAwsECRImageConfigRequest | Unset
        if isinstance(_aws_ecr_image_config, Unset):
            aws_ecr_image_config = UNSET
        else:
            aws_ecr_image_config = ServiceAwsECRImageConfigRequest.from_dict(_aws_ecr_image_config)

        _azure_acr_image_config = d.pop("azure_acr_image_config", UNSET)
        azure_acr_image_config: ServiceAzureACRImageConfigRequest | Unset
        if isinstance(_azure_acr_image_config, Unset):
            azure_acr_image_config = UNSET
        else:
            azure_acr_image_config = ServiceAzureACRImageConfigRequest.from_dict(_azure_acr_image_config)

        build_timeout = d.pop("build_timeout", UNSET)

        checksum = d.pop("checksum", UNSET)

        default_enabled = d.pop("default_enabled", UNSET)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        deploy_timeout = d.pop("deploy_timeout", UNSET)

        _gcp_gar_image_config = d.pop("gcp_gar_image_config", UNSET)
        gcp_gar_image_config: ServiceGcpGARImageConfigRequest | Unset
        if isinstance(_gcp_gar_image_config, Unset):
            gcp_gar_image_config = UNSET
        else:
            gcp_gar_image_config = ServiceGcpGARImageConfigRequest.from_dict(_gcp_gar_image_config)

        max_auto_retries = d.pop("max_auto_retries", UNSET)

        _operation_roles = d.pop("operation_roles", UNSET)
        operation_roles: ServiceCreateExternalImageComponentConfigRequestOperationRoles | Unset
        if isinstance(_operation_roles, Unset):
            operation_roles = UNSET
        else:
            operation_roles = ServiceCreateExternalImageComponentConfigRequestOperationRoles.from_dict(_operation_roles)

        references = cast(list[str], d.pop("references", UNSET))

        skip_noops = d.pop("skip_noops", UNSET)

        tag = d.pop("tag", UNSET)

        toggleable = d.pop("toggleable", UNSET)

        update_policy = d.pop("update_policy", UNSET)

        service_create_external_image_component_config_request = cls(
            image_url=image_url,
            app_config_id=app_config_id,
            auto_approve_on_policies_passing=auto_approve_on_policies_passing,
            aws_ecr_image_config=aws_ecr_image_config,
            azure_acr_image_config=azure_acr_image_config,
            build_timeout=build_timeout,
            checksum=checksum,
            default_enabled=default_enabled,
            dependencies=dependencies,
            deploy_timeout=deploy_timeout,
            gcp_gar_image_config=gcp_gar_image_config,
            max_auto_retries=max_auto_retries,
            operation_roles=operation_roles,
            references=references,
            skip_noops=skip_noops,
            tag=tag,
            toggleable=toggleable,
            update_policy=update_policy,
        )

        service_create_external_image_component_config_request.additional_properties = d
        return service_create_external_image_component_config_request

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
