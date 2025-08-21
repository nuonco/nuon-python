from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_policy_name import AppPolicyName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_policy_permissions import AppPolicyPermissions


T = TypeVar("T", bound="AppPolicy")


@_attrs_define
class AppPolicy:
    """
    Attributes:
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, AppPolicyName]):
        permissions (Union[Unset, AppPolicyPermissions]): Permissions are used to track granular permissions for each
            domain
        role_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, AppPolicyName] = UNSET
    permissions: Union[Unset, "AppPolicyPermissions"] = UNSET
    role_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        role_id = self.role_id

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
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_policy_permissions import AppPolicyPermissions

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, AppPolicyName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = AppPolicyName(_name)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, AppPolicyPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = AppPolicyPermissions.from_dict(_permissions)

        role_id = d.pop("role_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_policy = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            name=name,
            permissions=permissions,
            role_id=role_id,
            updated_at=updated_at,
        )

        app_policy.additional_properties = d
        return app_policy

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
