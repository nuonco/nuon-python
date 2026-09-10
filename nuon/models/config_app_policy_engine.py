from enum import StrEnum


class ConfigAppPolicyEngine(StrEnum):
    KYVERNO = "kyverno"
    OPA = "opa"

    def __str__(self) -> str:
        return str(self.value)
