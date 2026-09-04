from enum import StrEnum


class ServiceCompleteYourStackStepRequestAppType(StrEnum):
    CUSTOM = "custom"
    EXAMPLE = "example"

    def __str__(self) -> str:
        return str(self.value)
