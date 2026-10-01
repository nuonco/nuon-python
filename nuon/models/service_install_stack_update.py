from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_stack_version_run_type import AppStackVersionRunType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_stack_version_run_input_diff import AppStackVersionRunInputDiff
    from ..models.app_stack_version_run_role_diff import AppStackVersionRunRoleDiff


T = TypeVar("T", bound="ServiceInstallStackUpdate")


@_attrs_define
class ServiceInstallStackUpdate:
    """
    Attributes:
        input_diff (AppStackVersionRunInputDiff | Unset):
        role_diff (AppStackVersionRunRoleDiff | Unset):
        run_type (AppStackVersionRunType | Unset):
        status (AppCompositeStatus | Unset):
        version_id (str | Unset):
    """

    input_diff: AppStackVersionRunInputDiff | Unset = UNSET
    role_diff: AppStackVersionRunRoleDiff | Unset = UNSET
    run_type: AppStackVersionRunType | Unset = UNSET
    status: AppCompositeStatus | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_diff, Unset):
            input_diff = self.input_diff.to_dict()

        role_diff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_diff, Unset):
            role_diff = self.role_diff.to_dict()

        run_type: str | Unset = UNSET
        if not isinstance(self.run_type, Unset):
            run_type = self.run_type.value

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_diff is not UNSET:
            field_dict["input_diff"] = input_diff
        if role_diff is not UNSET:
            field_dict["role_diff"] = role_diff
        if run_type is not UNSET:
            field_dict["run_type"] = run_type
        if status is not UNSET:
            field_dict["status"] = status
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus  # noqa: PLC0415
        from ..models.app_stack_version_run_input_diff import AppStackVersionRunInputDiff  # noqa: PLC0415
        from ..models.app_stack_version_run_role_diff import AppStackVersionRunRoleDiff  # noqa: PLC0415

        d = dict(src_dict)
        _input_diff = d.pop("input_diff", UNSET)
        input_diff: AppStackVersionRunInputDiff | Unset
        if isinstance(_input_diff, Unset):
            input_diff = UNSET
        else:
            input_diff = AppStackVersionRunInputDiff.from_dict(_input_diff)

        _role_diff = d.pop("role_diff", UNSET)
        role_diff: AppStackVersionRunRoleDiff | Unset
        if isinstance(_role_diff, Unset):
            role_diff = UNSET
        else:
            role_diff = AppStackVersionRunRoleDiff.from_dict(_role_diff)

        _run_type = d.pop("run_type", UNSET)
        run_type: AppStackVersionRunType | Unset
        if isinstance(_run_type, Unset):
            run_type = UNSET
        else:
            run_type = AppStackVersionRunType(_run_type)

        _status = d.pop("status", UNSET)
        status: AppCompositeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AppCompositeStatus.from_dict(_status)

        version_id = d.pop("version_id", UNSET)

        service_install_stack_update = cls(
            input_diff=input_diff,
            role_diff=role_diff,
            run_type=run_type,
            status=status,
            version_id=version_id,
        )

        service_install_stack_update.additional_properties = d
        return service_install_stack_update

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
