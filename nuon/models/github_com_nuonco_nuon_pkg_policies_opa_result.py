from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opa_evaluation_error import OpaEvaluationError
    from ..models.opa_finding import OpaFinding


T = TypeVar("T", bound="GithubComNuoncoNuonPkgPoliciesOpaResult")


@_attrs_define
class GithubComNuoncoNuonPkgPoliciesOpaResult:
    """
    Attributes:
        check_id (str | Unset):
        decision (str | Unset):
        description (str | Unset):
        errors (list[OpaEvaluationError] | Unset):
        findings (list[OpaFinding] | Unset):
        input_count (int | Unset):
        title (str | Unset):
    """

    check_id: str | Unset = UNSET
    decision: str | Unset = UNSET
    description: str | Unset = UNSET
    errors: list[OpaEvaluationError] | Unset = UNSET
    findings: list[OpaFinding] | Unset = UNSET
    input_count: int | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_id = self.check_id

        decision = self.decision

        description = self.description

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        findings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.findings, Unset):
            findings = []
            for findings_item_data in self.findings:
                findings_item = findings_item_data.to_dict()
                findings.append(findings_item)

        input_count = self.input_count

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_id is not UNSET:
            field_dict["check_id"] = check_id
        if decision is not UNSET:
            field_dict["decision"] = decision
        if description is not UNSET:
            field_dict["description"] = description
        if errors is not UNSET:
            field_dict["errors"] = errors
        if findings is not UNSET:
            field_dict["findings"] = findings
        if input_count is not UNSET:
            field_dict["input_count"] = input_count
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opa_evaluation_error import OpaEvaluationError  # noqa: PLC0415
        from ..models.opa_finding import OpaFinding  # noqa: PLC0415

        d = dict(src_dict)
        check_id = d.pop("check_id", UNSET)

        decision = d.pop("decision", UNSET)

        description = d.pop("description", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[OpaEvaluationError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = OpaEvaluationError.from_dict(errors_item_data)

                errors.append(errors_item)

        _findings = d.pop("findings", UNSET)
        findings: list[OpaFinding] | Unset = UNSET
        if _findings is not UNSET:
            findings = []
            for findings_item_data in _findings:
                findings_item = OpaFinding.from_dict(findings_item_data)

                findings.append(findings_item)

        input_count = d.pop("input_count", UNSET)

        title = d.pop("title", UNSET)

        github_com_nuonco_nuon_pkg_policies_opa_result = cls(
            check_id=check_id,
            decision=decision,
            description=description,
            errors=errors,
            findings=findings,
            input_count=input_count,
            title=title,
        )

        github_com_nuonco_nuon_pkg_policies_opa_result.additional_properties = d
        return github_com_nuonco_nuon_pkg_policies_opa_result

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
