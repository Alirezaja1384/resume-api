from uuid import uuid4
from django.db.models import Model, UUIDField, DateTimeField


class BaseModel(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("created_at",)
