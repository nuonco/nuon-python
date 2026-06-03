from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plantypes_kubernetes_secret_sync_target import PlantypesKubernetesSecretSyncTarget


T = TypeVar("T", bound="PlantypesKubernetesSecretSync")


@_attrs_define
class PlantypesKubernetesSecretSync:
    """
    Attributes:
        azure_key_vault_secret_id (str | Unset): https://{vault-name}.vault.azure.net/secrets/{secret-name}
        format_ (str | Unset): NOTE(jm): this should probably come from the app config, but for now we just use string
            parsing to avoid
            updating the runner job and save time.
        gcp_secret_name (str | Unset): projects/{project}/secrets/{id}/versions/latest
        key_name (str | Unset):
        name (str | Unset):
        namespace (str | Unset): v1 destination (single). Used when Targets is empty.
        secret_arn (str | Unset):
        secret_name (str | Unset): the name of the secret from the config
        targets (list[PlantypesKubernetesSecretSyncTarget] | Unset): v2 destinations: when len(Targets) > 0 the runner
            uses the v2 path and fans the shared source out across each
            target's namespaces. The v1 fields above are ignored in that case.
    """

    azure_key_vault_secret_id: str | Unset = UNSET
    format_: str | Unset = UNSET
    gcp_secret_name: str | Unset = UNSET
    key_name: str | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    secret_arn: str | Unset = UNSET
    secret_name: str | Unset = UNSET
    targets: list[PlantypesKubernetesSecretSyncTarget] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        azure_key_vault_secret_id = self.azure_key_vault_secret_id

        format_ = self.format_

        gcp_secret_name = self.gcp_secret_name

        key_name = self.key_name

        name = self.name

        namespace = self.namespace

        secret_arn = self.secret_arn

        secret_name = self.secret_name

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if azure_key_vault_secret_id is not UNSET:
            field_dict["azure_key_vault_secret_id"] = azure_key_vault_secret_id
        if format_ is not UNSET:
            field_dict["format"] = format_
        if gcp_secret_name is not UNSET:
            field_dict["gcp_secret_name"] = gcp_secret_name
        if key_name is not UNSET:
            field_dict["key_name"] = key_name
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if secret_arn is not UNSET:
            field_dict["secret_arn"] = secret_arn
        if secret_name is not UNSET:
            field_dict["secret_name"] = secret_name
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plantypes_kubernetes_secret_sync_target import PlantypesKubernetesSecretSyncTarget

        d = dict(src_dict)
        azure_key_vault_secret_id = d.pop("azure_key_vault_secret_id", UNSET)

        format_ = d.pop("format", UNSET)

        gcp_secret_name = d.pop("gcp_secret_name", UNSET)

        key_name = d.pop("key_name", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        secret_arn = d.pop("secret_arn", UNSET)

        secret_name = d.pop("secret_name", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[PlantypesKubernetesSecretSyncTarget] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = PlantypesKubernetesSecretSyncTarget.from_dict(targets_item_data)

                targets.append(targets_item)

        plantypes_kubernetes_secret_sync = cls(
            azure_key_vault_secret_id=azure_key_vault_secret_id,
            format_=format_,
            gcp_secret_name=gcp_secret_name,
            key_name=key_name,
            name=name,
            namespace=namespace,
            secret_arn=secret_arn,
            secret_name=secret_name,
            targets=targets,
        )

        plantypes_kubernetes_secret_sync.additional_properties = d
        return plantypes_kubernetes_secret_sync

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
