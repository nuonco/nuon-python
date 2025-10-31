from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_aws_stack_outputs_break_glass_role_arns import AppAWSStackOutputsBreakGlassRoleArns
    from ..models.app_aws_stack_outputs_install_inputs import AppAWSStackOutputsInstallInputs


T = TypeVar("T", bound="AppAWSStackOutputs")


@_attrs_define
class AppAWSStackOutputs:
    """
    Attributes:
        account_id (str | Unset):
        break_glass_role_arns (AppAWSStackOutputsBreakGlassRoleArns | Unset):
        deprovision_iam_role_arn (str | Unset):
        install_inputs (AppAWSStackOutputsInstallInputs | Unset):
        maintenance_iam_role_arn (str | Unset):
        private_subnets (list[str] | Unset):
        provision_iam_role_arn (str | Unset):
        public_subnets (list[str] | Unset):
        region (str | Unset):
        runner_iam_role_arn (str | Unset):
        runner_subnet (str | Unset):
        vpc_id (str | Unset):
    """

    account_id: str | Unset = UNSET
    break_glass_role_arns: AppAWSStackOutputsBreakGlassRoleArns | Unset = UNSET
    deprovision_iam_role_arn: str | Unset = UNSET
    install_inputs: AppAWSStackOutputsInstallInputs | Unset = UNSET
    maintenance_iam_role_arn: str | Unset = UNSET
    private_subnets: list[str] | Unset = UNSET
    provision_iam_role_arn: str | Unset = UNSET
    public_subnets: list[str] | Unset = UNSET
    region: str | Unset = UNSET
    runner_iam_role_arn: str | Unset = UNSET
    runner_subnet: str | Unset = UNSET
    vpc_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        break_glass_role_arns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.break_glass_role_arns, Unset):
            break_glass_role_arns = self.break_glass_role_arns.to_dict()

        deprovision_iam_role_arn = self.deprovision_iam_role_arn

        install_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.install_inputs, Unset):
            install_inputs = self.install_inputs.to_dict()

        maintenance_iam_role_arn = self.maintenance_iam_role_arn

        private_subnets: list[str] | Unset = UNSET
        if not isinstance(self.private_subnets, Unset):
            private_subnets = self.private_subnets

        provision_iam_role_arn = self.provision_iam_role_arn

        public_subnets: list[str] | Unset = UNSET
        if not isinstance(self.public_subnets, Unset):
            public_subnets = self.public_subnets

        region = self.region

        runner_iam_role_arn = self.runner_iam_role_arn

        runner_subnet = self.runner_subnet

        vpc_id = self.vpc_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if break_glass_role_arns is not UNSET:
            field_dict["break_glass_role_arns"] = break_glass_role_arns
        if deprovision_iam_role_arn is not UNSET:
            field_dict["deprovision_iam_role_arn"] = deprovision_iam_role_arn
        if install_inputs is not UNSET:
            field_dict["install_inputs"] = install_inputs
        if maintenance_iam_role_arn is not UNSET:
            field_dict["maintenance_iam_role_arn"] = maintenance_iam_role_arn
        if private_subnets is not UNSET:
            field_dict["private_subnets"] = private_subnets
        if provision_iam_role_arn is not UNSET:
            field_dict["provision_iam_role_arn"] = provision_iam_role_arn
        if public_subnets is not UNSET:
            field_dict["public_subnets"] = public_subnets
        if region is not UNSET:
            field_dict["region"] = region
        if runner_iam_role_arn is not UNSET:
            field_dict["runner_iam_role_arn"] = runner_iam_role_arn
        if runner_subnet is not UNSET:
            field_dict["runner_subnet"] = runner_subnet
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_aws_stack_outputs_break_glass_role_arns import AppAWSStackOutputsBreakGlassRoleArns
        from ..models.app_aws_stack_outputs_install_inputs import AppAWSStackOutputsInstallInputs

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        _break_glass_role_arns = d.pop("break_glass_role_arns", UNSET)
        break_glass_role_arns: AppAWSStackOutputsBreakGlassRoleArns | Unset
        if isinstance(_break_glass_role_arns, Unset):
            break_glass_role_arns = UNSET
        else:
            break_glass_role_arns = AppAWSStackOutputsBreakGlassRoleArns.from_dict(_break_glass_role_arns)

        deprovision_iam_role_arn = d.pop("deprovision_iam_role_arn", UNSET)

        _install_inputs = d.pop("install_inputs", UNSET)
        install_inputs: AppAWSStackOutputsInstallInputs | Unset
        if isinstance(_install_inputs, Unset):
            install_inputs = UNSET
        else:
            install_inputs = AppAWSStackOutputsInstallInputs.from_dict(_install_inputs)

        maintenance_iam_role_arn = d.pop("maintenance_iam_role_arn", UNSET)

        private_subnets = cast(list[str], d.pop("private_subnets", UNSET))

        provision_iam_role_arn = d.pop("provision_iam_role_arn", UNSET)

        public_subnets = cast(list[str], d.pop("public_subnets", UNSET))

        region = d.pop("region", UNSET)

        runner_iam_role_arn = d.pop("runner_iam_role_arn", UNSET)

        runner_subnet = d.pop("runner_subnet", UNSET)

        vpc_id = d.pop("vpc_id", UNSET)

        app_aws_stack_outputs = cls(
            account_id=account_id,
            break_glass_role_arns=break_glass_role_arns,
            deprovision_iam_role_arn=deprovision_iam_role_arn,
            install_inputs=install_inputs,
            maintenance_iam_role_arn=maintenance_iam_role_arn,
            private_subnets=private_subnets,
            provision_iam_role_arn=provision_iam_role_arn,
            public_subnets=public_subnets,
            region=region,
            runner_iam_role_arn=runner_iam_role_arn,
            runner_subnet=runner_subnet,
            vpc_id=vpc_id,
        )

        app_aws_stack_outputs.additional_properties = d
        return app_aws_stack_outputs

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
