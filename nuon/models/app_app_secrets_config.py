from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_secret_config import AppAppSecretConfig


T = TypeVar("T", bound="AppAppSecretsConfig")


@_attrs_define
class AppAppSecretsConfig:
    """
    Attributes:
        app_config_id (str | Unset):
        app_id (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        secrets (list[AppAppSecretConfig] | Unset):
        updated_at (str | Unset):
    """

    app_config_id: str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    secrets: list[AppAppSecretConfig] | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        app_id = self.app_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_secret_config import AppAppSecretConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[AppAppSecretConfig] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = AppAppSecretConfig.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        updated_at = d.pop("updated_at", UNSET)

        app_app_secrets_config = cls(
            app_config_id=app_config_id,
            app_id=app_id,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            secrets=secrets,
            updated_at=updated_at,
        )

        app_app_secrets_config.additional_properties = d
        return app_app_secrets_config

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
