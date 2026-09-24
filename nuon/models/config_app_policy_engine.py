from enum import StrEnum


class ConfigAppPolicyEngine(StrEnum):
    APP_POLICY_ENGINE_KYVERNO = "kyverno"
    APP_POLICY_ENGINE_OPA = "opa"

    def __str__(self) -> str:
        return str(self.value)
