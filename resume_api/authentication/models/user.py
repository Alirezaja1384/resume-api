from django.contrib.auth.models import AbstractUser
from django.db.models import URLField, DateField


class User(AbstractUser):
    profile_image = URLField(null=True)

    birth_date = DateField(null=True)

    @property
    def full_name(self) -> str:
        return f"{self.first_name.strip()} {self.last_name.strip()}"
