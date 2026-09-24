from enum import StrEnum


class CompositeerrorsSectionKind(StrEnum):
    SECTION_CODE = "code"
    SECTION_MARKDOWN = "markdown"
    SECTION_TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
