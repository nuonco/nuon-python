from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateInstallRequestAzureAccount")


@_attrs_define
class ServiceCreateInstallRequestAzureAccount:
    """
    Attributes:
        location (Union[Unset, str]):
        service_principal_app_id (Union[Unset, str]):
        service_principal_password (Union[Unset, str]):
        subscription_id (Union[Unset, str]):
        subscription_tenant_id (Union[Unset, str]):
    """

    location: Union[Unset, str] = UNSET
    service_principal_app_id: Union[Unset, str] = UNSET
    service_principal_password: Union[Unset, str] = UNSET
    subscription_id: Union[Unset, str] = UNSET
    subscription_tenant_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        service_principal_app_id = self.service_principal_app_id

        service_principal_password = self.service_principal_password

        subscription_id = self.subscription_id

        subscription_tenant_id = self.subscription_tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if service_principal_app_id is not UNSET:
            field_dict["service_principal_app_id"] = service_principal_app_id
        if service_principal_password is not UNSET:
            field_dict["service_principal_password"] = service_principal_password
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if subscription_tenant_id is not UNSET:
            field_dict["subscription_tenant_id"] = subscription_tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = d.pop("location", UNSET)

        service_principal_app_id = d.pop("service_principal_app_id", UNSET)

        service_principal_password = d.pop("service_principal_password", UNSET)

        subscription_id = d.pop("subscription_id", UNSET)

        subscription_tenant_id = d.pop("subscription_tenant_id", UNSET)

        service_create_install_request_azure_account = cls(
            location=location,
            service_principal_app_id=service_principal_app_id,
            service_principal_password=service_principal_password,
            subscription_id=subscription_id,
            subscription_tenant_id=subscription_tenant_id,
        )

        service_create_install_request_azure_account.additional_properties = d
        return service_create_install_request_azure_account

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
