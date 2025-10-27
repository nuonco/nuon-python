from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputsSecretSyncOutput")


@_attrs_define
class OutputsSecretSyncOutput:
    """
    Attributes:
        arn (Union[Unset, str]):
        exists (Union[Unset, bool]):
        kubernetes_key (Union[Unset, str]):
        kubernetes_name (Union[Unset, str]):
        kubernetes_namespace (Union[Unset, str]):
        length (Union[Unset, int]):
        name (Union[Unset, str]):
        timestamp (Union[Unset, str]):
    """

    arn: Union[Unset, str] = UNSET
    exists: Union[Unset, bool] = UNSET
    kubernetes_key: Union[Unset, str] = UNSET
    kubernetes_name: Union[Unset, str] = UNSET
    kubernetes_namespace: Union[Unset, str] = UNSET
    length: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arn = self.arn

        exists = self.exists

        kubernetes_key = self.kubernetes_key

        kubernetes_name = self.kubernetes_name

        kubernetes_namespace = self.kubernetes_namespace

        length = self.length

        name = self.name

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arn is not UNSET:
            field_dict["arn"] = arn
        if exists is not UNSET:
            field_dict["exists"] = exists
        if kubernetes_key is not UNSET:
            field_dict["kubernetes_key"] = kubernetes_key
        if kubernetes_name is not UNSET:
            field_dict["kubernetes_name"] = kubernetes_name
        if kubernetes_namespace is not UNSET:
            field_dict["kubernetes_namespace"] = kubernetes_namespace
        if length is not UNSET:
            field_dict["length"] = length
        if name is not UNSET:
            field_dict["name"] = name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arn = d.pop("arn", UNSET)

        exists = d.pop("exists", UNSET)

        kubernetes_key = d.pop("kubernetes_key", UNSET)

        kubernetes_name = d.pop("kubernetes_name", UNSET)

        kubernetes_namespace = d.pop("kubernetes_namespace", UNSET)

        length = d.pop("length", UNSET)

        name = d.pop("name", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        outputs_secret_sync_output = cls(
            arn=arn,
            exists=exists,
            kubernetes_key=kubernetes_key,
            kubernetes_name=kubernetes_name,
            kubernetes_namespace=kubernetes_namespace,
            length=length,
            name=name,
            timestamp=timestamp,
        )

        outputs_secret_sync_output.additional_properties = d
        return outputs_secret_sync_output

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
