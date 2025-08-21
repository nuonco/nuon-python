from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app import AppApp
    from ..models.app_installer_metadata import AppInstallerMetadata


T = TypeVar("T", bound="ServiceRenderedInstaller")


@_attrs_define
class ServiceRenderedInstaller:
    """
    Attributes:
        apps (Union[Unset, list['AppApp']]):
        metadata (Union[Unset, AppInstallerMetadata]):
        sandbox_mode (Union[Unset, bool]):
    """

    apps: Union[Unset, list["AppApp"]] = UNSET
    metadata: Union[Unset, "AppInstallerMetadata"] = UNSET
    sandbox_mode: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps, Unset):
            apps = []
            for apps_item_data in self.apps:
                apps_item = apps_item_data.to_dict()
                apps.append(apps_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        sandbox_mode = self.sandbox_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps is not UNSET:
            field_dict["apps"] = apps
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app import AppApp
        from ..models.app_installer_metadata import AppInstallerMetadata

        d = dict(src_dict)
        apps = []
        _apps = d.pop("apps", UNSET)
        for apps_item_data in _apps or []:
            apps_item = AppApp.from_dict(apps_item_data)

            apps.append(apps_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AppInstallerMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AppInstallerMetadata.from_dict(_metadata)

        sandbox_mode = d.pop("sandbox_mode", UNSET)

        service_rendered_installer = cls(
            apps=apps,
            metadata=metadata,
            sandbox_mode=sandbox_mode,
        )

        service_rendered_installer.additional_properties = d
        return service_rendered_installer

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
