from typing import TYPE_CHECKING, cast

from django.db import models, transaction
from django_bleach.models import BleachField

from shared.models import BaseModel, max_choice_len
from .project import Project
from .work_experience import WorkExperience

if TYPE_CHECKING:
    from .contact_info import ContactInfoDict
    from .skill import SkillDict
    from .interest import InterestDict


class ProfileManager(models.Manager):
    def get_default(self):
        obj = self.filter(is_default=True).first()
        if obj is None:
            raise models.ObjectDoesNotExist("No default object")

        return obj


class EmploymentStatusChoices(models.TextChoices):
    LOOKING_FOR_JOB = "looking_for_job"
    EMPLOYED = "employed"
    FREELANCER = "freelancer"


class Profile(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    about_me = BleachField()

    job_title = models.CharField(max_length=255)

    image_url = models.URLField(null=True, blank=True)

    birth_date = models.DateField()

    employment_status = models.CharField(
        max_length=max_choice_len(EmploymentStatusChoices),
        choices=EmploymentStatusChoices,
    )

    contact_info: list["ContactInfoDict"] = cast(
        list["ContactInfoDict"], models.JSONField(default=list)
    )

    skills: list["SkillDict"] = cast(
        list["SkillDict"], models.JSONField(default=list)
    )

    interests: list["InterestDict"] = cast(
        list["InterestDict"], models.JSONField(default=list)
    )

    projects = models.ManyToManyField(Project, related_name="profiles")

    work_experiences = models.ManyToManyField(
        WorkExperience, related_name="profiles"
    )

    is_default = models.BooleanField(default=False)

    objects = ProfileManager()

    class Meta(BaseModel.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["is_default"],
                condition=models.Q(is_default=True),
                name="unique_default_profile",
            )
        ]

    def full_name(self) -> str:
        return f"{self.first_name.strip()} {self.last_name.strip()}"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ) -> None:
        with transaction.atomic():
            if self.is_default:
                self.__class__.objects.exclude(pk=self.pk).update(
                    is_default=False
                )

            super().save(force_insert, force_update, using, update_fields)
