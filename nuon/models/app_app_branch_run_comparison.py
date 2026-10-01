from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_branch_run import AppAppBranchRun
    from ..models.blobstore_blob import BlobstoreBlob


T = TypeVar("T", bound="AppAppBranchRunComparison")


@_attrs_define
class AppAppBranchRunComparison:
    """
    Attributes:
        base_run (AppAppBranchRun | Unset):
        base_run_id (str | Unset):
        config_diff (BlobstoreBlob | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        full_diff (BlobstoreBlob | Unset):
        git_diff (BlobstoreBlob | Unset):
        head_run (AppAppBranchRun | Unset):
        head_run_id (str | Unset):
        id (str | Unset):
        org_id (str | Unset):
        source_diff (BlobstoreBlob | Unset):
        updated_at (str | Unset):
    """

    base_run: AppAppBranchRun | Unset = UNSET
    base_run_id: str | Unset = UNSET
    config_diff: BlobstoreBlob | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    full_diff: BlobstoreBlob | Unset = UNSET
    git_diff: BlobstoreBlob | Unset = UNSET
    head_run: AppAppBranchRun | Unset = UNSET
    head_run_id: str | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    source_diff: BlobstoreBlob | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_run, Unset):
            base_run = self.base_run.to_dict()

        base_run_id = self.base_run_id

        config_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_diff, Unset):
            config_diff = self.config_diff.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        full_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_diff, Unset):
            full_diff = self.full_diff.to_dict()

        git_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_diff, Unset):
            git_diff = self.git_diff.to_dict()

        head_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.head_run, Unset):
            head_run = self.head_run.to_dict()

        head_run_id = self.head_run_id

        id = self.id

        org_id = self.org_id

        source_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_diff, Unset):
            source_diff = self.source_diff.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_run is not UNSET:
            field_dict["base_run"] = base_run
        if base_run_id is not UNSET:
            field_dict["base_run_id"] = base_run_id
        if config_diff is not UNSET:
            field_dict["config_diff"] = config_diff
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if full_diff is not UNSET:
            field_dict["full_diff"] = full_diff
        if git_diff is not UNSET:
            field_dict["git_diff"] = git_diff
        if head_run is not UNSET:
            field_dict["head_run"] = head_run
        if head_run_id is not UNSET:
            field_dict["head_run_id"] = head_run_id
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if source_diff is not UNSET:
            field_dict["source_diff"] = source_diff
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_branch_run import AppAppBranchRun  # noqa: PLC0415
        from ..models.blobstore_blob import BlobstoreBlob  # noqa: PLC0415

        d = dict(src_dict)
        _base_run = d.pop("base_run", UNSET)
        base_run: AppAppBranchRun | Unset
        if isinstance(_base_run, Unset):
            base_run = UNSET
        else:
            base_run = AppAppBranchRun.from_dict(_base_run)

        base_run_id = d.pop("base_run_id", UNSET)

        _config_diff = d.pop("config_diff", UNSET)
        config_diff: BlobstoreBlob | Unset
        if isinstance(_config_diff, Unset):
            config_diff = UNSET
        else:
            config_diff = BlobstoreBlob.from_dict(_config_diff)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _full_diff = d.pop("full_diff", UNSET)
        full_diff: BlobstoreBlob | Unset
        if isinstance(_full_diff, Unset):
            full_diff = UNSET
        else:
            full_diff = BlobstoreBlob.from_dict(_full_diff)

        _git_diff = d.pop("git_diff", UNSET)
        git_diff: BlobstoreBlob | Unset
        if isinstance(_git_diff, Unset):
            git_diff = UNSET
        else:
            git_diff = BlobstoreBlob.from_dict(_git_diff)

        _head_run = d.pop("head_run", UNSET)
        head_run: AppAppBranchRun | Unset
        if isinstance(_head_run, Unset):
            head_run = UNSET
        else:
            head_run = AppAppBranchRun.from_dict(_head_run)

        head_run_id = d.pop("head_run_id", UNSET)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        _source_diff = d.pop("source_diff", UNSET)
        source_diff: BlobstoreBlob | Unset
        if isinstance(_source_diff, Unset):
            source_diff = UNSET
        else:
            source_diff = BlobstoreBlob.from_dict(_source_diff)

        updated_at = d.pop("updated_at", UNSET)

        app_app_branch_run_comparison = cls(
            base_run=base_run,
            base_run_id=base_run_id,
            config_diff=config_diff,
            created_at=created_at,
            created_by_id=created_by_id,
            full_diff=full_diff,
            git_diff=git_diff,
            head_run=head_run,
            head_run_id=head_run_id,
            id=id,
            org_id=org_id,
            source_diff=source_diff,
            updated_at=updated_at,
        )

        app_app_branch_run_comparison.additional_properties = d
        return app_app_branch_run_comparison

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
