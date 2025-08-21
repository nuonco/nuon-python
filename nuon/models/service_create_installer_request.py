from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_installer_request_metadata import ServiceCreateInstallerRequestMetadata


T = TypeVar("T", bound="ServiceCreateInstallerRequest")


@_attrs_define
class ServiceCreateInstallerRequest:
    """
    Attributes:
        app_ids (list[str]):
        name (str):
        metadata (Union[Unset, ServiceCreateInstallerRequestMetadata]):
    """

    app_ids: list[str]
    name: str
    metadata: Union[Unset, "ServiceCreateInstallerRequestMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_ids = self.app_ids

        name = self.name

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_ids": app_ids,
                "name": name,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_installer_request_metadata import ServiceCreateInstallerRequestMetadata

        d = dict(src_dict)
        app_ids = cast(list[str], d.pop("app_ids"))

        name = d.pop("name")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ServiceCreateInstallerRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ServiceCreateInstallerRequestMetadata.from_dict(_metadata)

        service_create_installer_request = cls(
            app_ids=app_ids,
            name=name,
            metadata=metadata,
        )

        service_create_installer_request.additional_properties = d
        return service_create_installer_request

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
