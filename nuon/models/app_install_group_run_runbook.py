from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallGroupRunRunbook")


@_attrs_define
class AppInstallGroupRunRunbook:
    """
    Attributes:
        attempt (int | Unset): Attempt increments when a retry of the step re-runs a runbook that failed,
            so the retry gets a fresh idempotency key instead of adopting the failed run.
        run_id (str | Unset):
        runbook_id (str | Unset):
        runbook_name (str | Unset):
        status (str | Unset):
        workflow_id (str | Unset):
    """

    attempt: int | Unset = UNSET
    run_id: str | Unset = UNSET
    runbook_id: str | Unset = UNSET
    runbook_name: str | Unset = UNSET
    status: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        run_id = self.run_id

        runbook_id = self.runbook_id

        runbook_name = self.runbook_name

        status = self.status

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if runbook_id is not UNSET:
            field_dict["runbook_id"] = runbook_id
        if runbook_name is not UNSET:
            field_dict["runbook_name"] = runbook_name
        if status is not UNSET:
            field_dict["status"] = status
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt = d.pop("attempt", UNSET)

        run_id = d.pop("run_id", UNSET)

        runbook_id = d.pop("runbook_id", UNSET)

        runbook_name = d.pop("runbook_name", UNSET)

        status = d.pop("status", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        app_install_group_run_runbook = cls(
            attempt=attempt,
            run_id=run_id,
            runbook_id=runbook_id,
            runbook_name=runbook_name,
            status=status,
            workflow_id=workflow_id,
        )

        app_install_group_run_runbook.additional_properties = d
        return app_install_group_run_runbook

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
