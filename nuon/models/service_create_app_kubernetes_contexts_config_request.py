from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_app_kubernetes_context import ServiceAppKubernetesContext


T = TypeVar("T", bound="ServiceCreateAppKubernetesContextsConfigRequest")


@_attrs_define
class ServiceCreateAppKubernetesContextsConfigRequest:
    """
    Attributes:
        app_config_id (str):
        contexts (list[ServiceAppKubernetesContext] | Unset):
    """

    app_config_id: str
    contexts: list[ServiceAppKubernetesContext] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        contexts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = []
            for contexts_item_data in self.contexts:
                contexts_item = contexts_item_data.to_dict()
                contexts.append(contexts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_config_id": app_config_id,
            }
        )
        if contexts is not UNSET:
            field_dict["contexts"] = contexts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_app_kubernetes_context import ServiceAppKubernetesContext

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id")

        _contexts = d.pop("contexts", UNSET)
        contexts: list[ServiceAppKubernetesContext] | Unset = UNSET
        if _contexts is not UNSET:
            contexts = []
            for contexts_item_data in _contexts:
                contexts_item = ServiceAppKubernetesContext.from_dict(contexts_item_data)

                contexts.append(contexts_item)

        service_create_app_kubernetes_contexts_config_request = cls(
            app_config_id=app_config_id,
            contexts=contexts,
        )

        service_create_app_kubernetes_contexts_config_request.additional_properties = d
        return service_create_app_kubernetes_contexts_config_request

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
