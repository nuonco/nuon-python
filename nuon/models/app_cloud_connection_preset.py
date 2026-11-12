from enum import StrEnum


class AppCloudConnectionPreset(StrEnum):
    CLOUD_CONNECTION_PRESET_ACR = "acr"
    CLOUD_CONNECTION_PRESET_CUSTOM = "custom"
    CLOUD_CONNECTION_PRESET_ECR = "ecr"
    CLOUD_CONNECTION_PRESET_GAR = "gar"
    CLOUD_CONNECTION_PRESET_STACKS = "stacks"

    def __str__(self) -> str:
        return str(self.value)
