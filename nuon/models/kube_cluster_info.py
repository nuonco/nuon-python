from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
        GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
    )
    from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
        GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
    )
    from ..models.kube_cluster_info_env_vars import KubeClusterInfoEnvVars


T = TypeVar("T", bound="KubeClusterInfo")


@_attrs_define
class KubeClusterInfo:
    """
    Attributes:
        aws_auth (GithubComPowertoolsdevMonoPkgAwsCredentialsConfig | Unset):
        azure_auth (GithubComPowertoolsdevMonoPkgAzureCredentialsConfig | Unset):
        ca_data (str | Unset): CAData is the base64 encoded public certificate
        endpoint (str | Unset): Endpoint is the URL of the k8s api server
        env_vars (KubeClusterInfoEnvVars | Unset):
        id (str | Unset): ID is the ID of the EKS cluster
        inline (bool | Unset): If this is set, we will _not_ use aws-iam-authenticator, but rather inline create the
            token
        kube_config (str | Unset): KubeConfig will override the kube config, and be parsed instead of generating a new
            one
        trusted_role_arn (str | Unset): TrustedRoleARN is the arn of the role that should be assumed to interact with
            the cluster
            NOTE(JM): we are deprecating this
    """

    aws_auth: GithubComPowertoolsdevMonoPkgAwsCredentialsConfig | Unset = UNSET
    azure_auth: GithubComPowertoolsdevMonoPkgAzureCredentialsConfig | Unset = UNSET
    ca_data: str | Unset = UNSET
    endpoint: str | Unset = UNSET
    env_vars: KubeClusterInfoEnvVars | Unset = UNSET
    id: str | Unset = UNSET
    inline: bool | Unset = UNSET
    kube_config: str | Unset = UNSET
    trusted_role_arn: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        azure_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_auth, Unset):
            azure_auth = self.azure_auth.to_dict()

        ca_data = self.ca_data

        endpoint = self.endpoint

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        id = self.id

        inline = self.inline

        kube_config = self.kube_config

        trusted_role_arn = self.trusted_role_arn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if azure_auth is not UNSET:
            field_dict["azure_auth"] = azure_auth
        if ca_data is not UNSET:
            field_dict["ca_data"] = ca_data
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if id is not UNSET:
            field_dict["id"] = id
        if inline is not UNSET:
            field_dict["inline"] = inline
        if kube_config is not UNSET:
            field_dict["kube_config"] = kube_config
        if trusted_role_arn is not UNSET:
            field_dict["trusted_role_arn"] = trusted_role_arn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
            GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
        )
        from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
            GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
        )
        from ..models.kube_cluster_info_env_vars import KubeClusterInfoEnvVars

        d = dict(src_dict)
        _aws_auth = d.pop("aws_auth", UNSET)
        aws_auth: GithubComPowertoolsdevMonoPkgAwsCredentialsConfig | Unset
        if isinstance(_aws_auth, Unset):
            aws_auth = UNSET
        else:
            aws_auth = GithubComPowertoolsdevMonoPkgAwsCredentialsConfig.from_dict(_aws_auth)

        _azure_auth = d.pop("azure_auth", UNSET)
        azure_auth: GithubComPowertoolsdevMonoPkgAzureCredentialsConfig | Unset
        if isinstance(_azure_auth, Unset):
            azure_auth = UNSET
        else:
            azure_auth = GithubComPowertoolsdevMonoPkgAzureCredentialsConfig.from_dict(_azure_auth)

        ca_data = d.pop("ca_data", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: KubeClusterInfoEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = KubeClusterInfoEnvVars.from_dict(_env_vars)

        id = d.pop("id", UNSET)

        inline = d.pop("inline", UNSET)

        kube_config = d.pop("kube_config", UNSET)

        trusted_role_arn = d.pop("trusted_role_arn", UNSET)

        kube_cluster_info = cls(
            aws_auth=aws_auth,
            azure_auth=azure_auth,
            ca_data=ca_data,
            endpoint=endpoint,
            env_vars=env_vars,
            id=id,
            inline=inline,
            kube_config=kube_config,
            trusted_role_arn=trusted_role_arn,
        )

        kube_cluster_info.additional_properties = d
        return kube_cluster_info

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
