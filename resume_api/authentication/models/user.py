from typing import cast

from django.contrib.auth.models import AbstractUser
from django.db.models import URLField, DateField, JSONField

from .contact_info import ContactInfoDict


class User(AbstractUser):
    profile_image = URLField(null=True)

    birth_date = DateField(null=True)

    contact_info: list["ContactInfoDict"] = cast(
        list["ContactInfoDict"], JSONField(default=list)
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name.strip()} {self.last_name.strip()}"
