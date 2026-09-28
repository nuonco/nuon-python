from enum import StrEnum


class AppPolicyName(StrEnum):
    POLICY_NAME_HOSTED_INSTALLER = "hosted_installer"
    POLICY_NAME_INSTALLER = "installer"
    POLICY_NAME_ORG_ADMIN = "org_admin"
    POLICY_NAME_ORG_BUILDER = "org_builder"
    POLICY_NAME_ORG_READ_ONLY = "org_read_only"
    POLICY_NAME_ORG_SUPPORT = "org_support"
    POLICY_NAME_RUNNER = "runner"
    POLICY_NAME_STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
