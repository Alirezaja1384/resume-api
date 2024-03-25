from rest_framework.serializers import ModelSerializer

from resume.models import WorkExperience
from shared.schemas import TagsField
from .link import LinkSerializer


class WorkExperienceSerializer(ModelSerializer):
    links = LinkSerializer(many=True)

    tags = TagsField()

    class Meta:
        model = WorkExperience
        fields = (
            "company",
            "job_title",
            "description",
            "start_date",
            "end_date",
            "tags",
            "links",
        )
