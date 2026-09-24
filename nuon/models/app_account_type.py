from enum import StrEnum


class AppAccountType(StrEnum):
    ACCOUNT_TYPE_AUTH = "auth"
    ACCOUNT_TYPE_AUTH_0 = "auth0"
    ACCOUNT_TYPE_CANARY = "canary"
    ACCOUNT_TYPE_INTEGRATION = "integration"
    ACCOUNT_TYPE_SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
