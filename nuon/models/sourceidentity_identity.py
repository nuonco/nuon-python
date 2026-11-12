from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourceidentity_file import SourceidentityFile
    from ..models.sourceidentity_input import SourceidentityInput


T = TypeVar("T", bound="SourceidentityIdentity")


@_attrs_define
class SourceidentityIdentity:
    """
    Attributes:
        captured (bool | Unset):
        chart_version (str | Unset):
        checksum (str | Unset):
        commit (str | Unset):
        config_checksum (str | Unset):
        coverage (str | Unset):
        digest (str | Unset):
        files (list[SourceidentityFile] | Unset):
        inputs (list[SourceidentityInput] | Unset):
        inputs_recorded (bool | Unset):
        kind (str | Unset):
        reasons (list[str] | Unset):
        ref (str | Unset):
        repository (str | Unset):
        resolved_at (str | Unset):
        resolved_from (str | Unset):
        root (str | Unset):
        version (int | Unset):
    """

    captured: bool | Unset = UNSET
    chart_version: str | Unset = UNSET
    checksum: str | Unset = UNSET
    commit: str | Unset = UNSET
    config_checksum: str | Unset = UNSET
    coverage: str | Unset = UNSET
    digest: str | Unset = UNSET
    files: list[SourceidentityFile] | Unset = UNSET
    inputs: list[SourceidentityInput] | Unset = UNSET
    inputs_recorded: bool | Unset = UNSET
    kind: str | Unset = UNSET
    reasons: list[str] | Unset = UNSET
    ref: str | Unset = UNSET
    repository: str | Unset = UNSET
    resolved_at: str | Unset = UNSET
    resolved_from: str | Unset = UNSET
    root: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captured = self.captured

        chart_version = self.chart_version

        checksum = self.checksum

        commit = self.commit

        config_checksum = self.config_checksum

        coverage = self.coverage

        digest = self.digest

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        inputs_recorded = self.inputs_recorded

        kind = self.kind

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        ref = self.ref

        repository = self.repository

        resolved_at = self.resolved_at

        resolved_from = self.resolved_from

        root = self.root

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captured is not UNSET:
            field_dict["captured"] = captured
        if chart_version is not UNSET:
            field_dict["chart_version"] = chart_version
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if commit is not UNSET:
            field_dict["commit"] = commit
        if config_checksum is not UNSET:
            field_dict["config_checksum"] = config_checksum
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if digest is not UNSET:
            field_dict["digest"] = digest
        if files is not UNSET:
            field_dict["files"] = files
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if inputs_recorded is not UNSET:
            field_dict["inputs_recorded"] = inputs_recorded
        if kind is not UNSET:
            field_dict["kind"] = kind
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if ref is not UNSET:
            field_dict["ref"] = ref
        if repository is not UNSET:
            field_dict["repository"] = repository
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if resolved_from is not UNSET:
            field_dict["resolved_from"] = resolved_from
        if root is not UNSET:
            field_dict["root"] = root
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sourceidentity_file import SourceidentityFile  # noqa: PLC0415
        from ..models.sourceidentity_input import SourceidentityInput  # noqa: PLC0415

        d = dict(src_dict)
        captured = d.pop("captured", UNSET)

        chart_version = d.pop("chart_version", UNSET)

        checksum = d.pop("checksum", UNSET)

        commit = d.pop("commit", UNSET)

        config_checksum = d.pop("config_checksum", UNSET)

        coverage = d.pop("coverage", UNSET)

        digest = d.pop("digest", UNSET)

        _files = d.pop("files", UNSET)
        files: list[SourceidentityFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = SourceidentityFile.from_dict(files_item_data)

                files.append(files_item)

        _inputs = d.pop("inputs", UNSET)
        inputs: list[SourceidentityInput] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = SourceidentityInput.from_dict(inputs_item_data)

                inputs.append(inputs_item)

        inputs_recorded = d.pop("inputs_recorded", UNSET)

        kind = d.pop("kind", UNSET)

        reasons = cast(list[str], d.pop("reasons", UNSET))

        ref = d.pop("ref", UNSET)

        repository = d.pop("repository", UNSET)

        resolved_at = d.pop("resolved_at", UNSET)

        resolved_from = d.pop("resolved_from", UNSET)

        root = d.pop("root", UNSET)

        version = d.pop("version", UNSET)

        sourceidentity_identity = cls(
            captured=captured,
            chart_version=chart_version,
            checksum=checksum,
            commit=commit,
            config_checksum=config_checksum,
            coverage=coverage,
            digest=digest,
            files=files,
            inputs=inputs,
            inputs_recorded=inputs_recorded,
            kind=kind,
            reasons=reasons,
            ref=ref,
            repository=repository,
            resolved_at=resolved_at,
            resolved_from=resolved_from,
            root=root,
            version=version,
        )

        sourceidentity_identity.additional_properties = d
        return sourceidentity_identity

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
