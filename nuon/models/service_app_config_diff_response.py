from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_source_archive_diff import ConfigSourceArchiveDiff
    from ..models.diff_diff import DiffDiff
    from ..models.diff_diff_summary import DiffDiffSummary


T = TypeVar("T", bound="ServiceAppConfigDiffResponse")


@_attrs_define
class ServiceAppConfigDiffResponse:
    """
    Attributes:
        changed (str | Unset):
        config_id (str | Unset):
        diff (DiffDiff | Unset):
        old_config_id (str | Unset):
        source (ConfigSourceArchiveDiff | Unset):
        source_skipped (bool | Unset):
        summary (DiffDiffSummary | Unset):
    """

    changed: str | Unset = UNSET
    config_id: str | Unset = UNSET
    diff: DiffDiff | Unset = UNSET
    old_config_id: str | Unset = UNSET
    source: ConfigSourceArchiveDiff | Unset = UNSET
    source_skipped: bool | Unset = UNSET
    summary: DiffDiffSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        config_id = self.config_id

        diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        old_config_id = self.old_config_id

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        source_skipped = self.source_skipped

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed
        if config_id is not UNSET:
            field_dict["config_id"] = config_id
        if diff is not UNSET:
            field_dict["diff"] = diff
        if old_config_id is not UNSET:
            field_dict["old_config_id"] = old_config_id
        if source is not UNSET:
            field_dict["source"] = source
        if source_skipped is not UNSET:
            field_dict["source_skipped"] = source_skipped
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_source_archive_diff import ConfigSourceArchiveDiff  # noqa: PLC0415
        from ..models.diff_diff import DiffDiff  # noqa: PLC0415
        from ..models.diff_diff_summary import DiffDiffSummary  # noqa: PLC0415

        d = dict(src_dict)
        changed = d.pop("changed", UNSET)

        config_id = d.pop("config_id", UNSET)

        _diff = d.pop("diff", UNSET)
        diff: DiffDiff | Unset
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = DiffDiff.from_dict(_diff)

        old_config_id = d.pop("old_config_id", UNSET)

        _source = d.pop("source", UNSET)
        source: ConfigSourceArchiveDiff | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ConfigSourceArchiveDiff.from_dict(_source)

        source_skipped = d.pop("source_skipped", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: DiffDiffSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = DiffDiffSummary.from_dict(_summary)

        service_app_config_diff_response = cls(
            changed=changed,
            config_id=config_id,
            diff=diff,
            old_config_id=old_config_id,
            source=source,
            source_skipped=source_skipped,
            summary=summary,
        )

        service_app_config_diff_response.additional_properties = d
        return service_app_config_diff_response

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
