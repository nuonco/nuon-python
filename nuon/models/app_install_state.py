from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallState")


@_attrs_define
class AppInstallState:
    """
    Attributes:
        archived (Union[Unset, bool]):
        contents (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_id (Union[Unset, str]):
        triggered_by_id (Union[Unset, str]):
        triggered_by_type (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        version (Union[Unset, int]):
    """

    archived: Union[Unset, bool] = UNSET
    contents: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_id: Union[Unset, str] = UNSET
    triggered_by_id: Union[Unset, str] = UNSET
    triggered_by_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        contents = self.contents

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        triggered_by_id = self.triggered_by_id

        triggered_by_type = self.triggered_by_type

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if contents is not UNSET:
            field_dict["contents"] = contents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if triggered_by_id is not UNSET:
            field_dict["triggered_by_id"] = triggered_by_id
        if triggered_by_type is not UNSET:
            field_dict["triggered_by_type"] = triggered_by_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        contents = d.pop("contents", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        triggered_by_id = d.pop("triggered_by_id", UNSET)

        triggered_by_type = d.pop("triggered_by_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        app_install_state = cls(
            archived=archived,
            contents=contents,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            triggered_by_id=triggered_by_id,
            triggered_by_type=triggered_by_type,
            updated_at=updated_at,
            version=version,
        )

        app_install_state.additional_properties = d
        return app_install_state

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
