from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_install_stack_state_outputs import StateInstallStackStateOutputs


T = TypeVar("T", bound="StateInstallStackState")


@_attrs_define
class StateInstallStackState:
    """
    Attributes:
        checksum (str | Unset):
        outputs (StateInstallStackStateOutputs | Unset):
        populated (bool | Unset):
        quick_link_url (str | Unset):
        status (str | Unset):
        template_json (str | Unset):
        template_url (str | Unset):
    """

    checksum: str | Unset = UNSET
    outputs: StateInstallStackStateOutputs | Unset = UNSET
    populated: bool | Unset = UNSET
    quick_link_url: str | Unset = UNSET
    status: str | Unset = UNSET
    template_json: str | Unset = UNSET
    template_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum = self.checksum

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        populated = self.populated

        quick_link_url = self.quick_link_url

        status = self.status

        template_json = self.template_json

        template_url = self.template_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if populated is not UNSET:
            field_dict["populated"] = populated
        if quick_link_url is not UNSET:
            field_dict["quick_link_url"] = quick_link_url
        if status is not UNSET:
            field_dict["status"] = status
        if template_json is not UNSET:
            field_dict["template_json"] = template_json
        if template_url is not UNSET:
            field_dict["template_url"] = template_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_install_stack_state_outputs import StateInstallStackStateOutputs

        d = dict(src_dict)
        checksum = d.pop("checksum", UNSET)

        _outputs = d.pop("outputs", UNSET)
        outputs: StateInstallStackStateOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = StateInstallStackStateOutputs.from_dict(_outputs)

        populated = d.pop("populated", UNSET)

        quick_link_url = d.pop("quick_link_url", UNSET)

        status = d.pop("status", UNSET)

        template_json = d.pop("template_json", UNSET)

        template_url = d.pop("template_url", UNSET)

        state_install_stack_state = cls(
            checksum=checksum,
            outputs=outputs,
            populated=populated,
            quick_link_url=quick_link_url,
            status=status,
            template_json=template_json,
            template_url=template_url,
        )

        state_install_stack_state.additional_properties = d
        return state_install_stack_state

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
