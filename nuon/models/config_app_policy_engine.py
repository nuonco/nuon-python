from enum import Enum


class ConfigAppPolicyEngine(str, Enum):
    KYVERNO = "kyverno"
    OPA = "opa"

    def __str__(self) -> str:
        return str(self.value)
