from enum import Enum


class AppStackType(str, Enum):
    AWS_CLOUDFORMATION = "aws-cloudformation"

    def __str__(self) -> str:
        return str(self.value)
