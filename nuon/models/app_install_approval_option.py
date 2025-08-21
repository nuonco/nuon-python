from enum import Enum


class AppInstallApprovalOption(str, Enum):
    APPROVE_ALL = "approve-all"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
