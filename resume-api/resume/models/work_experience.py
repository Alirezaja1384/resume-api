from typing import TYPE_CHECKING, cast
from django.db import models
from django_bleach.models import BleachField

from shared.models import BaseModel, TagsField

if TYPE_CHECKING:
    from .link import LinkDict


class WorkExperience(BaseModel):
    company = models.CharField(max_length=255)

    job_title = models.CharField(max_length=255)

    description = BleachField()

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    tags = TagsField()

    links = cast(list["LinkDict"], models.JSONField(default=list))