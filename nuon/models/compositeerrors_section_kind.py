from enum import StrEnum


class CompositeerrorsSectionKind(StrEnum):
    CODE = "code"
    MARKDOWN = "markdown"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
