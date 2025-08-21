from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAppSecretConfig")


@_attrs_define
class AppAppSecretConfig:
    """
    Attributes:
        app_config_id (Union[Unset, str]):
        app_id (Union[Unset, str]):
        app_secrets_config_id (Union[Unset, str]):
        auto_generate (Union[Unset, bool]):
        cloudformation_param_name (Union[Unset, str]):
        cloudformation_stack_name (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        default (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        format_ (Union[Unset, str]):
        id (Union[Unset, str]):
        kubernetes_secret_name (Union[Unset, str]):
        kubernetes_secret_namespace (Union[Unset, str]):
        kubernetes_sync (Union[Unset, bool]): for syncing into kubernetes
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        required (Union[Unset, bool]):
        updated_at (Union[Unset, str]):
    """

    app_config_id: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    app_secrets_config_id: Union[Unset, str] = UNSET
    auto_generate: Union[Unset, bool] = UNSET
    cloudformation_param_name: Union[Unset, str] = UNSET
    cloudformation_stack_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    default: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    kubernetes_secret_name: Union[Unset, str] = UNSET
    kubernetes_secret_namespace: Union[Unset, str] = UNSET
    kubernetes_sync: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        app_secrets_config_id = self.app_secrets_config_id

        auto_generate = self.auto_generate

        cloudformation_param_name = self.cloudformation_param_name

        cloudformation_stack_name = self.cloudformation_stack_name

        created_at = self.created_at

        created_by_id = self.created_by_id

        default = self.default

        description = self.description

        display_name = self.display_name

        format_ = self.format_

        id = self.id

        kubernetes_secret_name = self.kubernetes_secret_name

        kubernetes_secret_namespace = self.kubernetes_secret_namespace

        kubernetes_sync = self.kubernetes_sync

        name = self.name

        org_id = self.org_id

        required = self.required

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_secrets_config_id is not UNSET:
            field_dict["app_secrets_config_id"] = app_secrets_config_id
        if auto_generate is not UNSET:
            field_dict["auto_generate"] = auto_generate
        if cloudformation_param_name is not UNSET:
            field_dict["cloudformation_param_name"] = cloudformation_param_name
        if cloudformation_stack_name is not UNSET:
            field_dict["cloudformation_stack_name"] = cloudformation_stack_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if kubernetes_secret_name is not UNSET:
            field_dict["kubernetes_secret_name"] = kubernetes_secret_name
        if kubernetes_secret_namespace is not UNSET:
            field_dict["kubernetes_secret_namespace"] = kubernetes_secret_namespace
        if kubernetes_sync is not UNSET:
            field_dict["kubernetes_sync"] = kubernetes_sync
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if required is not UNSET:
            field_dict["required"] = required
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        app_secrets_config_id = d.pop("app_secrets_config_id", UNSET)

        auto_generate = d.pop("auto_generate", UNSET)

        cloudformation_param_name = d.pop("cloudformation_param_name", UNSET)

        cloudformation_stack_name = d.pop("cloudformation_stack_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        format_ = d.pop("format", UNSET)

        id = d.pop("id", UNSET)

        kubernetes_secret_name = d.pop("kubernetes_secret_name", UNSET)

        kubernetes_secret_namespace = d.pop("kubernetes_secret_namespace", UNSET)

        kubernetes_sync = d.pop("kubernetes_sync", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        required = d.pop("required", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_app_secret_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            app_secrets_config_id=app_secrets_config_id,
            auto_generate=auto_generate,
            cloudformation_param_name=cloudformation_param_name,
            cloudformation_stack_name=cloudformation_stack_name,
            created_at=created_at,
            created_by_id=created_by_id,
            default=default,
            description=description,
            display_name=display_name,
            format_=format_,
            id=id,
            kubernetes_secret_name=kubernetes_secret_name,
            kubernetes_secret_namespace=kubernetes_secret_namespace,
            kubernetes_sync=kubernetes_sync,
            name=name,
            org_id=org_id,
            required=required,
            updated_at=updated_at,
        )

        app_app_secret_config.additional_properties = d
        return app_app_secret_config

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
