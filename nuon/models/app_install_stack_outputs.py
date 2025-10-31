from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_aws_stack_outputs import AppAWSStackOutputs
    from ..models.app_azure_stack_outputs import AppAzureStackOutputs
    from ..models.app_install_stack_outputs_data import AppInstallStackOutputsData
    from ..models.app_install_stack_outputs_data_contents import AppInstallStackOutputsDataContents


T = TypeVar("T", bound="AppInstallStackOutputs")


@_attrs_define
class AppInstallStackOutputs:
    """
    Attributes:
        aws (AppAWSStackOutputs | Unset):
        azure (AppAzureStackOutputs | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        data (AppInstallStackOutputsData | Unset):
        data_contents (AppInstallStackOutputsDataContents | Unset):
        id (str | Unset):
        install_stack_id (str | Unset):
        install_version_run_id (str | Unset):
        org_id (str | Unset):
        updated_at (str | Unset):
    """

    aws: AppAWSStackOutputs | Unset = UNSET
    azure: AppAzureStackOutputs | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    data: AppInstallStackOutputsData | Unset = UNSET
    data_contents: AppInstallStackOutputsDataContents | Unset = UNSET
    id: str | Unset = UNSET
    install_stack_id: str | Unset = UNSET
    install_version_run_id: str | Unset = UNSET
    org_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        azure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        data_contents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_contents, Unset):
            data_contents = self.data_contents.to_dict()

        id = self.id

        install_stack_id = self.install_stack_id

        install_version_run_id = self.install_version_run_id

        org_id = self.org_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws is not UNSET:
            field_dict["aws"] = aws
        if azure is not UNSET:
            field_dict["azure"] = azure
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if data is not UNSET:
            field_dict["data"] = data
        if data_contents is not UNSET:
            field_dict["data_contents"] = data_contents
        if id is not UNSET:
            field_dict["id"] = id
        if install_stack_id is not UNSET:
            field_dict["install_stack_id"] = install_stack_id
        if install_version_run_id is not UNSET:
            field_dict["install_version_run_id"] = install_version_run_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_aws_stack_outputs import AppAWSStackOutputs
        from ..models.app_azure_stack_outputs import AppAzureStackOutputs
        from ..models.app_install_stack_outputs_data import AppInstallStackOutputsData
        from ..models.app_install_stack_outputs_data_contents import AppInstallStackOutputsDataContents

        d = dict(src_dict)
        _aws = d.pop("aws", UNSET)
        aws: AppAWSStackOutputs | Unset
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = AppAWSStackOutputs.from_dict(_aws)

        _azure = d.pop("azure", UNSET)
        azure: AppAzureStackOutputs | Unset
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = AppAzureStackOutputs.from_dict(_azure)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _data = d.pop("data", UNSET)
        data: AppInstallStackOutputsData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AppInstallStackOutputsData.from_dict(_data)

        _data_contents = d.pop("data_contents", UNSET)
        data_contents: AppInstallStackOutputsDataContents | Unset
        if isinstance(_data_contents, Unset):
            data_contents = UNSET
        else:
            data_contents = AppInstallStackOutputsDataContents.from_dict(_data_contents)

        id = d.pop("id", UNSET)

        install_stack_id = d.pop("install_stack_id", UNSET)

        install_version_run_id = d.pop("install_version_run_id", UNSET)

        org_id = d.pop("org_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_install_stack_outputs = cls(
            aws=aws,
            azure=azure,
            created_at=created_at,
            created_by_id=created_by_id,
            data=data,
            data_contents=data_contents,
            id=id,
            install_stack_id=install_stack_id,
            install_version_run_id=install_version_run_id,
            org_id=org_id,
            updated_at=updated_at,
        )

        app_install_stack_outputs.additional_properties = d
        return app_install_stack_outputs

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
