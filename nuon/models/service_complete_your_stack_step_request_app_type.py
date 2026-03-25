from enum import Enum


class ServiceCompleteYourStackStepRequestAppType(str, Enum):
    CUSTOM = "custom"
    EXAMPLE = "example"

    def __str__(self) -> str:
        return str(self.value)
