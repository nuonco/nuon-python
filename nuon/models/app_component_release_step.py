from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_install_deploy import AppInstallDeploy


T = TypeVar("T", bound="AppComponentReleaseStep")


@_attrs_define
class AppComponentReleaseStep:
    """
    Attributes:
        component_release_id (Union[Unset, str]): parent release ID
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        delay (Union[Unset, str]): fields to control the delay of the individual step, as this is set based on the
            parent strategy
        id (Union[Unset, str]):
        install_deploys (Union[Unset, list['AppInstallDeploy']]):
        requested_install_ids (Union[Unset, list[str]]): When a step is created, a set of installs are targeted.
            However, by the time the release step goes out, the
            install might have been setup in any order of ways.
        status (Union[Unset, str]):
        status_description (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    component_release_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    delay: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_deploys: Union[Unset, list["AppInstallDeploy"]] = UNSET
    requested_install_ids: Union[Unset, list[str]] = UNSET
    status: Union[Unset, str] = UNSET
    status_description: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_release_id = self.component_release_id

        created_at = self.created_at

        created_by_id = self.created_by_id

        delay = self.delay

        id = self.id

        install_deploys: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.install_deploys, Unset):
            install_deploys = []
            for install_deploys_item_data in self.install_deploys:
                install_deploys_item = install_deploys_item_data.to_dict()
                install_deploys.append(install_deploys_item)

        requested_install_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.requested_install_ids, Unset):
            requested_install_ids = self.requested_install_ids

        status = self.status

        status_description = self.status_description

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_release_id is not UNSET:
            field_dict["component_release_id"] = component_release_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if delay is not UNSET:
            field_dict["delay"] = delay
        if id is not UNSET:
            field_dict["id"] = id
        if install_deploys is not UNSET:
            field_dict["install_deploys"] = install_deploys
        if requested_install_ids is not UNSET:
            field_dict["requested_install_ids"] = requested_install_ids
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_install_deploy import AppInstallDeploy

        d = dict(src_dict)
        component_release_id = d.pop("component_release_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        delay = d.pop("delay", UNSET)

        id = d.pop("id", UNSET)

        install_deploys = []
        _install_deploys = d.pop("install_deploys", UNSET)
        for install_deploys_item_data in _install_deploys or []:
            install_deploys_item = AppInstallDeploy.from_dict(install_deploys_item_data)

            install_deploys.append(install_deploys_item)

        requested_install_ids = cast(list[str], d.pop("requested_install_ids", UNSET))

        status = d.pop("status", UNSET)

        status_description = d.pop("status_description", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_component_release_step = cls(
            component_release_id=component_release_id,
            created_at=created_at,
            created_by_id=created_by_id,
            delay=delay,
            id=id,
            install_deploys=install_deploys,
            requested_install_ids=requested_install_ids,
            status=status,
            status_description=status_description,
            updated_at=updated_at,
        )

        app_component_release_step.additional_properties = d
        return app_component_release_step

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
