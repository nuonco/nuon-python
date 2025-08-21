from enum import Enum


class AppComponentBuildStatus(str, Enum):
    ACTIVE = "active"
    BUILDING = "building"
    DELETING = "deleting"
    ERROR = "error"
    PLANNING = "planning"

    def __str__(self) -> str:
        return str(self.value)
