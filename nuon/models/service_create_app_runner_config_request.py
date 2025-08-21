from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_runner_config_helm_driver_type import AppAppRunnerConfigHelmDriverType
from ..models.app_app_runner_type import AppAppRunnerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_create_app_runner_config_request_env_vars import ServiceCreateAppRunnerConfigRequestEnvVars


T = TypeVar("T", bound="ServiceCreateAppRunnerConfigRequest")


@_attrs_define
class ServiceCreateAppRunnerConfigRequest:
    """
    Attributes:
        type_ (AppAppRunnerType):
        app_config_id (Union[Unset, str]):
        env_vars (Union[Unset, ServiceCreateAppRunnerConfigRequestEnvVars]):
        helm_driver (Union[Unset, AppAppRunnerConfigHelmDriverType]):
        init_script_url (Union[Unset, str]):
    """

    type_: AppAppRunnerType
    app_config_id: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "ServiceCreateAppRunnerConfigRequestEnvVars"] = UNSET
    helm_driver: Union[Unset, AppAppRunnerConfigHelmDriverType] = UNSET
    init_script_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        app_config_id = self.app_config_id

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        helm_driver: Union[Unset, str] = UNSET
        if not isinstance(self.helm_driver, Unset):
            helm_driver = self.helm_driver.value

        init_script_url = self.init_script_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if app_config_id is not UNSET:
            field_dict["app_config_id"] = app_config_id
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if helm_driver is not UNSET:
            field_dict["helm_driver"] = helm_driver
        if init_script_url is not UNSET:
            field_dict["init_script_url"] = init_script_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_create_app_runner_config_request_env_vars import (
            ServiceCreateAppRunnerConfigRequestEnvVars,
        )

        d = dict(src_dict)
        type_ = AppAppRunnerType(d.pop("type"))

        app_config_id = d.pop("app_config_id", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, ServiceCreateAppRunnerConfigRequestEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ServiceCreateAppRunnerConfigRequestEnvVars.from_dict(_env_vars)

        _helm_driver = d.pop("helm_driver", UNSET)
        helm_driver: Union[Unset, AppAppRunnerConfigHelmDriverType]
        if isinstance(_helm_driver, Unset):
            helm_driver = UNSET
        else:
            helm_driver = AppAppRunnerConfigHelmDriverType(_helm_driver)

        init_script_url = d.pop("init_script_url", UNSET)

        service_create_app_runner_config_request = cls(
            type_=type_,
            app_config_id=app_config_id,
            env_vars=env_vars,
            helm_driver=helm_driver,
            init_script_url=init_script_url,
        )

        service_create_app_runner_config_request.additional_properties = d
        return service_create_app_runner_config_request

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
