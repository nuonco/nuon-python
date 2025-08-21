from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppTerraformWorkspace")


@_attrs_define
class AppTerraformWorkspace:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        owner_id (Union[Unset, str]):
        owner_type (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    owner_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_terraform_workspace = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            updated_at=updated_at,
        )

        app_terraform_workspace.additional_properties = d
        return app_terraform_workspace

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
