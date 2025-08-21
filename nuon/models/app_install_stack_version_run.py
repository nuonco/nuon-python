from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_stack_version_run_data import AppInstallStackVersionRunData


T = TypeVar("T", bound="AppInstallStackVersionRun")


@_attrs_define
class AppInstallStackVersionRun:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        data (Union[Unset, AppInstallStackVersionRunData]):
        id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    data: Union[Unset, "AppInstallStackVersionRunData"] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        id = self.id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_stack_version_run_data import AppInstallStackVersionRunData

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, AppInstallStackVersionRunData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AppInstallStackVersionRunData.from_dict(_data)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_stack_version_run = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            data=data,
            id=id,
            updated_at=updated_at,
        )

        app_install_stack_version_run.additional_properties = d
        return app_install_stack_version_run

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
