from enum import Enum


class AppPolicyReportOwnerType(str, Enum):
    COMPONENT_BUILDS = "component_builds"
    INSTALL_DEPLOYS = "install_deploys"
    INSTALL_SANDBOX_RUNS = "install_sandbox_runs"

    def __str__(self) -> str:
        return str(self.value)
