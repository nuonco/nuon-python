from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.state_install_state_inputs import StateInstallStateInputs
    from ..models.state_sandbox_state import StateSandboxState


T = TypeVar("T", bound="StateInstallState")


@_attrs_define
class StateInstallState:
    """
    Attributes:
        id (Union[Unset, str]):
        inputs (Union[Unset, StateInstallStateInputs]):
        internal_domain (Union[Unset, str]):
        name (Union[Unset, str]):
        populated (Union[Unset, bool]):
        public_domain (Union[Unset, str]):
        sandbox (Union[Unset, StateSandboxState]):
    """

    id: Union[Unset, str] = UNSET
    inputs: Union[Unset, "StateInstallStateInputs"] = UNSET
    internal_domain: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    populated: Union[Unset, bool] = UNSET
    public_domain: Union[Unset, str] = UNSET
    sandbox: Union[Unset, "StateSandboxState"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        internal_domain = self.internal_domain

        name = self.name

        populated = self.populated

        public_domain = self.public_domain

        sandbox: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox, Unset):
            sandbox = self.sandbox.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if internal_domain is not UNSET:
            field_dict["internal_domain"] = internal_domain
        if name is not UNSET:
            field_dict["name"] = name
        if populated is not UNSET:
            field_dict["populated"] = populated
        if public_domain is not UNSET:
            field_dict["public_domain"] = public_domain
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.state_install_state_inputs import StateInstallStateInputs
        from ..models.state_sandbox_state import StateSandboxState

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: Union[Unset, StateInstallStateInputs]
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = StateInstallStateInputs.from_dict(_inputs)

        internal_domain = d.pop("internal_domain", UNSET)

        name = d.pop("name", UNSET)

        populated = d.pop("populated", UNSET)

        public_domain = d.pop("public_domain", UNSET)

        _sandbox = d.pop("sandbox", UNSET)
        sandbox: Union[Unset, StateSandboxState]
        if isinstance(_sandbox, Unset):
            sandbox = UNSET
        else:
            sandbox = StateSandboxState.from_dict(_sandbox)

        state_install_state = cls(
            id=id,
            inputs=inputs,
            internal_domain=internal_domain,
            name=name,
            populated=populated,
            public_domain=public_domain,
            sandbox=sandbox,
        )

        state_install_state.additional_properties = d
        return state_install_state

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
