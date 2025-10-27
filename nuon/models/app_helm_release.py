from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_helm_chart import AppHelmChart
    from ..models.app_json_map import AppJSONMap


T = TypeVar("T", bound="AppHelmRelease")


@_attrs_define
class AppHelmRelease:
    """
    Attributes:
        body (Union[Unset, str]): The rspb.Release body, as a base64-encoded string
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        helm_chart (Union[Unset, AppHelmChart]):
        helm_chart_id (Union[Unset, str]):
        key (Union[Unset, str]):
        labels (Union[Unset, AppJSONMap]):
        name (Union[Unset, str]): Release "labels" that can be used as filters in the storage.Query(labels
            map[string]string)
            we implemented. Note that allowing Helm users to filter against new dimensions will require a
            new migration to be added, and the Create and/or update functions to be updated accordingly.
        namespace (Union[Unset, str]):
        org_id (Union[Unset, str]):
        owner (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]): See
            https://github.com/helm/helm/blob/c9fe3d118caec699eb2565df9838673af379ce12/pkg/storage/driver/secrets.go#L231
        updated_at (Union[Unset, str]):
        version (Union[Unset, int]):
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    helm_chart: Union[Unset, "AppHelmChart"] = UNSET
    helm_chart_id: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    labels: Union[Unset, "AppJSONMap"] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        created_at = self.created_at

        created_by_id = self.created_by_id

        helm_chart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.helm_chart, Unset):
            helm_chart = self.helm_chart.to_dict()

        helm_chart_id = self.helm_chart_id

        key = self.key

        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name = self.name

        namespace = self.namespace

        org_id = self.org_id

        owner = self.owner

        status = self.status

        type_ = self.type_

        updated_at = self.updated_at

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if helm_chart is not UNSET:
            field_dict["helmChart"] = helm_chart
        if helm_chart_id is not UNSET:
            field_dict["helmChartID"] = helm_chart_id
        if key is not UNSET:
            field_dict["key"] = key
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_helm_chart import AppHelmChart
        from ..models.app_json_map import AppJSONMap

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _helm_chart = d.pop("helmChart", UNSET)
        helm_chart: Union[Unset, AppHelmChart]
        if isinstance(_helm_chart, Unset):
            helm_chart = UNSET
        else:
            helm_chart = AppHelmChart.from_dict(_helm_chart)

        helm_chart_id = d.pop("helmChartID", UNSET)

        key = d.pop("key", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, AppJSONMap]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = AppJSONMap.from_dict(_labels)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        org_id = d.pop("org_id", UNSET)

        owner = d.pop("owner", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        app_helm_release = cls(
            body=body,
            created_at=created_at,
            created_by_id=created_by_id,
            helm_chart=helm_chart,
            helm_chart_id=helm_chart_id,
            key=key,
            labels=labels,
            name=name,
            namespace=namespace,
            org_id=org_id,
            owner=owner,
            status=status,
            type_=type_,
            updated_at=updated_at,
            version=version,
        )

        app_helm_release.additional_properties = d
        return app_helm_release

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
