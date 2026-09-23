from enum import StrEnum


class AppTokenType(StrEnum):
    ADMIN = "admin"
    AUTH = "auth"
    AUTH0 = "auth0"
    CANARY = "canary"
    FEDERATED = "federated"
    INTEGRATION = "integration"
    NUON = "nuon"
    OAUTH = "oauth"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
