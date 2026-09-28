from enum import StrEnum


class AppPolicyReportOwnerType(StrEnum):
    POLICY_REPORT_OWNER_TYPE_COMPONENT_BUILD = "component_builds"
    POLICY_REPORT_OWNER_TYPE_INSTALL_DEPLOY = "install_deploys"
    POLICY_REPORT_OWNER_TYPE_INSTALL_SANDBOX_RUN = "install_sandbox_runs"

    def __str__(self) -> str:
        return str(self.value)
