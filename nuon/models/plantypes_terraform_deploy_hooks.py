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
    from ..models.plantypes_terraform_deploy_hooks_env_vars import PlantypesTerraformDeployHooksEnvVars


T = TypeVar("T", bound="PlantypesTerraformDeployHooks")


@_attrs_define
class PlantypesTerraformDeployHooks:
    """
    Attributes:
        enabled (bool | Unset):
        env_vars (PlantypesTerraformDeployHooksEnvVars | Unset):
        run_auth (GithubComPowertoolsdevMonoPkgAwsCredentialsConfig | Unset):
    """

    enabled: bool | Unset = UNSET
    env_vars: PlantypesTerraformDeployHooksEnvVars | Unset = UNSET
    run_auth: GithubComPowertoolsdevMonoPkgAwsCredentialsConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        env_vars: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        run_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_auth, Unset):
            run_auth = self.run_auth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars
        if run_auth is not UNSET:
            field_dict["runAuth"] = run_auth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_powertoolsdev_mono_pkg_aws_credentials_config import (
            GithubComPowertoolsdevMonoPkgAwsCredentialsConfig,
        )
        from ..models.plantypes_terraform_deploy_hooks_env_vars import PlantypesTerraformDeployHooksEnvVars

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _env_vars = d.pop("envVars", UNSET)
        env_vars: PlantypesTerraformDeployHooksEnvVars | Unset
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = PlantypesTerraformDeployHooksEnvVars.from_dict(_env_vars)

        _run_auth = d.pop("runAuth", UNSET)
        run_auth: GithubComPowertoolsdevMonoPkgAwsCredentialsConfig | Unset
        if isinstance(_run_auth, Unset):
            run_auth = UNSET
        else:
            run_auth = GithubComPowertoolsdevMonoPkgAwsCredentialsConfig.from_dict(_run_auth)

        plantypes_terraform_deploy_hooks = cls(
            enabled=enabled,
            env_vars=env_vars,
            run_auth=run_auth,
        )

        plantypes_terraform_deploy_hooks.additional_properties = d
        return plantypes_terraform_deploy_hooks

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
