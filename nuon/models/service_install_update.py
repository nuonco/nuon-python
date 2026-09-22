from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_update_type import ServiceInstallUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_app_config_update import ServiceInstallAppConfigUpdate
    from ..models.service_install_config_update import ServiceInstallConfigUpdate
    from ..models.service_install_inputs_update import ServiceInstallInputsUpdate
    from ..models.service_install_stack_update import ServiceInstallStackUpdate


T = TypeVar("T", bound="ServiceInstallUpdate")


@_attrs_define
class ServiceInstallUpdate:
    """
    Attributes:
        app_config (ServiceInstallAppConfigUpdate | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        id (str | Unset):
        inputs (ServiceInstallInputsUpdate | Unset):
        install_config (ServiceInstallConfigUpdate | Unset):
        stack (ServiceInstallStackUpdate | Unset):
        type_ (ServiceInstallUpdateType | Unset):
        workflow_id (str | Unset):
    """

    app_config: ServiceInstallAppConfigUpdate | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    id: str | Unset = UNSET
    inputs: ServiceInstallInputsUpdate | Unset = UNSET
    install_config: ServiceInstallConfigUpdate | Unset = UNSET
    stack: ServiceInstallStackUpdate | Unset = UNSET
    type_: ServiceInstallUpdateType | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_config, Unset):
            app_config = self.app_config.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        install_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_config, Unset):
            install_config = self.install_config.to_dict()

        stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack, Unset):
            stack = self.stack.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config is not UNSET:
            field_dict["app_config"] = app_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if install_config is not UNSET:
            field_dict["install_config"] = install_config
        if stack is not UNSET:
            field_dict["stack"] = stack
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_app_config_update import ServiceInstallAppConfigUpdate  # noqa: PLC0415
        from ..models.service_install_config_update import ServiceInstallConfigUpdate  # noqa: PLC0415
        from ..models.service_install_inputs_update import ServiceInstallInputsUpdate  # noqa: PLC0415
        from ..models.service_install_stack_update import ServiceInstallStackUpdate  # noqa: PLC0415

        d = dict(src_dict)
        _app_config = d.pop("app_config", UNSET)
        app_config: ServiceInstallAppConfigUpdate | Unset
        if isinstance(_app_config, Unset):
            app_config = UNSET
        else:
            app_config = ServiceInstallAppConfigUpdate.from_dict(_app_config)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: ServiceInstallInputsUpdate | Unset
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ServiceInstallInputsUpdate.from_dict(_inputs)

        _install_config = d.pop("install_config", UNSET)
        install_config: ServiceInstallConfigUpdate | Unset
        if isinstance(_install_config, Unset):
            install_config = UNSET
        else:
            install_config = ServiceInstallConfigUpdate.from_dict(_install_config)

        _stack = d.pop("stack", UNSET)
        stack: ServiceInstallStackUpdate | Unset
        if isinstance(_stack, Unset):
            stack = UNSET
        else:
            stack = ServiceInstallStackUpdate.from_dict(_stack)

        _type_ = d.pop("type", UNSET)
        type_: ServiceInstallUpdateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServiceInstallUpdateType(_type_)

        workflow_id = d.pop("workflow_id", UNSET)

        service_install_update = cls(
            app_config=app_config,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            inputs=inputs,
            install_config=install_config,
            stack=stack,
            type_=type_,
            workflow_id=workflow_id,
        )

        service_install_update.additional_properties = d
        return service_install_update

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
