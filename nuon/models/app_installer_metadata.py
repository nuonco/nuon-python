from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppInstallerMetadata")


@_attrs_define
class AppInstallerMetadata:
    """
    Attributes:
        community_url (Union[Unset, str]):
        copyright_markdown (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by_id (Union[Unset, str]):
        demo_url (Union[Unset, str]):
        description (Union[Unset, str]):
        documentation_url (Union[Unset, str]):
        favicon_url (Union[Unset, str]):
        footer_markdown (Union[Unset, str]):
        formatted_demo_url (Union[Unset, str]):
        github_url (Union[Unset, str]):
        homepage_url (Union[Unset, str]):
        id (Union[Unset, str]):
        installer_id (Union[Unset, str]):
        logo_url (Union[Unset, str]):
        name (Union[Unset, str]):
        og_image_url (Union[Unset, str]):
        post_install_markdown (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    community_url: Union[Unset, str] = UNSET
    copyright_markdown: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by_id: Union[Unset, str] = UNSET
    demo_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    documentation_url: Union[Unset, str] = UNSET
    favicon_url: Union[Unset, str] = UNSET
    footer_markdown: Union[Unset, str] = UNSET
    formatted_demo_url: Union[Unset, str] = UNSET
    github_url: Union[Unset, str] = UNSET
    homepage_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    installer_id: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    og_image_url: Union[Unset, str] = UNSET
    post_install_markdown: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        community_url = self.community_url

        copyright_markdown = self.copyright_markdown

        created_at = self.created_at

        created_by_id = self.created_by_id

        demo_url = self.demo_url

        description = self.description

        documentation_url = self.documentation_url

        favicon_url = self.favicon_url

        footer_markdown = self.footer_markdown

        formatted_demo_url = self.formatted_demo_url

        github_url = self.github_url

        homepage_url = self.homepage_url

        id = self.id

        installer_id = self.installer_id

        logo_url = self.logo_url

        name = self.name

        og_image_url = self.og_image_url

        post_install_markdown = self.post_install_markdown

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if community_url is not UNSET:
            field_dict["community_url"] = community_url
        if copyright_markdown is not UNSET:
            field_dict["copyright_markdown"] = copyright_markdown
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_id is not UNSET:
            field_dict["created_by_id"] = created_by_id
        if demo_url is not UNSET:
            field_dict["demo_url"] = demo_url
        if description is not UNSET:
            field_dict["description"] = description
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if favicon_url is not UNSET:
            field_dict["favicon_url"] = favicon_url
        if footer_markdown is not UNSET:
            field_dict["footer_markdown"] = footer_markdown
        if formatted_demo_url is not UNSET:
            field_dict["formatted_demo_url"] = formatted_demo_url
        if github_url is not UNSET:
            field_dict["github_url"] = github_url
        if homepage_url is not UNSET:
            field_dict["homepage_url"] = homepage_url
        if id is not UNSET:
            field_dict["id"] = id
        if installer_id is not UNSET:
            field_dict["installer_id"] = installer_id
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if og_image_url is not UNSET:
            field_dict["og_image_url"] = og_image_url
        if post_install_markdown is not UNSET:
            field_dict["post_install_markdown"] = post_install_markdown
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        community_url = d.pop("community_url", UNSET)

        copyright_markdown = d.pop("copyright_markdown", UNSET)

        created_at = d.pop("created_at", UNSET)

        created_by_id = d.pop("created_by_id", UNSET)

        demo_url = d.pop("demo_url", UNSET)

        description = d.pop("description", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        favicon_url = d.pop("favicon_url", UNSET)

        footer_markdown = d.pop("footer_markdown", UNSET)

        formatted_demo_url = d.pop("formatted_demo_url", UNSET)

        github_url = d.pop("github_url", UNSET)

        homepage_url = d.pop("homepage_url", UNSET)

        id = d.pop("id", UNSET)

        installer_id = d.pop("installer_id", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        name = d.pop("name", UNSET)

        og_image_url = d.pop("og_image_url", UNSET)

        post_install_markdown = d.pop("post_install_markdown", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        app_installer_metadata = cls(
            community_url=community_url,
            copyright_markdown=copyright_markdown,
            created_at=created_at,
            created_by_id=created_by_id,
            demo_url=demo_url,
            description=description,
            documentation_url=documentation_url,
            favicon_url=favicon_url,
            footer_markdown=footer_markdown,
            formatted_demo_url=formatted_demo_url,
            github_url=github_url,
            homepage_url=homepage_url,
            id=id,
            installer_id=installer_id,
            logo_url=logo_url,
            name=name,
            og_image_url=og_image_url,
            post_install_markdown=post_install_markdown,
            updated_at=updated_at,
        )

        app_installer_metadata.additional_properties = d
        return app_installer_metadata

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
