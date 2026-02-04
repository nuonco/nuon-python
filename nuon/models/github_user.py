from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_plan import GithubPlan
    from ..models.github_text_match import GithubTextMatch
    from ..models.github_timestamp import GithubTimestamp
    from ..models.github_user_permissions import GithubUserPermissions


T = TypeVar("T", bound="GithubUser")


@_attrs_define
class GithubUser:
    """
    Attributes:
        avatar_url (str | Unset):
        bio (str | Unset):
        blog (str | Unset):
        collaborators (int | Unset):
        company (str | Unset):
        created_at (GithubTimestamp | Unset):
        disk_usage (int | Unset):
        email (str | Unset):
        events_url (str | Unset):
        followers (int | Unset):
        followers_url (str | Unset):
        following (int | Unset):
        following_url (str | Unset):
        gists_url (str | Unset):
        gravatar_id (str | Unset):
        hireable (bool | Unset):
        html_url (str | Unset):
        id (int | Unset):
        ldap_dn (str | Unset):
        location (str | Unset):
        login (str | Unset):
        name (str | Unset):
        node_id (str | Unset):
        organizations_url (str | Unset):
        owned_private_repos (int | Unset):
        permissions (GithubUserPermissions | Unset): Permissions and RoleName identify the permissions and role that a
            user has on a given
            repository. These are only populated when calling Repositories.ListCollaborators.
        plan (GithubPlan | Unset):
        private_gists (int | Unset):
        public_gists (int | Unset):
        public_repos (int | Unset):
        received_events_url (str | Unset):
        repos_url (str | Unset):
        role_name (str | Unset):
        site_admin (bool | Unset):
        starred_url (str | Unset):
        subscriptions_url (str | Unset):
        suspended_at (GithubTimestamp | Unset):
        text_matches (list[GithubTextMatch] | Unset): TextMatches is only populated from search results that request
            text matches
            See: search.go and https://docs.github.com/en/rest/search/#text-match-metadata
        total_private_repos (int | Unset):
        twitter_username (str | Unset):
        two_factor_authentication (bool | Unset):
        type_ (str | Unset):
        updated_at (GithubTimestamp | Unset):
        url (str | Unset): API URLs
    """

    avatar_url: str | Unset = UNSET
    bio: str | Unset = UNSET
    blog: str | Unset = UNSET
    collaborators: int | Unset = UNSET
    company: str | Unset = UNSET
    created_at: GithubTimestamp | Unset = UNSET
    disk_usage: int | Unset = UNSET
    email: str | Unset = UNSET
    events_url: str | Unset = UNSET
    followers: int | Unset = UNSET
    followers_url: str | Unset = UNSET
    following: int | Unset = UNSET
    following_url: str | Unset = UNSET
    gists_url: str | Unset = UNSET
    gravatar_id: str | Unset = UNSET
    hireable: bool | Unset = UNSET
    html_url: str | Unset = UNSET
    id: int | Unset = UNSET
    ldap_dn: str | Unset = UNSET
    location: str | Unset = UNSET
    login: str | Unset = UNSET
    name: str | Unset = UNSET
    node_id: str | Unset = UNSET
    organizations_url: str | Unset = UNSET
    owned_private_repos: int | Unset = UNSET
    permissions: GithubUserPermissions | Unset = UNSET
    plan: GithubPlan | Unset = UNSET
    private_gists: int | Unset = UNSET
    public_gists: int | Unset = UNSET
    public_repos: int | Unset = UNSET
    received_events_url: str | Unset = UNSET
    repos_url: str | Unset = UNSET
    role_name: str | Unset = UNSET
    site_admin: bool | Unset = UNSET
    starred_url: str | Unset = UNSET
    subscriptions_url: str | Unset = UNSET
    suspended_at: GithubTimestamp | Unset = UNSET
    text_matches: list[GithubTextMatch] | Unset = UNSET
    total_private_repos: int | Unset = UNSET
    twitter_username: str | Unset = UNSET
    two_factor_authentication: bool | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: GithubTimestamp | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        bio = self.bio

        blog = self.blog

        collaborators = self.collaborators

        company = self.company

        created_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        disk_usage = self.disk_usage

        email = self.email

        events_url = self.events_url

        followers = self.followers

        followers_url = self.followers_url

        following = self.following

        following_url = self.following_url

        gists_url = self.gists_url

        gravatar_id = self.gravatar_id

        hireable = self.hireable

        html_url = self.html_url

        id = self.id

        ldap_dn = self.ldap_dn

        location = self.location

        login = self.login

        name = self.name

        node_id = self.node_id

        organizations_url = self.organizations_url

        owned_private_repos = self.owned_private_repos

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        private_gists = self.private_gists

        public_gists = self.public_gists

        public_repos = self.public_repos

        received_events_url = self.received_events_url

        repos_url = self.repos_url

        role_name = self.role_name

        site_admin = self.site_admin

        starred_url = self.starred_url

        subscriptions_url = self.subscriptions_url

        suspended_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suspended_at, Unset):
            suspended_at = self.suspended_at.to_dict()

        text_matches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.text_matches, Unset):
            text_matches = []
            for text_matches_item_data in self.text_matches:
                text_matches_item = text_matches_item_data.to_dict()
                text_matches.append(text_matches_item)

        total_private_repos = self.total_private_repos

        twitter_username = self.twitter_username

        two_factor_authentication = self.two_factor_authentication

        type_ = self.type_

        updated_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if bio is not UNSET:
            field_dict["bio"] = bio
        if blog is not UNSET:
            field_dict["blog"] = blog
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if company is not UNSET:
            field_dict["company"] = company
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage
        if email is not UNSET:
            field_dict["email"] = email
        if events_url is not UNSET:
            field_dict["events_url"] = events_url
        if followers is not UNSET:
            field_dict["followers"] = followers
        if followers_url is not UNSET:
            field_dict["followers_url"] = followers_url
        if following is not UNSET:
            field_dict["following"] = following
        if following_url is not UNSET:
            field_dict["following_url"] = following_url
        if gists_url is not UNSET:
            field_dict["gists_url"] = gists_url
        if gravatar_id is not UNSET:
            field_dict["gravatar_id"] = gravatar_id
        if hireable is not UNSET:
            field_dict["hireable"] = hireable
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if ldap_dn is not UNSET:
            field_dict["ldap_dn"] = ldap_dn
        if location is not UNSET:
            field_dict["location"] = location
        if login is not UNSET:
            field_dict["login"] = login
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if organizations_url is not UNSET:
            field_dict["organizations_url"] = organizations_url
        if owned_private_repos is not UNSET:
            field_dict["owned_private_repos"] = owned_private_repos
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if plan is not UNSET:
            field_dict["plan"] = plan
        if private_gists is not UNSET:
            field_dict["private_gists"] = private_gists
        if public_gists is not UNSET:
            field_dict["public_gists"] = public_gists
        if public_repos is not UNSET:
            field_dict["public_repos"] = public_repos
        if received_events_url is not UNSET:
            field_dict["received_events_url"] = received_events_url
        if repos_url is not UNSET:
            field_dict["repos_url"] = repos_url
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if site_admin is not UNSET:
            field_dict["site_admin"] = site_admin
        if starred_url is not UNSET:
            field_dict["starred_url"] = starred_url
        if subscriptions_url is not UNSET:
            field_dict["subscriptions_url"] = subscriptions_url
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at
        if text_matches is not UNSET:
            field_dict["text_matches"] = text_matches
        if total_private_repos is not UNSET:
            field_dict["total_private_repos"] = total_private_repos
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if two_factor_authentication is not UNSET:
            field_dict["two_factor_authentication"] = two_factor_authentication
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_plan import GithubPlan
        from ..models.github_text_match import GithubTextMatch
        from ..models.github_timestamp import GithubTimestamp
        from ..models.github_user_permissions import GithubUserPermissions

        d = dict(src_dict)
        avatar_url = d.pop("avatar_url", UNSET)

        bio = d.pop("bio", UNSET)

        blog = d.pop("blog", UNSET)

        collaborators = d.pop("collaborators", UNSET)

        company = d.pop("company", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: GithubTimestamp | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GithubTimestamp.from_dict(_created_at)

        disk_usage = d.pop("disk_usage", UNSET)

        email = d.pop("email", UNSET)

        events_url = d.pop("events_url", UNSET)

        followers = d.pop("followers", UNSET)

        followers_url = d.pop("followers_url", UNSET)

        following = d.pop("following", UNSET)

        following_url = d.pop("following_url", UNSET)

        gists_url = d.pop("gists_url", UNSET)

        gravatar_id = d.pop("gravatar_id", UNSET)

        hireable = d.pop("hireable", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        ldap_dn = d.pop("ldap_dn", UNSET)

        location = d.pop("location", UNSET)

        login = d.pop("login", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("node_id", UNSET)

        organizations_url = d.pop("organizations_url", UNSET)

        owned_private_repos = d.pop("owned_private_repos", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: GithubUserPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = GithubUserPermissions.from_dict(_permissions)

        _plan = d.pop("plan", UNSET)
        plan: GithubPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = GithubPlan.from_dict(_plan)

        private_gists = d.pop("private_gists", UNSET)

        public_gists = d.pop("public_gists", UNSET)

        public_repos = d.pop("public_repos", UNSET)

        received_events_url = d.pop("received_events_url", UNSET)

        repos_url = d.pop("repos_url", UNSET)

        role_name = d.pop("role_name", UNSET)

        site_admin = d.pop("site_admin", UNSET)

        starred_url = d.pop("starred_url", UNSET)

        subscriptions_url = d.pop("subscriptions_url", UNSET)

        _suspended_at = d.pop("suspended_at", UNSET)
        suspended_at: GithubTimestamp | Unset
        if isinstance(_suspended_at, Unset):
            suspended_at = UNSET
        else:
            suspended_at = GithubTimestamp.from_dict(_suspended_at)

        _text_matches = d.pop("text_matches", UNSET)
        text_matches: list[GithubTextMatch] | Unset = UNSET
        if _text_matches is not UNSET:
            text_matches = []
            for text_matches_item_data in _text_matches:
                text_matches_item = GithubTextMatch.from_dict(text_matches_item_data)

                text_matches.append(text_matches_item)

        total_private_repos = d.pop("total_private_repos", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        two_factor_authentication = d.pop("two_factor_authentication", UNSET)

        type_ = d.pop("type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: GithubTimestamp | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = GithubTimestamp.from_dict(_updated_at)

        url = d.pop("url", UNSET)

        github_user = cls(
            avatar_url=avatar_url,
            bio=bio,
            blog=blog,
            collaborators=collaborators,
            company=company,
            created_at=created_at,
            disk_usage=disk_usage,
            email=email,
            events_url=events_url,
            followers=followers,
            followers_url=followers_url,
            following=following,
            following_url=following_url,
            gists_url=gists_url,
            gravatar_id=gravatar_id,
            hireable=hireable,
            html_url=html_url,
            id=id,
            ldap_dn=ldap_dn,
            location=location,
            login=login,
            name=name,
            node_id=node_id,
            organizations_url=organizations_url,
            owned_private_repos=owned_private_repos,
            permissions=permissions,
            plan=plan,
            private_gists=private_gists,
            public_gists=public_gists,
            public_repos=public_repos,
            received_events_url=received_events_url,
            repos_url=repos_url,
            role_name=role_name,
            site_admin=site_admin,
            starred_url=starred_url,
            subscriptions_url=subscriptions_url,
            suspended_at=suspended_at,
            text_matches=text_matches,
            total_private_repos=total_private_repos,
            twitter_username=twitter_username,
            two_factor_authentication=two_factor_authentication,
            type_=type_,
            updated_at=updated_at,
            url=url,
        )

        github_user.additional_properties = d
        return github_user

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
