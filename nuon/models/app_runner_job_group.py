from enum import Enum


class AppRunnerJobGroup(str, Enum):
    ACTIONS = "actions"
    ANY = "any"
    BUILD = "build"
    DEPLOY = "deploy"
    HEALTH_CHECKS = "health-checks"
    MANAGEMENT = "management"
    OPERATIONS = "operations"
    RUNNER = "runner"
    SANDBOX = "sandbox"
    SYNC = "sync"
    VALUE_9 = ""

    def __str__(self) -> str:
        return str(self.value)
