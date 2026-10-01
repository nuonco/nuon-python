from enum import StrEnum


class StatePartialName(StrEnum):
    PARTIAL_ACTIONS = "actions"
    PARTIAL_APP = "app"
    PARTIAL_CLOUD = "cloud"
    PARTIAL_COMPONENTS = "components"
    PARTIAL_DOMAIN = "domain"
    PARTIAL_INPUTS = "inputs"
    PARTIAL_ORG = "org"
    PARTIAL_RUNNER = "runner"
    PARTIAL_SANDBOX = "sandbox"
    PARTIAL_SECRETS = "secrets"
    PARTIAL_STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
