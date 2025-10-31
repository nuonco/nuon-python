from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_awsecr_image_config import AppAWSECRImageConfig


T = TypeVar("T", bound="AppExternalImageComponentConfig")


@_attrs_define
class AppExternalImageComponentConfig:
    """
    Attributes:
        aws_ecr_image_config (AppAWSECRImageConfig | Unset):
        component_config_connection_id (str | Unset): value
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        image_url (str | Unset):
        tag (str | Unset):
        updated_at (str | Unset):
    """

    aws_ecr_image_config: AppAWSECRImageConfig | Unset = UNSET
    component_config_connection_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    image_url: str | Unset = UNSET
    tag: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_ecr_image_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_ecr_image_config, Unset):
            aws_ecr_image_config = self.aws_ecr_image_config.to_dict()

        component_config_connection_id = self.component_config_connection_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        image_url = self.image_url

        tag = self.tag

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_ecr_image_config is not UNSET:
            field_dict["aws_ecr_image_config"] = aws_ecr_image_config
        if component_config_connection_id is not UNSET:
            field_dict["component_config_connection_id"] = component_config_connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if tag is not UNSET:
            field_dict["tag"] = tag
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_awsecr_image_config import AppAWSECRImageConfig

        d = dict(src_dict)
        _aws_ecr_image_config = d.pop("aws_ecr_image_config", UNSET)
        aws_ecr_image_config: AppAWSECRImageConfig | Unset
        if isinstance(_aws_ecr_image_config, Unset):
            aws_ecr_image_config = UNSET
        else:
            aws_ecr_image_config = AppAWSECRImageConfig.from_dict(_aws_ecr_image_config)

        component_config_connection_id = d.pop("component_config_connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        image_url = d.pop("image_url", UNSET)

        tag = d.pop("tag", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_external_image_component_config = cls(
            aws_ecr_image_config=aws_ecr_image_config,
            component_config_connection_id=component_config_connection_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            image_url=image_url,
            tag=tag,
            updated_at=updated_at,
        )

        app_external_image_component_config.additional_properties = d
        return app_external_image_component_config

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
