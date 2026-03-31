from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_composite_status import AppCompositeStatus
    from ..models.app_onboarding_app_config import AppOnboardingAppConfig


T = TypeVar("T", bound="AppOnboarding")


@_attrs_define
class AppOnboarding:
    """
    Attributes:
        account_id (str | Unset):
        app_attributes (list[str] | Unset):
        app_branch_id (str | Unset):
        app_config (AppOnboardingAppConfig | Unset):
        app_id (str | Unset):
        app_type (str | Unset): Step 2: Your Stack
        cloud_provider (str | Unset):
        created_at (str | Unset):
        created_by_id (str | Unset):
        current_step (str | Unset):
        example_app_slug (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        install_mode (str | Unset): Step 3: Install
        org_id (str | Unset): Step 1: Organization
        status (str | Unset):
        status_v2 (AppCompositeStatus | Unset):
        step_error (str | Unset):
        step_status (str | Unset): Async step status (for queue-based signal processing)
        updated_at (str | Unset):
        workflow_id (str | Unset):
    """

    account_id: str | Unset = UNSET
    app_attributes: list[str] | Unset = UNSET
    app_branch_id: str | Unset = UNSET
    app_config: AppOnboardingAppConfig | Unset = UNSET
    app_id: str | Unset = UNSET
    app_type: str | Unset = UNSET
    cloud_provider: str | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by_id: str | Unset = UNSET
    current_step: str | Unset = UNSET
    example_app_slug: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    install_mode: str | Unset = UNSET
    org_id: str | Unset = UNSET
    status: str | Unset = UNSET
    status_v2: AppCompositeStatus | Unset = UNSET
    step_error: str | Unset = UNSET
    step_status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        app_attributes: list[str] | Unset = UNSET
        if not isinstance(self.app_attributes, Unset):
            app_attributes = self.app_attributes

        app_branch_id = self.app_branch_id

        app_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_config, Unset):
            app_config = self.app_config.to_dict()

        app_id = self.app_id

        app_type = self.app_type

        cloud_provider = self.cloud_provider

        created_at = self.created_at

        created_by_id = self.created_by_id

        current_step = self.current_step

        example_app_slug = self.example_app_slug

        id = self.id

        install_id = self.install_id

        install_mode = self.install_mode

        org_id = self.org_id

        status = self.status

        status_v2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_v2, Unset):
            status_v2 = self.status_v2.to_dict()

        step_error = self.step_error

        step_status = self.step_status

        updated_at = self.updated_at

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if app_attributes is not UNSET:
            field_dict["app_attributes"] = app_attributes
        if app_branch_id is not UNSET:
            field_dict["app_branch_id"] = app_branch_id
        if app_config is not UNSET:
            field_dict["app_config"] = app_config
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if app_type is not UNSET:
            field_dict["app_type"] = app_type
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if current_step is not UNSET:
            field_dict["current_step"] = current_step
        if example_app_slug is not UNSET:
            field_dict["example_app_slug"] = example_app_slug
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if install_mode is not UNSET:
            field_dict["install_mode"] = install_mode
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_v2 is not UNSET:
            field_dict["status_v2"] = status_v2
        if step_error is not UNSET:
            field_dict["step_error"] = step_error
        if step_status is not UNSET:
            field_dict["step_status"] = step_status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_composite_status import AppCompositeStatus
        from ..models.app_onboarding_app_config import AppOnboardingAppConfig

        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        app_attributes = cast(list[str], d.pop("app_attributes", UNSET))

        app_branch_id = d.pop("app_branch_id", UNSET)

        _app_config = d.pop("app_config", UNSET)
        app_config: AppOnboardingAppConfig | Unset
        if isinstance(_app_config, Unset):
            app_config = UNSET
        else:
            app_config = AppOnboardingAppConfig.from_dict(_app_config)

        app_id = d.pop("app_id", UNSET)

        app_type = d.pop("app_type", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        current_step = d.pop("current_step", UNSET)

        example_app_slug = d.pop("example_app_slug", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        install_mode = d.pop("install_mode", UNSET)

        org_id = d.pop("org_id", UNSET)

        status = d.pop("status", UNSET)

        _status_v2 = d.pop("status_v2", UNSET)
        status_v2: AppCompositeStatus | Unset
        if isinstance(_status_v2, Unset):
            status_v2 = UNSET
        else:
            status_v2 = AppCompositeStatus.from_dict(_status_v2)

        step_error = d.pop("step_error", UNSET)

        step_status = d.pop("step_status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        app_onboarding = cls(
            account_id=account_id,
            app_attributes=app_attributes,
            app_branch_id=app_branch_id,
            app_config=app_config,
            app_id=app_id,
            app_type=app_type,
            cloud_provider=cloud_provider,
            created_at=created_at,
            created_by_id=created_by_id,
            current_step=current_step,
            example_app_slug=example_app_slug,
            id=id,
            install_id=install_id,
            install_mode=install_mode,
            org_id=org_id,
            status=status,
            status_v2=status_v2,
            step_error=step_error,
            step_status=step_status,
            updated_at=updated_at,
            workflow_id=workflow_id,
        )

        app_onboarding.additional_properties = d
        return app_onboarding

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
