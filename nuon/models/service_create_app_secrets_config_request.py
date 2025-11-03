from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_secret_config import ServiceAppSecretConfig


T = TypeVar("T", bound="ServiceCreateAppSecretsConfigRequest")


@_attrs_define
class ServiceCreateAppSecretsConfigRequest:
    """
    Attributes:
        app_config_id (str):
        secrets (list[ServiceAppSecretConfig] | Unset):
    """

    app_config_id: str
    secrets: list[ServiceAppSecretConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
            }
        )
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_secret_config import ServiceAppSecretConfig

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        _secrets = d.pop("secrets", UNSET)
        secrets: list[ServiceAppSecretConfig] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = ServiceAppSecretConfig.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        service_create_app_secrets_config_request = cls(
            app_config_id=app_config_id,
            secrets=secrets,
        )

        service_create_app_secrets_config_request.additional_properties = d
        return service_create_app_secrets_config_request

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
