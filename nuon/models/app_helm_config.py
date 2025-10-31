from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_helm_config_values import AppHelmConfigValues


T = TypeVar("T", bound="AppHelmConfig")


@_attrs_define
class AppHelmConfig:
    """
    Attributes:
        chart_name (str | Unset):
        namespace (str | Unset):
        storage_driver (str | Unset):
        take_ownership (bool | Unset): Newer fields that we don't need to store as columns in the database
        values (AppHelmConfigValues | Unset):
        values_files (list[str] | Unset):
    """

    chart_name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    storage_driver: str | Unset = UNSET
    take_ownership: bool | Unset = UNSET
    values: AppHelmConfigValues | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chart_name = self.chart_name

        namespace = self.namespace

        storage_driver = self.storage_driver

        take_ownership = self.take_ownership

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chart_name is not UNSET:
            field_dict["chart_name"] = chart_name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if storage_driver is not UNSET:
            field_dict["storage_driver"] = storage_driver
        if take_ownership is not UNSET:
            field_dict["take_ownership"] = take_ownership
        if values is not UNSET:
            field_dict["values"] = values
        if values_files is not UNSET:
            field_dict["values_files"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_helm_config_values import AppHelmConfigValues

        d = dict(src_dict)
        chart_name = d.pop("chart_name", UNSET)

        namespace = d.pop("namespace", UNSET)

        storage_driver = d.pop("storage_driver", UNSET)

        take_ownership = d.pop("take_ownership", UNSET)

        _values = d.pop("values", UNSET)
        values: AppHelmConfigValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AppHelmConfigValues.from_dict(_values)

        values_files = cast(list[str], d.pop("values_files", UNSET))

        app_helm_config = cls(
            chart_name=chart_name,
            namespace=namespace,
            storage_driver=storage_driver,
            take_ownership=take_ownership,
            values=values,
            values_files=values_files,
        )

        app_helm_config.additional_properties = d
        return app_helm_config

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
