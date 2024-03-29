from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.reverse import reverse

from authentication.v1.schemas import UserSerializer
from resume.models import CoverLetter, Project, WorkExperience
from shared.schemas import OwnedPrimaryKeyRelatedField
from .project import AdminProjectSerializer
from .work_experience import AdminWorkExperienceSerializer


class AdminCoverLetterSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    public_url = SerializerMethodField(method_name="get_public_url")

    class Meta:
        model = CoverLetter
        fields = ("id", "user", "introduction", "text", "public_url")

    def get_public_url(self, obj) -> str:
        return reverse(
            "v1:resume:cover-letter-detail",
            request=self.context["request"],
            args=[obj.id],
        )


class AdminDetailedCoverLetterSerializer(AdminCoverLetterSerializer):
    projects = AdminProjectSerializer(many=True, read_only=True)
    work_experiences = AdminWorkExperienceSerializer(many=True, read_only=True)

    project_ids = OwnedPrimaryKeyRelatedField(
        source="projects",
        many=True,
        write_only=True,
        queryset=Project.objects.all(),
        owner_field="user",
    )

    work_experience_ids = OwnedPrimaryKeyRelatedField(
        source="work_experiences",
        many=True,
        write_only=True,
        queryset=WorkExperience.objects.all(),
        owner_field="user",
    )

    class Meta(AdminCoverLetterSerializer.Meta):
        fields = AdminCoverLetterSerializer.Meta.fields + (
            "user",
            "projects",
            "work_experiences",
            "project_ids",
            "work_experience_ids",
        )
