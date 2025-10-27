from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppTerraformLock")


@_attrs_define
class AppTerraformLock:
    """
    Attributes:
        created (Union[Unset, str]):
        id (Union[Unset, str]):
        info (Union[Unset, str]):
        operation (Union[Unset, str]):
        path (Union[Unset, str]):
        version (Union[Unset, Any]):
        who (Union[Unset, str]):
    """

    created: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    info: Union[Unset, str] = UNSET
    operation: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    version: Union[Unset, Any] = UNSET
    who: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        id = self.id

        info = self.info

        operation = self.operation

        path = self.path

        version = self.version

        who = self.who

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if info is not UNSET:
            field_dict["info"] = info
        if operation is not UNSET:
            field_dict["operation"] = operation
        if path is not UNSET:
            field_dict["path"] = path
        if version is not UNSET:
            field_dict["version"] = version
        if who is not UNSET:
            field_dict["who"] = who

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        id = d.pop("id", UNSET)

        info = d.pop("info", UNSET)

        operation = d.pop("operation", UNSET)

        path = d.pop("path", UNSET)

        version = d.pop("version", UNSET)

        who = d.pop("who", UNSET)

        app_terraform_lock = cls(
            created=created,
            id=id,
            info=info,
            operation=operation,
            path=path,
            version=version,
            who=who,
        )

        app_terraform_lock.additional_properties = d
        return app_terraform_lock

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
