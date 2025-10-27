from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_assume_role_config import CredentialsAssumeRoleConfig
    from ..models.credentials_static_credentials import CredentialsStaticCredentials


T = TypeVar("T", bound="GithubComPowertoolsdevMonoPkgAwsCredentialsConfig")


@_attrs_define
class GithubComPowertoolsdevMonoPkgAwsCredentialsConfig:
    """
    Attributes:
        assume_role (Union[Unset, CredentialsAssumeRoleConfig]):
        cache_id (Union[Unset, str]): when cache ID is set, these credentials will be reused, up to the duration of the
            sessionTimeout (or default)
        profile (Union[Unset, str]): If profile is provided, we'll use that profile over the default credentials
        region (Union[Unset, str]):
        static (Union[Unset, CredentialsStaticCredentials]):
        use_default (Union[Unset, bool]):
    """

    assume_role: Union[Unset, "CredentialsAssumeRoleConfig"] = UNSET
    cache_id: Union[Unset, str] = UNSET
    profile: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    static: Union[Unset, "CredentialsStaticCredentials"] = UNSET
    use_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assume_role: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assume_role, Unset):
            assume_role = self.assume_role.to_dict()

        cache_id = self.cache_id

        profile = self.profile

        region = self.region

        static: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static, Unset):
            static = self.static.to_dict()

        use_default = self.use_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assume_role is not UNSET:
            field_dict["assume_role"] = assume_role
        if cache_id is not UNSET:
            field_dict["cache_id"] = cache_id
        if profile is not UNSET:
            field_dict["profile"] = profile
        if region is not UNSET:
            field_dict["region"] = region
        if static is not UNSET:
            field_dict["static"] = static
        if use_default is not UNSET:
            field_dict["use_default"] = use_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials_assume_role_config import CredentialsAssumeRoleConfig
        from ..models.credentials_static_credentials import CredentialsStaticCredentials

        d = dict(src_dict)
        _assume_role = d.pop("assume_role", UNSET)
        assume_role: Union[Unset, CredentialsAssumeRoleConfig]
        if isinstance(_assume_role, Unset):
            assume_role = UNSET
        else:
            assume_role = CredentialsAssumeRoleConfig.from_dict(_assume_role)

        cache_id = d.pop("cache_id", UNSET)

        profile = d.pop("profile", UNSET)

        region = d.pop("region", UNSET)

        _static = d.pop("static", UNSET)
        static: Union[Unset, CredentialsStaticCredentials]
        if isinstance(_static, Unset):
            static = UNSET
        else:
            static = CredentialsStaticCredentials.from_dict(_static)

        use_default = d.pop("use_default", UNSET)

        github_com_powertoolsdev_mono_pkg_aws_credentials_config = cls(
            assume_role=assume_role,
            cache_id=cache_id,
            profile=profile,
            region=region,
            static=static,
            use_default=use_default,
        )

        github_com_powertoolsdev_mono_pkg_aws_credentials_config.additional_properties = d
        return github_com_powertoolsdev_mono_pkg_aws_credentials_config

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
