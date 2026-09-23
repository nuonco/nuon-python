from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helpers_preview_source_branch import HelpersPreviewSourceBranch
    from ..models.helpers_preview_source_pr import HelpersPreviewSourcePR


T = TypeVar("T", bound="HelpersListPreviewSourcesResult")


@_attrs_define
class HelpersListPreviewSourcesResult:
    """
    Attributes:
        branches (list[HelpersPreviewSourceBranch] | Unset):
        pull_requests (list[HelpersPreviewSourcePR] | Unset):
    """

    branches: list[HelpersPreviewSourceBranch] | Unset = UNSET
    pull_requests: list[HelpersPreviewSourcePR] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        pull_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pull_requests, Unset):
            pull_requests = []
            for pull_requests_item_data in self.pull_requests:
                pull_requests_item = pull_requests_item_data.to_dict()
                pull_requests.append(pull_requests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branches is not UNSET:
            field_dict["branches"] = branches
        if pull_requests is not UNSET:
            field_dict["pull_requests"] = pull_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helpers_preview_source_branch import HelpersPreviewSourceBranch  # noqa: PLC0415
        from ..models.helpers_preview_source_pr import HelpersPreviewSourcePR  # noqa: PLC0415

        d = dict(src_dict)
        _branches = d.pop("branches", UNSET)
        branches: list[HelpersPreviewSourceBranch] | Unset = UNSET
        if _branches is not UNSET:
            branches = []
            for branches_item_data in _branches:
                branches_item = HelpersPreviewSourceBranch.from_dict(branches_item_data)

                branches.append(branches_item)

        _pull_requests = d.pop("pull_requests", UNSET)
        pull_requests: list[HelpersPreviewSourcePR] | Unset = UNSET
        if _pull_requests is not UNSET:
            pull_requests = []
            for pull_requests_item_data in _pull_requests:
                pull_requests_item = HelpersPreviewSourcePR.from_dict(pull_requests_item_data)

                pull_requests.append(pull_requests_item)

        helpers_list_preview_sources_result = cls(
            branches=branches,
            pull_requests=pull_requests,
        )

        helpers_list_preview_sources_result.additional_properties = d
        return helpers_list_preview_sources_result

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
