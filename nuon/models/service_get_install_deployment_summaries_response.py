from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_deployment_summary import ServiceInstallDeploymentSummary


T = TypeVar("T", bound="ServiceGetInstallDeploymentSummariesResponse")


@_attrs_define
class ServiceGetInstallDeploymentSummariesResponse:
    """
    Attributes:
        deployments (list[ServiceInstallDeploymentSummary] | Unset):
        has_more (bool | Unset):
        limit (int | Unset):
        next_cursor (str | Unset):
        offset (int | Unset):
        page (int | Unset):
        total (int | None | Unset):
    """

    deployments: list[ServiceInstallDeploymentSummary] | Unset = UNSET
    has_more: bool | Unset = UNSET
    limit: int | Unset = UNSET
    next_cursor: str | Unset = UNSET
    offset: int | Unset = UNSET
    page: int | Unset = UNSET
    total: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = []
            for deployments_item_data in self.deployments:
                deployments_item = deployments_item_data.to_dict()
                deployments.append(deployments_item)

        has_more = self.has_more

        limit = self.limit

        next_cursor = self.next_cursor

        offset = self.offset

        page = self.page

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployments is not UNSET:
            field_dict["deployments"] = deployments
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if limit is not UNSET:
            field_dict["limit"] = limit
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if offset is not UNSET:
            field_dict["offset"] = offset
        if page is not UNSET:
            field_dict["page"] = page
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_deployment_summary import ServiceInstallDeploymentSummary  # noqa: PLC0415

        d = dict(src_dict)
        _deployments = d.pop("deployments", UNSET)
        deployments: list[ServiceInstallDeploymentSummary] | Unset = UNSET
        if _deployments is not UNSET:
            deployments = []
            for deployments_item_data in _deployments:
                deployments_item = ServiceInstallDeploymentSummary.from_dict(deployments_item_data)

                deployments.append(deployments_item)

        has_more = d.pop("has_more", UNSET)

        limit = d.pop("limit", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        offset = d.pop("offset", UNSET)

        page = d.pop("page", UNSET)

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        service_get_install_deployment_summaries_response = cls(
            deployments=deployments,
            has_more=has_more,
            limit=limit,
            next_cursor=next_cursor,
            offset=offset,
            page=page,
            total=total,
        )

        service_get_install_deployment_summaries_response.additional_properties = d
        return service_get_install_deployment_summaries_response

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
