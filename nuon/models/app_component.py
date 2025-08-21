from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_component_type import AppComponentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_component_links import AppComponentLinks


T = TypeVar("T", bound="AppComponent")


@_attrs_define
class AppComponent:
    """
    Attributes:
        app_id (Union[Unset, str]):
        config_versions (Union[Unset, int]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        dependencies (Union[Unset, list[str]]):
        id (Union[Unset, str]):
        links (Union[Unset, AppComponentLinks]):
        name (Union[Unset, str]):
        resolved_var_name (Union[Unset, str]):
        status (Union[Unset, str]):
        status_description (Union[Unset, str]):
        type_ (Union[Unset, AppComponentType]):
        updated_at (Union[Unset, str]):
        var_name (Union[Unset, str]):
    """

    app_id: Union[Unset, str] = UNSET
    config_versions: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    dependencies: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "AppComponentLinks"] = UNSET
    name: Union[Unset, str] = UNSET
    resolved_var_name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    type_: Union[Unset, AppComponentType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    var_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        config_versions = self.config_versions

        created_at = self.created_at

        created_by_id = self.created_by_id

        dependencies: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        id = self.id

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        resolved_var_name = self.resolved_var_name

        status = self.status

        status_description = self.status_description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        var_name = self.var_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if config_versions is not UNSET:
            field_dict["config_versions"] = config_versions
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if resolved_var_name is not UNSET:
            field_dict["resolved_var_name"] = resolved_var_name
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if var_name is not UNSET:
            field_dict["var_name"] = var_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_component_links import AppComponentLinks

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        config_versions = d.pop("config_versions", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, AppComponentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppComponentLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        resolved_var_name = d.pop("resolved_var_name", UNSET)

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AppComponentType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AppComponentType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        var_name = d.pop("var_name", UNSET)

        app_component = cls(
            app_id=app_id,
            config_versions=config_versions,
            created_at=created_at,
            created_by_id=created_by_id,
            dependencies=dependencies,
            id=id,
            links=links,
            name=name,
            resolved_var_name=resolved_var_name,
            status=status,
            status_description=status_description,
            type_=type_,
            updated_at=updated_at,
            var_name=var_name,
        )

        app_component.additional_properties = d
        return app_component

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
