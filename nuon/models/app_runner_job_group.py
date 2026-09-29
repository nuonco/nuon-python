from enum import StrEnum


class AppRunnerJobGroup(StrEnum):
    RUNNER_JOB_GROUP_ACTIONS = "actions"
    RUNNER_JOB_GROUP_ANY = "any"
    RUNNER_JOB_GROUP_BUILD = "build"
    RUNNER_JOB_GROUP_DEPLOY = "deploy"
    RUNNER_JOB_GROUP_HEALTH_CHECKS = "health-checks"
    RUNNER_JOB_GROUP_IMAGE_ACTIONS = "image-actions"
    RUNNER_JOB_GROUP_MANAGEMENT = "management"
    RUNNER_JOB_GROUP_OPERATIONS = "operations"
    RUNNER_JOB_GROUP_RUNNER = "runner"
    RUNNER_JOB_GROUP_SANDBOX = "sandbox"
    RUNNER_JOB_GROUP_SYNC = "sync"
    RUNNER_JOB_GROUP_UNKNOWN = ""

    def __str__(self) -> str:
        return str(self.value)
