from enum import Enum


class AppStackDeploymentScope(str, Enum):
    RESOURCE_GROUP = "resource_group"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
