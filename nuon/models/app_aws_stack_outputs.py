from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppAWSStackOutputs")


@_attrs_define
class AppAWSStackOutputs:
    """
    Attributes:
        account_id (Union[Unset, str]):
        deprovision_iam_role_arn (Union[Unset, str]):
        maintenance_iam_role_arn (Union[Unset, str]):
        private_subnets (Union[Unset, list[str]]):
        provision_iam_role_arn (Union[Unset, str]):
        public_subnets (Union[Unset, list[str]]):
        region (Union[Unset, str]):
        runner_iam_role_arn (Union[Unset, str]):
        runner_subnet (Union[Unset, str]):
        vpc_id (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    deprovision_iam_role_arn: Union[Unset, str] = UNSET
    maintenance_iam_role_arn: Union[Unset, str] = UNSET
    private_subnets: Union[Unset, list[str]] = UNSET
    provision_iam_role_arn: Union[Unset, str] = UNSET
    public_subnets: Union[Unset, list[str]] = UNSET
    region: Union[Unset, str] = UNSET
    runner_iam_role_arn: Union[Unset, str] = UNSET
    runner_subnet: Union[Unset, str] = UNSET
    vpc_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        deprovision_iam_role_arn = self.deprovision_iam_role_arn

        maintenance_iam_role_arn = self.maintenance_iam_role_arn

        private_subnets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.private_subnets, Unset):
            private_subnets = self.private_subnets

        provision_iam_role_arn = self.provision_iam_role_arn

        public_subnets: Union[Unset, list[str]] = UNSET
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
        if deprovision_iam_role_arn is not UNSET:
            field_dict["deprovision_iam_role_arn"] = deprovision_iam_role_arn
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
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        deprovision_iam_role_arn = d.pop("deprovision_iam_role_arn", UNSET)

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
            deprovision_iam_role_arn=deprovision_iam_role_arn,
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
