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
        tag (str):
        app_config_id (str | Unset):
        aws_ecr_image_config (ServiceAwsECRImageConfigRequest | Unset):
        azure_acr_image_config (ServiceAzureACRImageConfigRequest | Unset):
        build_timeout (str | Unset): Duration string for build operations (e.g., "30m", "1h")
        checksum (str | Unset):
        dependencies (list[str] | Unset):
        deploy_timeout (str | Unset): Duration string for deploy operations (e.g., "30m", "1h")
        gcp_gar_image_config (ServiceGcpGARImageConfigRequest | Unset):
        max_auto_retries (int | Unset):
        operation_roles (ServiceCreateExternalImageComponentConfigRequestOperationRoles | Unset):
        references (list[str] | Unset):
    """

    image_url: str
    tag: str
    app_config_id: str | Unset = UNSET
    aws_ecr_image_config: ServiceAwsECRImageConfigRequest | Unset = UNSET
    azure_acr_image_config: ServiceAzureACRImageConfigRequest | Unset = UNSET
    build_timeout: str | Unset = UNSET
    checksum: str | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    deploy_timeout: str | Unset = UNSET
    gcp_gar_image_config: ServiceGcpGARImageConfigRequest | Unset = UNSET
    max_auto_retries: int | Unset = UNSET
    operation_roles: ServiceCreateExternalImageComponentConfigRequestOperationRoles | Unset = UNSET
    references: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        tag = self.tag

        app_config_id = self.app_config_id

        aws_ecr_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_ecr_image_config, Unset):
            aws_ecr_image_config = self.aws_ecr_image_config.to_dict()

        azure_acr_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_acr_image_config, Unset):
            azure_acr_image_config = self.azure_acr_image_config.to_dict()

        build_timeout = self.build_timeout

        checksum = self.checksum

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_url": image_url,
                "tag": tag,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if aws_ecr_image_config is not UNSET:
            field_dict["aws_ecr_image_config"] = aws_ecr_image_config
        if azure_acr_image_config is not UNSET:
            field_dict["azure_acr_image_config"] = azure_acr_image_config
        if build_timeout is not UNSET:
            field_dict["build_timeout"] = build_timeout
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
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

        tag = d.pop("tag")

        app_config_id = d.pop("app_config_id", UNSET)

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

        service_create_external_image_component_config_request = cls(
            image_url=image_url,
            tag=tag,
            app_config_id=app_config_id,
            aws_ecr_image_config=aws_ecr_image_config,
            azure_acr_image_config=azure_acr_image_config,
            build_timeout=build_timeout,
            checksum=checksum,
            dependencies=dependencies,
            deploy_timeout=deploy_timeout,
            gcp_gar_image_config=gcp_gar_image_config,
            max_auto_retries=max_auto_retries,
            operation_roles=operation_roles,
            references=references,
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
