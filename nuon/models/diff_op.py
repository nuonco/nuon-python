from enum import StrEnum


class DiffOp(StrEnum):
    OP_ADD = "add"
    OP_CHANGE = "change"
    OP_NOOP = "noop"
    OP_REMOVE = "remove"
    OP_UNKNOWN = ""

    def __str__(self) -> str:
        return str(self.value)
