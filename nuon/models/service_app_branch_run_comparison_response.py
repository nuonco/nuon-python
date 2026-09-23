from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blobstore_blob_metadata import BlobstoreBlobMetadata
    from ..models.service_app_branch_run_comparison_run_summary import ServiceAppBranchRunComparisonRunSummary


T = TypeVar("T", bound="ServiceAppBranchRunComparisonResponse")


@_attrs_define
class ServiceAppBranchRunComparisonResponse:
    """
    Attributes:
        base_run (ServiceAppBranchRunComparisonRunSummary | Unset):
        base_run_id (str | Unset):
        base_sha (str | Unset):
        config_diff (BlobstoreBlobMetadata | Unset):
        config_diff_content (Any | Unset):
        full_diff (BlobstoreBlobMetadata | Unset):
        full_diff_content (Any | Unset):
        git_diff (BlobstoreBlobMetadata | Unset):
        git_diff_content (Any | Unset):
        head_run (ServiceAppBranchRunComparisonRunSummary | Unset):
        head_run_id (str | Unset):
        head_sha (str | Unset):
        id (str | Unset):
    """

    base_run: ServiceAppBranchRunComparisonRunSummary | Unset = UNSET
    base_run_id: str | Unset = UNSET
    base_sha: str | Unset = UNSET
    config_diff: BlobstoreBlobMetadata | Unset = UNSET
    config_diff_content: Any | Unset = UNSET
    full_diff: BlobstoreBlobMetadata | Unset = UNSET
    full_diff_content: Any | Unset = UNSET
    git_diff: BlobstoreBlobMetadata | Unset = UNSET
    git_diff_content: Any | Unset = UNSET
    head_run: ServiceAppBranchRunComparisonRunSummary | Unset = UNSET
    head_run_id: str | Unset = UNSET
    head_sha: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_run, Unset):
            base_run = self.base_run.to_dict()

        base_run_id = self.base_run_id

        base_sha = self.base_sha

        config_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_diff, Unset):
            config_diff = self.config_diff.to_dict()

        config_diff_content = self.config_diff_content

        full_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_diff, Unset):
            full_diff = self.full_diff.to_dict()

        full_diff_content = self.full_diff_content

        git_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_diff, Unset):
            git_diff = self.git_diff.to_dict()

        git_diff_content = self.git_diff_content

        head_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.head_run, Unset):
            head_run = self.head_run.to_dict()

        head_run_id = self.head_run_id

        head_sha = self.head_sha

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_run is not UNSET:
            field_dict["base_run"] = base_run
        if base_run_id is not UNSET:
            field_dict["base_run_id"] = base_run_id
        if base_sha is not UNSET:
            field_dict["base_sha"] = base_sha
        if config_diff is not UNSET:
            field_dict["config_diff"] = config_diff
        if config_diff_content is not UNSET:
            field_dict["config_diff_content"] = config_diff_content
        if full_diff is not UNSET:
            field_dict["full_diff"] = full_diff
        if full_diff_content is not UNSET:
            field_dict["full_diff_content"] = full_diff_content
        if git_diff is not UNSET:
            field_dict["git_diff"] = git_diff
        if git_diff_content is not UNSET:
            field_dict["git_diff_content"] = git_diff_content
        if head_run is not UNSET:
            field_dict["head_run"] = head_run
        if head_run_id is not UNSET:
            field_dict["head_run_id"] = head_run_id
        if head_sha is not UNSET:
            field_dict["head_sha"] = head_sha
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blobstore_blob_metadata import BlobstoreBlobMetadata  # noqa: PLC0415
        from ..models.service_app_branch_run_comparison_run_summary import (
            ServiceAppBranchRunComparisonRunSummary,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _base_run = d.pop("base_run", UNSET)
        base_run: ServiceAppBranchRunComparisonRunSummary | Unset
        if isinstance(_base_run, Unset):
            base_run = UNSET
        else:
            base_run = ServiceAppBranchRunComparisonRunSummary.from_dict(_base_run)

        base_run_id = d.pop("base_run_id", UNSET)

        base_sha = d.pop("base_sha", UNSET)

        _config_diff = d.pop("config_diff", UNSET)
        config_diff: BlobstoreBlobMetadata | Unset
        if isinstance(_config_diff, Unset):
            config_diff = UNSET
        else:
            config_diff = BlobstoreBlobMetadata.from_dict(_config_diff)

        config_diff_content = d.pop("config_diff_content", UNSET)

        _full_diff = d.pop("full_diff", UNSET)
        full_diff: BlobstoreBlobMetadata | Unset
        if isinstance(_full_diff, Unset):
            full_diff = UNSET
        else:
            full_diff = BlobstoreBlobMetadata.from_dict(_full_diff)

        full_diff_content = d.pop("full_diff_content", UNSET)

        _git_diff = d.pop("git_diff", UNSET)
        git_diff: BlobstoreBlobMetadata | Unset
        if isinstance(_git_diff, Unset):
            git_diff = UNSET
        else:
            git_diff = BlobstoreBlobMetadata.from_dict(_git_diff)

        git_diff_content = d.pop("git_diff_content", UNSET)

        _head_run = d.pop("head_run", UNSET)
        head_run: ServiceAppBranchRunComparisonRunSummary | Unset
        if isinstance(_head_run, Unset):
            head_run = UNSET
        else:
            head_run = ServiceAppBranchRunComparisonRunSummary.from_dict(_head_run)

        head_run_id = d.pop("head_run_id", UNSET)

        head_sha = d.pop("head_sha", UNSET)

        id = d.pop("id", UNSET)

        service_app_branch_run_comparison_response = cls(
            base_run=base_run,
            base_run_id=base_run_id,
            base_sha=base_sha,
            config_diff=config_diff,
            config_diff_content=config_diff_content,
            full_diff=full_diff,
            full_diff_content=full_diff_content,
            git_diff=git_diff,
            git_diff_content=git_diff_content,
            head_run=head_run,
            head_run_id=head_run_id,
            head_sha=head_sha,
            id=id,
        )

        service_app_branch_run_comparison_response.additional_properties = d
        return service_app_branch_run_comparison_response

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
