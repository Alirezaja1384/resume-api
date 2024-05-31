from django.db import models


class ProfileProject(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("profile", "project")
        ordering = ("pk",)
