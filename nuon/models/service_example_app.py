from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceExampleApp")


@_attrs_define
class ServiceExampleApp:
    """
    Attributes:
        branch (str | Unset):
        category (str | Unset):
        cloud_provider (str | Unset):
        description (str | Unset):
        difficulty (str | Unset):
        directory (str | Unset):
        display_name (str | Unset):
        repo (str | Unset):
        slug (str | Unset):
        tags (list[str] | Unset):
    """

    branch: str | Unset = UNSET
    category: str | Unset = UNSET
    cloud_provider: str | Unset = UNSET
    description: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    directory: str | Unset = UNSET
    display_name: str | Unset = UNSET
    repo: str | Unset = UNSET
    slug: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        category = self.category

        cloud_provider = self.cloud_provider

        description = self.description

        difficulty = self.difficulty

        directory = self.directory

        display_name = self.display_name

        repo = self.repo

        slug = self.slug

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if category is not UNSET:
            field_dict["category"] = category
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if description is not UNSET:
            field_dict["description"] = description
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if directory is not UNSET:
            field_dict["directory"] = directory
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if repo is not UNSET:
            field_dict["repo"] = repo
        if slug is not UNSET:
            field_dict["slug"] = slug
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        category = d.pop("category", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        description = d.pop("description", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        directory = d.pop("directory", UNSET)

        display_name = d.pop("display_name", UNSET)

        repo = d.pop("repo", UNSET)

        slug = d.pop("slug", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        service_example_app = cls(
            branch=branch,
            category=category,
            cloud_provider=cloud_provider,
            description=description,
            difficulty=difficulty,
            directory=directory,
            display_name=display_name,
            repo=repo,
            slug=slug,
            tags=tags,
        )

        service_example_app.additional_properties = d
        return service_example_app

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
