from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appbundle_finding import AppbundleFinding


T = TypeVar("T", bound="AppbundleQualificationReport")


@_attrs_define
class AppbundleQualificationReport:
    """
    Attributes:
        platform (str | Unset):
        qualified (bool | Unset):
        violations (list[AppbundleFinding] | Unset):
        warnings (list[AppbundleFinding] | Unset):
    """

    platform: str | Unset = UNSET
    qualified: bool | Unset = UNSET
    violations: list[AppbundleFinding] | Unset = UNSET
    warnings: list[AppbundleFinding] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        qualified = self.qualified

        violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.violations, Unset):
            violations = []
            for violations_item_data in self.violations:
                violations_item = violations_item_data.to_dict()
                violations.append(violations_item)

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if qualified is not UNSET:
            field_dict["qualified"] = qualified
        if violations is not UNSET:
            field_dict["violations"] = violations
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appbundle_finding import AppbundleFinding  # noqa: PLC0415

        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        qualified = d.pop("qualified", UNSET)

        _violations = d.pop("violations", UNSET)
        violations: list[AppbundleFinding] | Unset = UNSET
        if _violations is not UNSET:
            violations = []
            for violations_item_data in _violations:
                violations_item = AppbundleFinding.from_dict(violations_item_data)

                violations.append(violations_item)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[AppbundleFinding] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = AppbundleFinding.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        appbundle_qualification_report = cls(
            platform=platform,
            qualified=qualified,
            violations=violations,
            warnings=warnings,
        )

        appbundle_qualification_report.additional_properties = d
        return appbundle_qualification_report

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
