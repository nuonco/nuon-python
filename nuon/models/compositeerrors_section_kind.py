from enum import Enum


class CompositeerrorsSectionKind(str, Enum):
    CODE = "code"
    MARKDOWN = "markdown"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
