from enum import StrEnum


class AppInstallApprovalOption(StrEnum):
    APPROVE_ALL = "approve-all"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
