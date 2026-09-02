from enum import StrEnum


class AppProviderType(StrEnum):
    GITHUB = "github"
    GOOGLE = "google"
    OIDC = "oidc"

    def __str__(self) -> str:
        return str(self.value)
