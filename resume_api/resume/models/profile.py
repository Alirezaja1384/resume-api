from datetime import date
from typing import TYPE_CHECKING, cast

from django.db import models, transaction
from django.contrib.auth import get_user_model
from django_bleach.models import BleachField

from shared.models import BaseModel, max_choice_len

from .project import Project
from .work_experience import WorkExperience

if TYPE_CHECKING:
    from .skill import SkillDict
    from .interest import InterestDict
    from authentication.models.contact_info import ContactInfoDict

UserModel = get_user_model()


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
    introduction = models.CharField(max_length=255, null=True)

    about_me = BleachField()

    job_title = models.CharField(max_length=255)

    employment_status = models.CharField(
        max_length=max_choice_len(EmploymentStatusChoices),
        choices=EmploymentStatusChoices,
    )

    skills: list["SkillDict"] = cast(list["SkillDict"], models.JSONField(default=list))

    interests: list["InterestDict"] = cast(
        list["InterestDict"], models.JSONField(default=list)
    )

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="Profiles"
    )

    projects = models.ManyToManyField(Project, related_name="profiles")

    work_experiences = models.ManyToManyField(WorkExperience, related_name="profiles")

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

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ) -> None:
        with transaction.atomic():
            if self.is_default:
                self.__class__.objects.exclude(pk=self.pk).update(is_default=False)

            super().save(force_insert, force_update, using, update_fields)

    # <Backward compatibility>
    @property
    def full_name(self) -> str:
        return self.user.full_name

    @property
    def image_url(self) -> str | None:
        return self.user.profile_image

    @property
    def birth_date(self) -> date:
        return self.user.birth_date or date(year=2000, month=1, day=1)

    @property
    def contact_info(self) -> "ContactInfoDict":
        return self.user.contact_info

    # </Backward compatibility>
