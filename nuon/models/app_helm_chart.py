from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_helm_release import AppHelmRelease


T = TypeVar("T", bound="AppHelmChart")


@_attrs_define
class AppHelmChart:
    """
    Attributes:
        created_at (str | Unset):
        created_by_id (str | Unset):
        helm_releases (list[AppHelmRelease] | Unset):
        id (str | Unset):
        org_id (str | Unset):
        owner_id (str | Unset):
        owner_type (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    helm_releases: list[AppHelmRelease] | Unset = UNSET
    id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_id = self.created_by_id

        helm_releases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.helm_releases, Unset):
            helm_releases = []
            for helm_releases_item_data in self.helm_releases:
                helm_releases_item = helm_releases_item_data.to_dict()
                helm_releases.append(helm_releases_item)

        id = self.id

        org_id = self.org_id

        owner_id = self.owner_id

        owner_type = self.owner_type

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if helm_releases is not UNSET:
            field_dict["helmReleases"] = helm_releases
        if id is not UNSET:
            field_dict["id"] = id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_helm_release import AppHelmRelease

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _helm_releases = d.pop("helmReleases", UNSET)
        helm_releases: list[AppHelmRelease] | Unset = UNSET
        if _helm_releases is not UNSET:
            helm_releases = []
            for helm_releases_item_data in _helm_releases:
                helm_releases_item = AppHelmRelease.from_dict(helm_releases_item_data)

                helm_releases.append(helm_releases_item)

        id = d.pop("id", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        owner_type = d.pop("owner_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_helm_chart = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            helm_releases=helm_releases,
            id=id,
            org_id=org_id,
            owner_id=owner_id,
            owner_type=owner_type,
            updated_at=updated_at,
        )

        app_helm_chart.additional_properties = d
        return app_helm_chart

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
