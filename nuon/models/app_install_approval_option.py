from enum import StrEnum


class AppInstallApprovalOption(StrEnum):
    INSTALL_APPROVAL_OPTION_APPROVE_ALL = "approve-all"
    INSTALL_APPROVAL_OPTION_PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
