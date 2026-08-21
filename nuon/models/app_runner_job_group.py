from enum import Enum


class AppRunnerJobGroup(str, Enum):
    ACTIONS = "actions"
    ANY = "any"
    BUILD = "build"
    DEPLOY = "deploy"
    HEALTH_CHECKS = "health-checks"
    IMAGE_ACTIONS = "image-actions"
    MANAGEMENT = "management"
    OPERATIONS = "operations"
    RUNNER = "runner"
    SANDBOX = "sandbox"
    SYNC = "sync"
    VALUE_10 = ""

    def __str__(self) -> str:
        return str(self.value)
