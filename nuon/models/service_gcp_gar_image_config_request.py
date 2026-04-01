from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceGcpGARImageConfigRequest")


@_attrs_define
class ServiceGcpGARImageConfigRequest:
    """
    Attributes:
        gcp_project_id (str | Unset):
        gcp_region (str | Unset):
        image_url (str | Unset):
        service_account_email (str | Unset):
        tag (str | Unset):
        workload_identity_provider (str | Unset):
    """

    gcp_project_id: str | Unset = UNSET
    gcp_region: str | Unset = UNSET
    image_url: str | Unset = UNSET
    service_account_email: str | Unset = UNSET
    tag: str | Unset = UNSET
    workload_identity_provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gcp_project_id = self.gcp_project_id

        gcp_region = self.gcp_region

        image_url = self.image_url

        service_account_email = self.service_account_email

        tag = self.tag

        workload_identity_provider = self.workload_identity_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gcp_project_id is not UNSET:
            field_dict["gcp_project_id"] = gcp_project_id
        if gcp_region is not UNSET:
            field_dict["gcp_region"] = gcp_region
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if service_account_email is not UNSET:
            field_dict["service_account_email"] = service_account_email
        if tag is not UNSET:
            field_dict["tag"] = tag
        if workload_identity_provider is not UNSET:
            field_dict["workload_identity_provider"] = workload_identity_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gcp_project_id = d.pop("gcp_project_id", UNSET)

        gcp_region = d.pop("gcp_region", UNSET)

        image_url = d.pop("image_url", UNSET)

        service_account_email = d.pop("service_account_email", UNSET)

        tag = d.pop("tag", UNSET)

        workload_identity_provider = d.pop("workload_identity_provider", UNSET)

        service_gcp_gar_image_config_request = cls(
            gcp_project_id=gcp_project_id,
            gcp_region=gcp_region,
            image_url=image_url,
            service_account_email=service_account_email,
            tag=tag,
            workload_identity_provider=workload_identity_provider,
        )

        service_gcp_gar_image_config_request.additional_properties = d
        return service_gcp_gar_image_config_request

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
