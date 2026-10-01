from enum import StrEnum


class SignatureAuthorityType(StrEnum):
    AUTHORITY_TYPE_KEYLESS = "keyless"
    AUTHORITY_TYPE_PUBLIC_KEY = "public_key"

    def __str__(self) -> str:
        return str(self.value)
