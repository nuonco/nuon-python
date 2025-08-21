from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_aws_stack_outputs import AppAWSStackOutputs
    from ..models.app_azure_stack_outputs import AppAzureStackOutputs
    from ..models.app_install_stack_outputs_data import AppInstallStackOutputsData


T = TypeVar("T", bound="AppInstallStackOutputs")


@_attrs_define
class AppInstallStackOutputs:
    """
    Attributes:
        aws (Union[Unset, AppAWSStackOutputs]):
        azure (Union[Unset, AppAzureStackOutputs]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        data (Union[Unset, AppInstallStackOutputsData]):
        id (Union[Unset, str]):
        install_stack_id (Union[Unset, str]):
        install_version_run_id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    aws: Union[Unset, "AppAWSStackOutputs"] = UNSET
    azure: Union[Unset, "AppAzureStackOutputs"] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    data: Union[Unset, "AppInstallStackOutputsData"] = UNSET
    id: Union[Unset, str] = UNSET
    install_stack_id: Union[Unset, str] = UNSET
    install_version_run_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        azure: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        created_at = self.created_at

        created_by_id = self.created_by_id

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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

        d = dict(src_dict)
        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, AppAWSStackOutputs]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = AppAWSStackOutputs.from_dict(_aws)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, AppAzureStackOutputs]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = AppAzureStackOutputs.from_dict(_azure)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, AppInstallStackOutputsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AppInstallStackOutputsData.from_dict(_data)

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
