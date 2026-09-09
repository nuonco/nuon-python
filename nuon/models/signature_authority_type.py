from enum import StrEnum


class SignatureAuthorityType(StrEnum):
    KEYLESS = "keyless"
    PUBLIC_KEY = "public_key"

    def __str__(self) -> str:
        return str(self.value)
