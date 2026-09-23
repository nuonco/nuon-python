from enum import StrEnum


class AppStackDeploymentScope(StrEnum):
    RESOURCE_GROUP = "resource_group"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
