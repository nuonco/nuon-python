from enum import Enum


class StatePartialName(str, Enum):
    ACTIONS = "actions"
    APP = "app"
    CLOUD = "cloud"
    COMPONENTS = "components"
    DOMAIN = "domain"
    INPUTS = "inputs"
    ORG = "org"
    RUNNER = "runner"
    SANDBOX = "sandbox"
    SECRETS = "secrets"
    STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
