from enum import StrEnum


class AppRoleType(StrEnum):
    ROLE_TYPE_HOSTED_INSTALLER = "hosted-installer"
    ROLE_TYPE_INSTALLER = "installer"
    ROLE_TYPE_ORG_ADMIN = "org_admin"
    ROLE_TYPE_ORG_BUILDER = "org_builder"
    ROLE_TYPE_ORG_READ_ONLY = "org_read_only"
    ROLE_TYPE_ORG_SUPPORT = "org_support"
    ROLE_TYPE_PHONE_HOME = "phone_home"
    ROLE_TYPE_RUNNER = "runner"
    ROLE_TYPE_RUNNER_INSTALL = "runner_install"
    ROLE_TYPE_RUNNER_JOB = "runner_job"
    ROLE_TYPE_STACK = "stack"
    ROLE_TYPE_TELEMETRY_COLLECTOR = "telemetry_collector"

    def __str__(self) -> str:
        return str(self.value)
