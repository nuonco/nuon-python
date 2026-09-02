from enum import StrEnum


class RefsRefType(StrEnum):
    ACTIONS = "actions"
    COMPONENT = "component"
    INPUTS = "inputs"
    INSTALL_INPUTS = "install_inputs"
    INSTALL_STACK = "install_stack"
    SANDBOX = "sandbox"
    SECRETS = "secrets"

    def __str__(self) -> str:
        return str(self.value)
