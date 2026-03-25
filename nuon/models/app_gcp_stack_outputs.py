from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_gcp_stack_outputs_break_glass_sa_emails import AppGCPStackOutputsBreakGlassSaEmails
    from ..models.app_gcp_stack_outputs_custom_sa_emails import AppGCPStackOutputsCustomSaEmails
    from ..models.app_gcp_stack_outputs_install_inputs import AppGCPStackOutputsInstallInputs


T = TypeVar("T", bound="AppGCPStackOutputs")


@_attrs_define
class AppGCPStackOutputs:
    """
    Attributes:
        break_glass_sa_emails (AppGCPStackOutputsBreakGlassSaEmails | Unset):
        custom_sa_emails (AppGCPStackOutputsCustomSaEmails | Unset):
        deprovision_sa_email (str | Unset):
        install_inputs (AppGCPStackOutputsInstallInputs | Unset):
        maintenance_sa_email (str | Unset):
        network_id (str | Unset):
        network_name (str | Unset):
        private_subnet_name (str | Unset):
        project_id (str | Unset):
        provision_sa_email (str | Unset):
        public_subnet_name (str | Unset):
        region (str | Unset):
        runner_service_account_email (str | Unset):
        runner_subnet_name (str | Unset):
    """

    break_glass_sa_emails: AppGCPStackOutputsBreakGlassSaEmails | Unset = UNSET
    custom_sa_emails: AppGCPStackOutputsCustomSaEmails | Unset = UNSET
    deprovision_sa_email: str | Unset = UNSET
    install_inputs: AppGCPStackOutputsInstallInputs | Unset = UNSET
    maintenance_sa_email: str | Unset = UNSET
    network_id: str | Unset = UNSET
    network_name: str | Unset = UNSET
    private_subnet_name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    provision_sa_email: str | Unset = UNSET
    public_subnet_name: str | Unset = UNSET
    region: str | Unset = UNSET
    runner_service_account_email: str | Unset = UNSET
    runner_subnet_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        break_glass_sa_emails: dict[str, Any] | Unset = UNSET
        if not isinstance(self.break_glass_sa_emails, Unset):
            break_glass_sa_emails = self.break_glass_sa_emails.to_dict()

        custom_sa_emails: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_sa_emails, Unset):
            custom_sa_emails = self.custom_sa_emails.to_dict()

        deprovision_sa_email = self.deprovision_sa_email

        install_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_inputs, Unset):
            install_inputs = self.install_inputs.to_dict()

        maintenance_sa_email = self.maintenance_sa_email

        network_id = self.network_id

        network_name = self.network_name

        private_subnet_name = self.private_subnet_name

        project_id = self.project_id

        provision_sa_email = self.provision_sa_email

        public_subnet_name = self.public_subnet_name

        region = self.region

        runner_service_account_email = self.runner_service_account_email

        runner_subnet_name = self.runner_subnet_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if break_glass_sa_emails is not UNSET:
            field_dict["break_glass_sa_emails"] = break_glass_sa_emails
        if custom_sa_emails is not UNSET:
            field_dict["custom_sa_emails"] = custom_sa_emails
        if deprovision_sa_email is not UNSET:
            field_dict["deprovision_sa_email"] = deprovision_sa_email
        if install_inputs is not UNSET:
            field_dict["install_inputs"] = install_inputs
        if maintenance_sa_email is not UNSET:
            field_dict["maintenance_sa_email"] = maintenance_sa_email
        if network_id is not UNSET:
            field_dict["network_id"] = network_id
        if network_name is not UNSET:
            field_dict["network_name"] = network_name
        if private_subnet_name is not UNSET:
            field_dict["private_subnet_name"] = private_subnet_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if provision_sa_email is not UNSET:
            field_dict["provision_sa_email"] = provision_sa_email
        if public_subnet_name is not UNSET:
            field_dict["public_subnet_name"] = public_subnet_name
        if region is not UNSET:
            field_dict["region"] = region
        if runner_service_account_email is not UNSET:
            field_dict["runner_service_account_email"] = runner_service_account_email
        if runner_subnet_name is not UNSET:
            field_dict["runner_subnet_name"] = runner_subnet_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_gcp_stack_outputs_break_glass_sa_emails import AppGCPStackOutputsBreakGlassSaEmails
        from ..models.app_gcp_stack_outputs_custom_sa_emails import AppGCPStackOutputsCustomSaEmails
        from ..models.app_gcp_stack_outputs_install_inputs import AppGCPStackOutputsInstallInputs

        d = dict(src_dict)
        _break_glass_sa_emails = d.pop("break_glass_sa_emails", UNSET)
        break_glass_sa_emails: AppGCPStackOutputsBreakGlassSaEmails | Unset
        if isinstance(_break_glass_sa_emails, Unset):
            break_glass_sa_emails = UNSET
        else:
            break_glass_sa_emails = AppGCPStackOutputsBreakGlassSaEmails.from_dict(_break_glass_sa_emails)

        _custom_sa_emails = d.pop("custom_sa_emails", UNSET)
        custom_sa_emails: AppGCPStackOutputsCustomSaEmails | Unset
        if isinstance(_custom_sa_emails, Unset):
            custom_sa_emails = UNSET
        else:
            custom_sa_emails = AppGCPStackOutputsCustomSaEmails.from_dict(_custom_sa_emails)

        deprovision_sa_email = d.pop("deprovision_sa_email", UNSET)

        _install_inputs = d.pop("install_inputs", UNSET)
        install_inputs: AppGCPStackOutputsInstallInputs | Unset
        if isinstance(_install_inputs, Unset):
            install_inputs = UNSET
        else:
            install_inputs = AppGCPStackOutputsInstallInputs.from_dict(_install_inputs)

        maintenance_sa_email = d.pop("maintenance_sa_email", UNSET)

        network_id = d.pop("network_id", UNSET)

        network_name = d.pop("network_name", UNSET)

        private_subnet_name = d.pop("private_subnet_name", UNSET)

        project_id = d.pop("project_id", UNSET)

        provision_sa_email = d.pop("provision_sa_email", UNSET)

        public_subnet_name = d.pop("public_subnet_name", UNSET)

        region = d.pop("region", UNSET)

        runner_service_account_email = d.pop("runner_service_account_email", UNSET)

        runner_subnet_name = d.pop("runner_subnet_name", UNSET)

        app_gcp_stack_outputs = cls(
            break_glass_sa_emails=break_glass_sa_emails,
            custom_sa_emails=custom_sa_emails,
            deprovision_sa_email=deprovision_sa_email,
            install_inputs=install_inputs,
            maintenance_sa_email=maintenance_sa_email,
            network_id=network_id,
            network_name=network_name,
            private_subnet_name=private_subnet_name,
            project_id=project_id,
            provision_sa_email=provision_sa_email,
            public_subnet_name=public_subnet_name,
            region=region,
            runner_service_account_email=runner_service_account_email,
            runner_subnet_name=runner_subnet_name,
        )

        app_gcp_stack_outputs.additional_properties = d
        return app_gcp_stack_outputs

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
