from enum import StrEnum


class RefsRefType(StrEnum):
    REF_TYPE_ACTIONS = "actions"
    REF_TYPE_COMPONENTS = "component"
    REF_TYPE_INPUTS = "inputs"
    REF_TYPE_INSTALL_INPUTS = "install_inputs"
    REF_TYPE_INSTALL_STACK = "install_stack"
    REF_TYPE_SANDBOX = "sandbox"
    REF_TYPE_SECRETS = "secrets"

    def __str__(self) -> str:
        return str(self.value)
