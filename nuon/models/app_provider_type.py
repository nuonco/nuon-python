from enum import Enum


class AppProviderType(str, Enum):
    GITHUB = "github"
    GOOGLE = "google"
    OIDC = "oidc"

    def __str__(self) -> str:
        return str(self.value)
