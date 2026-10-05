from enum import StrEnum


class AppTokenType(StrEnum):
    TOKEN_TYPE_ADMIN = "admin"
    TOKEN_TYPE_AUTH = "auth"
    TOKEN_TYPE_AUTH_0 = "auth0"
    TOKEN_TYPE_CANARY = "canary"
    TOKEN_TYPE_FEDERATED = "federated"
    TOKEN_TYPE_INTEGRATION = "integration"
    TOKEN_TYPE_NUON = "nuon"
    TOKEN_TYPE_O_AUTH = "oauth"
    TOKEN_TYPE_STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
