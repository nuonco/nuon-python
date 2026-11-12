from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_install_deployment_source_diff_kind import ServiceInstallDeploymentSourceDiffKind
from ..models.service_install_deployment_source_diff_status import ServiceInstallDeploymentSourceDiffStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_install_deployment_source_build import ServiceInstallDeploymentSourceBuild
    from ..models.service_install_deployment_source_file import ServiceInstallDeploymentSourceFile
    from ..models.service_install_deployment_source_file_content import ServiceInstallDeploymentSourceFileContent


T = TypeVar("T", bound="ServiceInstallDeploymentSourceDiff")


@_attrs_define
class ServiceInstallDeploymentSourceDiff:
    """
    Attributes:
        after (ServiceInstallDeploymentSourceBuild | Unset):
        before (ServiceInstallDeploymentSourceBuild | Unset):
        files (list[ServiceInstallDeploymentSourceFile] | Unset):
        kind (ServiceInstallDeploymentSourceDiffKind | Unset):
        message (str | Unset):
        name (str | Unset):
        partial (bool | Unset):
        reasons (list[str] | Unset):
        selected_file (ServiceInstallDeploymentSourceFileContent | Unset):
        status (ServiceInstallDeploymentSourceDiffStatus | Unset):
    """

    after: ServiceInstallDeploymentSourceBuild | Unset = UNSET
    before: ServiceInstallDeploymentSourceBuild | Unset = UNSET
    files: list[ServiceInstallDeploymentSourceFile] | Unset = UNSET
    kind: ServiceInstallDeploymentSourceDiffKind | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    partial: bool | Unset = UNSET
    reasons: list[str] | Unset = UNSET
    selected_file: ServiceInstallDeploymentSourceFileContent | Unset = UNSET
    status: ServiceInstallDeploymentSourceDiffStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after, Unset):
            after = self.after.to_dict()

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        message = self.message

        name = self.name

        partial = self.partial

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        selected_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_file, Unset):
            selected_file = self.selected_file.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if files is not UNSET:
            field_dict["files"] = files
        if kind is not UNSET:
            field_dict["kind"] = kind
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if partial is not UNSET:
            field_dict["partial"] = partial
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if selected_file is not UNSET:
            field_dict["selected_file"] = selected_file
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_install_deployment_source_build import ServiceInstallDeploymentSourceBuild  # noqa: PLC0415
        from ..models.service_install_deployment_source_file import ServiceInstallDeploymentSourceFile  # noqa: PLC0415
        from ..models.service_install_deployment_source_file_content import ServiceInstallDeploymentSourceFileContent  # noqa: PLC0415

        d = dict(src_dict)
        _after = d.pop("after", UNSET)
        after: ServiceInstallDeploymentSourceBuild | Unset
        if isinstance(_after, Unset):
            after = UNSET
        else:
            after = ServiceInstallDeploymentSourceBuild.from_dict(_after)

        _before = d.pop("before", UNSET)
        before: ServiceInstallDeploymentSourceBuild | Unset
        if isinstance(_before, Unset):
            before = UNSET
        else:
            before = ServiceInstallDeploymentSourceBuild.from_dict(_before)

        _files = d.pop("files", UNSET)
        files: list[ServiceInstallDeploymentSourceFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ServiceInstallDeploymentSourceFile.from_dict(files_item_data)

                files.append(files_item)

        _kind = d.pop("kind", UNSET)
        kind: ServiceInstallDeploymentSourceDiffKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ServiceInstallDeploymentSourceDiffKind(_kind)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        partial = d.pop("partial", UNSET)

        reasons = cast(list[str], d.pop("reasons", UNSET))

        _selected_file = d.pop("selected_file", UNSET)
        selected_file: ServiceInstallDeploymentSourceFileContent | Unset
        if isinstance(_selected_file, Unset):
            selected_file = UNSET
        else:
            selected_file = ServiceInstallDeploymentSourceFileContent.from_dict(_selected_file)

        _status = d.pop("status", UNSET)
        status: ServiceInstallDeploymentSourceDiffStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ServiceInstallDeploymentSourceDiffStatus(_status)

        service_install_deployment_source_diff = cls(
            after=after,
            before=before,
            files=files,
            kind=kind,
            message=message,
            name=name,
            partial=partial,
            reasons=reasons,
            selected_file=selected_file,
            status=status,
        )

        service_install_deployment_source_diff.additional_properties = d
        return service_install_deployment_source_diff

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
