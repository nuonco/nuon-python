from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
    from ..models.kube_cluster_info import KubeClusterInfo
    from ..models.plantypes_kubernetes_secret_sync import PlantypesKubernetesSecretSync
    from ..models.plantypes_sandbox_mode import PlantypesSandboxMode


T = TypeVar("T", bound="PlantypesSyncSecretsPlan")


@_attrs_define
class PlantypesSyncSecretsPlan:
    """
    Attributes:
        aws_auth (Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]):
        azure_auth (Union[Unset, GithubComPowertoolsdevMonoPkgAzureCredentialsConfig]):
        cluster_info (Union[Unset, KubeClusterInfo]):
        kubernetes_secrets (Union[Unset, list['PlantypesKubernetesSecretSync']]):
        sandbox_mode (Union[Unset, PlantypesSandboxMode]):
    """

    aws_auth: Union[Unset, "GithubComPowertoolsdevMonoPkgAwsCredentialsConfig"] = UNSET
    azure_auth: Union[Unset, "GithubComPowertoolsdevMonoPkgAzureCredentialsConfig"] = UNSET
    cluster_info: Union[Unset, "KubeClusterInfo"] = UNSET
    kubernetes_secrets: Union[Unset, list["PlantypesKubernetesSecretSync"]] = UNSET
    sandbox_mode: Union[Unset, "PlantypesSandboxMode"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aws_auth, Unset):
            aws_auth = self.aws_auth.to_dict()

        azure_auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.azure_auth, Unset):
            azure_auth = self.azure_auth.to_dict()

        cluster_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = self.cluster_info.to_dict()

        kubernetes_secrets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.kubernetes_secrets, Unset):
            kubernetes_secrets = []
            for kubernetes_secrets_item_data in self.kubernetes_secrets:
                kubernetes_secrets_item = kubernetes_secrets_item_data.to_dict()
                kubernetes_secrets.append(kubernetes_secrets_item)

        sandbox_mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_mode, Unset):
            sandbox_mode = self.sandbox_mode.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_auth is not UNSET:
            field_dict["aws_auth"] = aws_auth
        if azure_auth is not UNSET:
            field_dict["azure_auth"] = azure_auth
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if kubernetes_secrets is not UNSET:
            field_dict["kubernetes_secrets"] = kubernetes_secrets
        if sandbox_mode is not UNSET:
            field_dict["sandbox_mode"] = sandbox_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
            GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
        )
        from ..models.github_com_powertoolsdev_mono_pkg_azure_credentials_config import (
            GithubComPowertoolsdevMonoPkgAzureCredentialsConfig,
        )
        from ..models.kube_cluster_info import KubeClusterInfo
        from ..models.plantypes_kubernetes_secret_sync import PlantypesKubernetesSecretSync
        from ..models.plantypes_sandbox_mode import PlantypesSandboxMode

        d = dict(src_dict)
        _aws_auth = d.pop("aws_auth", UNSET)
        aws_auth: Union[Unset, GithubComPowertoolsdevMonoPkgAwsCredentialsConfig]
        if isinstance(_aws_auth, Unset):
            aws_auth = UNSET
        else:
            aws_auth = GithubComPowertoolsdevMonoPkgAwsCredentialsConfig.from_dict(_aws_auth)

        _azure_auth = d.pop("azure_auth", UNSET)
        azure_auth: Union[Unset, GithubComPowertoolsdevMonoPkgAzureCredentialsConfig]
        if isinstance(_azure_auth, Unset):
            azure_auth = UNSET
        else:
            azure_auth = GithubComPowertoolsdevMonoPkgAzureCredentialsConfig.from_dict(_azure_auth)

        _cluster_info = d.pop("cluster_info", UNSET)
        cluster_info: Union[Unset, KubeClusterInfo]
        if isinstance(_cluster_info, Unset):
            cluster_info = UNSET
        else:
            cluster_info = KubeClusterInfo.from_dict(_cluster_info)

        kubernetes_secrets = []
        _kubernetes_secrets = d.pop("kubernetes_secrets", UNSET)
        for kubernetes_secrets_item_data in _kubernetes_secrets or []:
            kubernetes_secrets_item = PlantypesKubernetesSecretSync.from_dict(kubernetes_secrets_item_data)

            kubernetes_secrets.append(kubernetes_secrets_item)

        _sandbox_mode = d.pop("sandbox_mode", UNSET)
        sandbox_mode: Union[Unset, PlantypesSandboxMode]
        if isinstance(_sandbox_mode, Unset):
            sandbox_mode = UNSET
        else:
            sandbox_mode = PlantypesSandboxMode.from_dict(_sandbox_mode)

        plantypes_sync_secrets_plan = cls(
            aws_auth=aws_auth,
            azure_auth=azure_auth,
            cluster_info=cluster_info,
            kubernetes_secrets=kubernetes_secrets,
            sandbox_mode=sandbox_mode,
        )

        plantypes_sync_secrets_plan.additional_properties = d
        return plantypes_sync_secrets_plan

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
