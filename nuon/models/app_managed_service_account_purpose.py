from enum import StrEnum


class AppManagedServiceAccountPurpose(StrEnum):
    MANAGED_SERVICE_ACCOUNT_PURPOSE_PHONE_HOME = "phone_home"
    MANAGED_SERVICE_ACCOUNT_PURPOSE_STACK = "stack"
    MANAGED_SERVICE_ACCOUNT_PURPOSE_TELEMETRY_COLLECTOR = "telemetry_collector"

    def __str__(self) -> str:
        return str(self.value)
