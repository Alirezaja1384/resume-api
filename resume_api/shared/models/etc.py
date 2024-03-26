from typing import Type, cast
from django.db import models


def max_choice_len(cls: Type[models.TextChoices]) -> int:
    return max(map(len, cast(list[str], cls.values)))
