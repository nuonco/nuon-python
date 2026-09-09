from enum import StrEnum


class AppAccountType(StrEnum):
    AUTH = "auth"
    AUTH0 = "auth0"
    CANARY = "canary"
    INTEGRATION = "integration"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
