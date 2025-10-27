from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceReadme")


@_attrs_define
class ServiceReadme:
    """
    Attributes:
        original (Union[Unset, str]):
        readme (Union[Unset, str]):
        warnings (Union[Unset, list[str]]):
    """

    original: Union[Unset, str] = UNSET
    readme: Union[Unset, str] = UNSET
    warnings: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original = self.original

        readme = self.readme

        warnings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original is not UNSET:
            field_dict["original"] = original
        if readme is not UNSET:
            field_dict["readme"] = readme
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        original = d.pop("original", UNSET)

        readme = d.pop("readme", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        service_readme = cls(
            original=original,
            readme=readme,
            warnings=warnings,
        )

        service_readme.additional_properties = d
        return service_readme

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
