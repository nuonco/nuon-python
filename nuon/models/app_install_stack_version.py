from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_install_stack_version_run import AppInstallStackVersionRun


T = TypeVar("T", bound="AppInstallStackVersion")


@_attrs_define
class AppInstallStackVersion:
    """
    Attributes:
        app_config_id (Union[Unset, str]):
        aws_bucket_key (Union[Unset, str]):
        aws_bucket_name (Union[Unset, str]): aws configuration parameters
        checksum (Union[Unset, str]):
        composite_status (Union[Unset, AppCompositeStatus]):
        contents (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        id (Union[Unset, str]):
        install_id (Union[Unset, str]):
        install_stack_id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        phone_home_id (Union[Unset, str]):
        phone_home_url (Union[Unset, str]):
        quick_link_url (Union[Unset, str]):
        runs (Union[Unset, list['AppInstallStackVersionRun']]):
        template_url (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    app_config_id: Union[Unset, str] = UNSET
    aws_bucket_key: Union[Unset, str] = UNSET
    aws_bucket_name: Union[Unset, str] = UNSET
    checksum: Union[Unset, str] = UNSET
    composite_status: Union[Unset, "AppCompositeStatus"] = UNSET
    contents: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_id: Union[Unset, str] = UNSET
    install_stack_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    phone_home_id: Union[Unset, str] = UNSET
    phone_home_url: Union[Unset, str] = UNSET
    quick_link_url: Union[Unset, str] = UNSET
    runs: Union[Unset, list["AppInstallStackVersionRun"]] = UNSET
    template_url: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_config_id = self.app_config_id

        aws_bucket_key = self.aws_bucket_key

        aws_bucket_name = self.aws_bucket_name

        checksum = self.checksum

        composite_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.composite_status, Unset):
            composite_status = self.composite_status.to_dict()

        contents = self.contents

        created_at = self.created_at

        created_by_id = self.created_by_id

        id = self.id

        install_id = self.install_id

        install_stack_id = self.install_stack_id

        org_id = self.org_id

        phone_home_id = self.phone_home_id

        phone_home_url = self.phone_home_url

        quick_link_url = self.quick_link_url

        runs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()
                runs.append(runs_item)

        template_url = self.template_url

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if aws_bucket_key is not UNSET:
            field_dict["aws_bucket_key"] = aws_bucket_key
        if aws_bucket_name is not UNSET:
            field_dict["aws_bucket_name"] = aws_bucket_name
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if composite_status is not UNSET:
            field_dict["composite_status"] = composite_status
        if contents is not UNSET:
            field_dict["contents"] = contents
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_stack_id is not UNSET:
            field_dict["install_stack_id"] = install_stack_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if phone_home_id is not UNSET:
            field_dict["phone_home_id"] = phone_home_id
        if phone_home_url is not UNSET:
            field_dict["phone_home_url"] = phone_home_url
        if quick_link_url is not UNSET:
            field_dict["quick_link_url"] = quick_link_url
        if runs is not UNSET:
            field_dict["runs"] = runs
        if template_url is not UNSET:
            field_dict["template_url"] = template_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_install_stack_version_run import AppInstallStackVersionRun

        d = dict(src_dict)
        app_config_id = d.pop("app_config_id", UNSET)

        aws_bucket_key = d.pop("aws_bucket_key", UNSET)

        aws_bucket_name = d.pop("aws_bucket_name", UNSET)

        checksum = d.pop("checksum", UNSET)

        _composite_status = d.pop("composite_status", UNSET)
        composite_status: Union[Unset, AppCompositeStatus]
        if isinstance(_composite_status, Unset):
            composite_status = UNSET
        else:
            composite_status = AppCompositeStatus.from_dict(_composite_status)

        contents = d.pop("contents", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_stack_id = d.pop("install_stack_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        phone_home_id = d.pop("phone_home_id", UNSET)

        phone_home_url = d.pop("phone_home_url", UNSET)

        quick_link_url = d.pop("quick_link_url", UNSET)

        runs = []
        _runs = d.pop("runs", UNSET)
        for runs_item_data in _runs or []:
            runs_item = AppInstallStackVersionRun.from_dict(runs_item_data)

            runs.append(runs_item)

        template_url = d.pop("template_url", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_stack_version = cls(
            app_config_id=app_config_id,
            aws_bucket_key=aws_bucket_key,
            aws_bucket_name=aws_bucket_name,
            checksum=checksum,
            composite_status=composite_status,
            contents=contents,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            install_id=install_id,
            install_stack_id=install_stack_id,
            org_id=org_id,
            phone_home_id=phone_home_id,
            phone_home_url=phone_home_url,
            quick_link_url=quick_link_url,
            runs=runs,
            template_url=template_url,
            updated_at=updated_at,
        )

        app_install_stack_version.additional_properties = d
        return app_install_stack_version

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
