from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_app_bundle_runtime import AppAppBundleRuntime
    from ..models.appbundle_runbook_template import AppbundleRunbookTemplate


T = TypeVar("T", bound="ServiceCreateBundleRequest")


@_attrs_define
class ServiceCreateBundleRequest:
    """
    Attributes:
        app_config_id (str):
        runbooks (list[AppbundleRunbookTemplate] | Unset):
        runtime (AppAppBundleRuntime | Unset):
        target_platform (str | Unset):
    """

    app_config_id: str
    runbooks: list[AppbundleRunbookTemplate] | Unset = UNSET
    runtime: AppAppBundleRuntime | Unset = UNSET
    target_platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        runbooks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.runbooks, Unset):
            runbooks = []
            for runbooks_item_data in self.runbooks:
                runbooks_item = runbooks_item_data.to_dict()
                runbooks.append(runbooks_item)

        runtime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.to_dict()

        target_platform = self.target_platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
            }
        )
        if runbooks is not UNSET:
            field_dict["runbooks"] = runbooks
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if target_platform is not UNSET:
            field_dict["target_platform"] = target_platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_app_bundle_runtime import AppAppBundleRuntime  # noqa: PLC0415
        from ..models.appbundle_runbook_template import AppbundleRunbookTemplate  # noqa: PLC0415

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        _runbooks = d.pop("runbooks", UNSET)
        runbooks: list[AppbundleRunbookTemplate] | Unset = UNSET
        if _runbooks is not UNSET:
            runbooks = []
            for runbooks_item_data in _runbooks:
                runbooks_item = AppbundleRunbookTemplate.from_dict(runbooks_item_data)

                runbooks.append(runbooks_item)

        _runtime = d.pop("runtime", UNSET)
        runtime: AppAppBundleRuntime | Unset
        if isinstance(_runtime, Unset):
            runtime = UNSET
        else:
            runtime = AppAppBundleRuntime.from_dict(_runtime)

        target_platform = d.pop("target_platform", UNSET)

        service_create_bundle_request = cls(
            app_config_id=app_config_id,
            runbooks=runbooks,
            runtime=runtime,
            target_platform=target_platform,
        )

        service_create_bundle_request.additional_properties = d
        return service_create_bundle_request

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
