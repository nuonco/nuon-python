from enum import Enum


class AppPolicyName(str, Enum):
    HOSTED_INSTALLER = "hosted_installer"
    INSTALLER = "installer"
    ORG_ADMIN = "org_admin"
    ORG_SUPPORT = "org_support"
    RUNNER = "runner"

    def __str__(self) -> str:
        return str(self.value)
