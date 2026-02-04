from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_aws_ecr_image_config_request import ServiceAwsECRImageConfigRequest


T = TypeVar("T", bound="ServiceCreateExternalImageComponentConfigRequest")


@_attrs_define
class ServiceCreateExternalImageComponentConfigRequest:
    """
    Attributes:
        image_url (str):
        tag (str):
        app_config_id (str | Unset):
        aws_ecr_image_config (ServiceAwsECRImageConfigRequest | Unset):
        build_timeout (str | Unset): Duration string for build operations (e.g., "30m", "1h")
        checksum (str | Unset):
        dependencies (list[str] | Unset):
        deploy_timeout (str | Unset): Duration string for deploy operations (e.g., "30m", "1h")
        references (list[str] | Unset):
    """

    image_url: str
    tag: str
    app_config_id: str | Unset = UNSET
    aws_ecr_image_config: ServiceAwsECRImageConfigRequest | Unset = UNSET
    build_timeout: str | Unset = UNSET
    checksum: str | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    deploy_timeout: str | Unset = UNSET
    references: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        tag = self.tag

        app_config_id = self.app_config_id

        aws_ecr_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_ecr_image_config, Unset):
            aws_ecr_image_config = self.aws_ecr_image_config.to_dict()

        build_timeout = self.build_timeout

        checksum = self.checksum

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        deploy_timeout = self.deploy_timeout

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
        if build_timeout is not UNSET:
            field_dict["build_timeout"] = build_timeout
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if deploy_timeout is not UNSET:
            field_dict["deploy_timeout"] = deploy_timeout
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_aws_ecr_image_config_request import ServiceAwsECRImageConfigRequest

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

        build_timeout = d.pop("build_timeout", UNSET)

        checksum = d.pop("checksum", UNSET)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        deploy_timeout = d.pop("deploy_timeout", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        service_create_external_image_component_config_request = cls(
            image_url=image_url,
            tag=tag,
            app_config_id=app_config_id,
            aws_ecr_image_config=aws_ecr_image_config,
            build_timeout=build_timeout,
            checksum=checksum,
            dependencies=dependencies,
            deploy_timeout=deploy_timeout,
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
