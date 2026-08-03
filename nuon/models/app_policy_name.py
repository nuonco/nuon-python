from enum import Enum


class AppPolicyName(str, Enum):
    HOSTED_INSTALLER = "hosted_installer"
    INSTALLER = "installer"
    ORG_ADMIN = "org_admin"
    ORG_BUILDER = "org_builder"
    ORG_READ_ONLY = "org_read_only"
    ORG_SUPPORT = "org_support"
    RUNNER = "runner"

    def __str__(self) -> str:
        return str(self.value)
