from django.db import models
from django_bleach.models import BleachField

from shared.models import BaseModel
from .project import Project
from .work_experience import WorkExperience


class CoverLetter(BaseModel):
    introduction = models.CharField(max_length=255, null=True)

    text = BleachField()

    user = models.ForeignKey(
        "authentication.User",
        on_delete=models.CASCADE,
        related_name="cover_letters",
    )

    projects = models.ManyToManyField(Project, related_name="cover_letters")

    work_experiences = models.ManyToManyField(
        WorkExperience, related_name="cover_letters"
    )
