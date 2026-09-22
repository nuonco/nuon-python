from enum import StrEnum


class DiffOp(StrEnum):
    ADD = "add"
    CHANGE = "change"
    NOOP = "noop"
    REMOVE = "remove"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
