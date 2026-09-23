from enum import StrEnum


class AppTriggerFilterType(StrEnum):
    CONTAINS = "contains"
    EQ = "eq"
    EXISTS = "exists"
    GT = "gt"
    GTE = "gte"
    IN = "in"
    LT = "lt"
    LTE = "lte"
    NEQ = "neq"
    NOT_EXISTS = "not_exists"
    PREFIX = "prefix"
    REGEX = "regex"
    SUFFIX = "suffix"

    def __str__(self) -> str:
        return str(self.value)
