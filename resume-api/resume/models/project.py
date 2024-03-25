from typing import TYPE_CHECKING, cast
from django.db import models
from django_bleach.models import BleachField

from shared.models import BaseModel, TagsField

if TYPE_CHECKING:
    from .link import LinkDict


class Project(BaseModel):
    name = models.CharField(max_length=255)
    description = BleachField()

    tags = TagsField()

    links = cast(list["LinkDict"], models.JSONField(default=list))
