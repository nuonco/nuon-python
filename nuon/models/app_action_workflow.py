from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_action_workflow_config import AppActionWorkflowConfig


T = TypeVar("T", bound="AppActionWorkflow")


@_attrs_define
class AppActionWorkflow:
    """
    Attributes:
        app_id (Union[Unset, str]):
        config_count (Union[Unset, int]):
        configs (Union[Unset, list['AppActionWorkflowConfig']]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]): metadata
        status (Union[Unset, str]): TODO: change to default null after migration & after initial pr
        status_description (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    app_id: Union[Unset, str] = UNSET
    config_count: Union[Unset, int] = UNSET
    configs: Union[Unset, list["AppActionWorkflowConfig"]] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        config_count = self.config_count

        configs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.configs, Unset):
            configs = []
            for configs_item_data in self.configs:
                configs_item = configs_item_data.to_dict()
                configs.append(configs_item)

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        name = self.name

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if config_count is not UNSET:
            field_dict["config_count"] = config_count
        if configs is not UNSET:
            field_dict["configs"] = configs
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_action_workflow_config import AppActionWorkflowConfig

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        config_count = d.pop("config_count", UNSET)

        configs = []
        _configs = d.pop("configs", UNSET)
        for configs_item_data in _configs or []:
            configs_item = AppActionWorkflowConfig.from_dict(configs_item_data)

            configs.append(configs_item)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_action_workflow = cls(
            app_id=app_id,
            config_count=config_count,
            configs=configs,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            name=name,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
        )

        app_action_workflow.additional_properties = d
        return app_action_workflow

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
