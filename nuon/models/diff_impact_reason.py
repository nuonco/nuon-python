from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diff_edge_reason import DiffEdgeReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffImpactReason")


@_attrs_define
class DiffImpactReason:
    """
    Attributes:
        edge (DiffEdgeReason | Unset):
        from_ (str | Unset):
    """

    edge: DiffEdgeReason | Unset = UNSET
    from_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edge: str | Unset = UNSET
        if not isinstance(self.edge, Unset):
            edge = self.edge.value

        from_ = self.from_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge is not UNSET:
            field_dict["edge"] = edge
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _edge = d.pop("edge", UNSET)
        edge: DiffEdgeReason | Unset
        if isinstance(_edge, Unset):
            edge = UNSET
        else:
            edge = DiffEdgeReason(_edge)

        from_ = d.pop("from", UNSET)

        diff_impact_reason = cls(
            edge=edge,
            from_=from_,
        )

        diff_impact_reason.additional_properties = d
        return diff_impact_reason

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
