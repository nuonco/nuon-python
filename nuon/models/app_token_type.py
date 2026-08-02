from enum import Enum


class AppTokenType(str, Enum):
    ADMIN = "admin"
    AUTH = "auth"
    AUTH0 = "auth0"
    CANARY = "canary"
    FEDERATED = "federated"
    INTEGRATION = "integration"
    NUON = "nuon"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
