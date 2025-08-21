from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCreateInstallerRequestMetadata")


@_attrs_define
class ServiceCreateInstallerRequestMetadata:
    """
    Attributes:
        community_url (str):
        description (str):
        documentation_url (str):
        favicon_url (str):
        github_url (str):
        homepage_url (str):
        logo_url (str):
        copyright_markdown (Union[Unset, str]):
        demo_url (Union[Unset, str]):
        footer_markdown (Union[Unset, str]):
        og_image_url (Union[Unset, str]):
        post_install_markdown (Union[Unset, str]):
    """

    community_url: str
    description: str
    documentation_url: str
    favicon_url: str
    github_url: str
    homepage_url: str
    logo_url: str
    copyright_markdown: Union[Unset, str] = UNSET
    demo_url: Union[Unset, str] = UNSET
    footer_markdown: Union[Unset, str] = UNSET
    og_image_url: Union[Unset, str] = UNSET
    post_install_markdown: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        community_url = self.community_url

        description = self.description

        documentation_url = self.documentation_url

        favicon_url = self.favicon_url

        github_url = self.github_url

        homepage_url = self.homepage_url

        logo_url = self.logo_url

        copyright_markdown = self.copyright_markdown

        demo_url = self.demo_url

        footer_markdown = self.footer_markdown

        og_image_url = self.og_image_url

        post_install_markdown = self.post_install_markdown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "community_url": community_url,
                "description": description,
                "documentation_url": documentation_url,
                "favicon_url": favicon_url,
                "github_url": github_url,
                "homepage_url": homepage_url,
                "logo_url": logo_url,
            }
        )
        if copyright_markdown is not UNSET:
            field_dict["copyright_markdown"] = copyright_markdown
        if demo_url is not UNSET:
            field_dict["demo_url"] = demo_url
        if footer_markdown is not UNSET:
            field_dict["footer_markdown"] = footer_markdown
        if og_image_url is not UNSET:
            field_dict["og_image_url"] = og_image_url
        if post_install_markdown is not UNSET:
            field_dict["post_install_markdown"] = post_install_markdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        community_url = d.pop("community_url")

        description = d.pop("description")

        documentation_url = d.pop("documentation_url")

        favicon_url = d.pop("favicon_url")

        github_url = d.pop("github_url")

        homepage_url = d.pop("homepage_url")

        logo_url = d.pop("logo_url")

        copyright_markdown = d.pop("copyright_markdown", UNSET)

        demo_url = d.pop("demo_url", UNSET)

        footer_markdown = d.pop("footer_markdown", UNSET)

        og_image_url = d.pop("og_image_url", UNSET)

        post_install_markdown = d.pop("post_install_markdown", UNSET)

        service_create_installer_request_metadata = cls(
            community_url=community_url,
            description=description,
            documentation_url=documentation_url,
            favicon_url=favicon_url,
            github_url=github_url,
            homepage_url=homepage_url,
            logo_url=logo_url,
            copyright_markdown=copyright_markdown,
            demo_url=demo_url,
            footer_markdown=footer_markdown,
            og_image_url=og_image_url,
            post_install_markdown=post_install_markdown,
        )

        service_create_installer_request_metadata.additional_properties = d
        return service_create_installer_request_metadata

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
