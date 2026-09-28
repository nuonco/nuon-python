from enum import StrEnum


class AppRoleType(StrEnum):
    ROLE_TYPE_HOSTED_INSTALLER = "hosted-installer"
    ROLE_TYPE_INSTALLER = "installer"
    ROLE_TYPE_ORG_ADMIN = "org_admin"
    ROLE_TYPE_ORG_BUILDER = "org_builder"
    ROLE_TYPE_ORG_READ_ONLY = "org_read_only"
    ROLE_TYPE_ORG_SUPPORT = "org_support"
    ROLE_TYPE_RUNNER = "runner"
    ROLE_TYPE_STACK = "stack"

    def __str__(self) -> str:
        return str(self.value)
