from enum import StrEnum


class AppProviderType(StrEnum):
    PROVIDER_TYPE_GIT_HUB = "github"
    PROVIDER_TYPE_GOOGLE = "google"
    PROVIDER_TYPE_OIDC = "oidc"

    def __str__(self) -> str:
        return str(self.value)
