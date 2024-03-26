from rest_framework.serializers import ModelSerializer, ValidationError

from resume.models import WorkExperience
from shared.schemas import TagsField
from .link import AdminLinkSerializer


class AdminWorkExperienceSerializer(ModelSerializer):
    links = AdminLinkSerializer(many=True)

    tags = TagsField()

    class Meta:
        model = WorkExperience
        fields = (
            "id",
            "company",
            "job_title",
            "description",
            "start_date",
            "end_date",
            "tags",
            "links",
        )

        read_only_fields = ("id",)

    def validate(self, attrs: dict):
        if (
            attrs.get("end_date", None)
            and attrs["start_date"] > attrs["end_date"]
        ):
            raise ValidationError(
                {"end_date": "Finish must occur after start!"}
            )

        return attrs
