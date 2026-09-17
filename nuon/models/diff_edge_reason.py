from enum import StrEnum


class DiffEdgeReason(StrEnum):
    COMPONENT_DEPENDENCY = "component_dependency"
    COMPONENT_REFERENCE = "component_reference"
    INPUT_REFERENCE = "input_reference"
    INSTALL_STACK_OUTPUT = "install_stack_output"
    OPERATION_ROLE = "operation_role"
    SANDBOX_OUTPUT = "sandbox_output"
    SECRET_REFERENCE = "secret_reference"
    STACK_RENDER = "stack_render"

    def __str__(self) -> str:
        return str(self.value)
