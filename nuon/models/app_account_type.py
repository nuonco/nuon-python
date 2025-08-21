from enum import Enum


class AppAccountType(str, Enum):
    AUTH0 = "auth0"
    CANARY = "canary"
    INTEGRATION = "integration"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
