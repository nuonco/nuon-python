from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kube_cluster_info import KubeClusterInfo
    from ..models.plantypes_helm_value import PlantypesHelmValue


T = TypeVar("T", bound="PlantypesHelmDeployPlan")


@_attrs_define
class PlantypesHelmDeployPlan:
    """
    Attributes:
        cluster_info (KubeClusterInfo | Unset):
        create_namespace (bool | Unset):
        helm_chart_id (str | Unset):
        name (str | Unset): NOTE(jm): these fields should probably just come from the app config, however we keep them
            around for
            debuggability
        namespace (str | Unset):
        storage_driver (str | Unset):
        take_ownership (bool | Unset):
        values (list[PlantypesHelmValue] | Unset):
        values_files (list[str] | Unset):
    """

    cluster_info: KubeClusterInfo | Unset = UNSET
    create_namespace: bool | Unset = UNSET
    helm_chart_id: str | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    storage_driver: str | Unset = UNSET
    take_ownership: bool | Unset = UNSET
    values: list[PlantypesHelmValue] | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        create_namespace = self.create_namespace

        helm_chart_id = self.helm_chart_id

        name = self.name

        namespace = self.namespace

        storage_driver = self.storage_driver

        take_ownership = self.take_ownership

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if create_namespace is not UNSET:
            field_dict["create_namespace"] = create_namespace
        if helm_chart_id is not UNSET:
            field_dict["helm_chart_id"] = helm_chart_id
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if storage_driver is not UNSET:
            field_dict["storage_driver"] = storage_driver
        if take_ownership is not UNSET:
            field_dict["take_ownership"] = take_ownership
        if values is not UNSET:
            field_dict["values"] = values
        if values_files is not UNSET:
            field_dict["values_files"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kube_cluster_info import KubeClusterInfo
        from ..models.plantypes_helm_value import PlantypesHelmValue

        d = dict(src_dict)
        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: KubeClusterInfo | Unset
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        create_namespace = d.pop("create_namespace", UNSET)

        helm_chart_id = d.pop("helm_chart_id", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        storage_driver = d.pop("storage_driver", UNSET)

        take_ownership = d.pop("take_ownership", UNSET)

        _values = d.pop("values", UNSET)
        values: list[PlantypesHelmValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = PlantypesHelmValue.from_dict(values_item_data)

                values.append(values_item)

        values_files = cast(list[str], d.pop("values_files", UNSET))

        plantypes_helm_deploy_plan = cls(
            cluster_info=cluster_info,
            create_namespace=create_namespace,
            helm_chart_id=helm_chart_id,
            name=name,
            namespace=namespace,
            storage_driver=storage_driver,
            take_ownership=take_ownership,
            values=values,
            values_files=values_files,
        )

        plantypes_helm_deploy_plan.additional_properties = d
        return plantypes_helm_deploy_plan

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
