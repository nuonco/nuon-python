from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_account import AppAccount
    from ..models.app_notebook_cell import AppNotebookCell
    from ..models.app_queue import AppQueue


T = TypeVar("T", bound="AppNotebook")


@_attrs_define
class AppNotebook:
    """
    Attributes:
        cell_count (int | Unset):
        cells (list[AppNotebookCell] | Unset):
        created_at (str | Unset):
        created_by (AppAccount | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        id (str | Unset):
        install_id (str | Unset):
        latest_run_at (str | Unset):
        name (str | Unset):
        queue (AppQueue | Unset):
        status (str | Unset):
        updated_at (str | Unset):
    """

    cell_count: int | Unset = UNSET
    cells: list[AppNotebookCell] | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: AppAccount | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    install_id: str | Unset = UNSET
    latest_run_at: str | Unset = UNSET
    name: str | Unset = UNSET
    queue: AppQueue | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cell_count = self.cell_count

        cells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cells, Unset):
            cells = []
            for cells_item_data in self.cells:
                cells_item = cells_item_data.to_dict()
                cells.append(cells_item)

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_id = self.created_by_id

        description = self.description

        id = self.id

        install_id = self.install_id

        latest_run_at = self.latest_run_at

        name = self.name

        queue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue, Unset):
            queue = self.queue.to_dict()

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cell_count is not UNSET:
            field_dict["cell_count"] = cell_count
        if cells is not UNSET:
            field_dict["cells"] = cells
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if install_id is not UNSET:
            field_dict["install_id"] = install_id
        if latest_run_at is not UNSET:
            field_dict["latest_run_at"] = latest_run_at
        if name is not UNSET:
            field_dict["name"] = name
        if queue is not UNSET:
            field_dict["queue"] = queue
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_account import AppAccount
        from ..models.app_notebook_cell import AppNotebookCell
        from ..models.app_queue import AppQueue

        d = dict(src_dict)
        cell_count = d.pop("cell_count", UNSET)

        _cells = d.pop("cells", UNSET)
        cells: list[AppNotebookCell] | Unset = UNSET
        if _cells is not UNSET:
            cells = []
            for cells_item_data in _cells:
                cells_item = AppNotebookCell.from_dict(cells_item_data)

                cells.append(cells_item)

        created_at = d.pop("created_at", UNSET)

        _created_by = d.pop("created_by", UNSET)
        created_by: AppAccount | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AppAccount.from_dict(_created_by)

        created_by_id = d.pop("created_by_id", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        install_id = d.pop("install_id", UNSET)

        latest_run_at = d.pop("latest_run_at", UNSET)

        name = d.pop("name", UNSET)

        _queue = d.pop("queue", UNSET)
        queue: AppQueue | Unset
        if isinstance(_queue, Unset):
            queue = UNSET
        else:
            queue = AppQueue.from_dict(_queue)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_notebook = cls(
            cell_count=cell_count,
            cells=cells,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            description=description,
            id=id,
            install_id=install_id,
            latest_run_at=latest_run_at,
            name=name,
            queue=queue,
            status=status,
            updated_at=updated_at,
        )

        app_notebook.additional_properties = d
        return app_notebook

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
