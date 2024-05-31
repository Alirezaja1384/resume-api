from django.db import models


class ProfileWorkExperience(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    work_experience = models.ForeignKey(
        "WorkExperience", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("profile", "work_experience")
        ordering = ("pk",)
