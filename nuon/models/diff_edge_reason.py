from enum import StrEnum


class DiffEdgeReason(StrEnum):
    EDGE_REASON_COMPONENT_DEPENDENCY = "component_dependency"
    EDGE_REASON_COMPONENT_REFERENCE = "component_reference"
    EDGE_REASON_INPUT_REFERENCE = "input_reference"
    EDGE_REASON_INSTALL_STACK_OUTPUT = "install_stack_output"
    EDGE_REASON_OPERATION_ROLE = "operation_role"
    EDGE_REASON_SANDBOX_OUTPUT = "sandbox_output"
    EDGE_REASON_SECRET_REFERENCE = "secret_reference"
    EDGE_REASON_STACK_RENDER = "stack_render"

    def __str__(self) -> str:
        return str(self.value)
