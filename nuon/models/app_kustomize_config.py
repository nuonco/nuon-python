from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppKustomizeConfig")


@_attrs_define
class AppKustomizeConfig:
    """
    Attributes:
        enable_helm (bool | Unset): Enable Helm chart inflation during kustomize build
        load_restrictor (str | Unset): Load restrictor: "none" or "rootOnly" (default: "rootOnly")
        patches (list[str] | Unset): Additional patch files to apply after kustomize build
        path (str | Unset): Path to kustomization directory (relative to source root)
    """

    enable_helm: bool | Unset = UNSET
    load_restrictor: str | Unset = UNSET
    patches: list[str] | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_helm = self.enable_helm

        load_restrictor = self.load_restrictor

        patches: list[str] | Unset = UNSET
        if not isinstance(self.patches, Unset):
            patches = self.patches

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_helm is not UNSET:
            field_dict["enable_helm"] = enable_helm
        if load_restrictor is not UNSET:
            field_dict["load_restrictor"] = load_restrictor
        if patches is not UNSET:
            field_dict["patches"] = patches
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_helm = d.pop("enable_helm", UNSET)

        load_restrictor = d.pop("load_restrictor", UNSET)

        patches = cast(list[str], d.pop("patches", UNSET))

        path = d.pop("path", UNSET)

        app_kustomize_config = cls(
            enable_helm=enable_helm,
            load_restrictor=load_restrictor,
            patches=patches,
            path=path,
        )

        app_kustomize_config.additional_properties = d
        return app_kustomize_config

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
