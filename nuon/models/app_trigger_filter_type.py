from enum import StrEnum


class AppTriggerFilterType(StrEnum):
    TRIGGER_FILTER_TYPE_CONTAINS = "contains"
    TRIGGER_FILTER_TYPE_EQ = "eq"
    TRIGGER_FILTER_TYPE_EXISTS = "exists"
    TRIGGER_FILTER_TYPE_GT = "gt"
    TRIGGER_FILTER_TYPE_GTE = "gte"
    TRIGGER_FILTER_TYPE_IN = "in"
    TRIGGER_FILTER_TYPE_LT = "lt"
    TRIGGER_FILTER_TYPE_LTE = "lte"
    TRIGGER_FILTER_TYPE_NOT_EXISTS = "not_exists"
    TRIGGER_FILTER_TYPE_N_EQ = "neq"
    TRIGGER_FILTER_TYPE_PREFIX = "prefix"
    TRIGGER_FILTER_TYPE_REGEX = "regex"
    TRIGGER_FILTER_TYPE_SUFFIX = "suffix"

    def __str__(self) -> str:
        return str(self.value)
