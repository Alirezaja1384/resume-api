from rest_framework.serializers import ModelSerializer

from authentication.v1.schemas import UserSerializer
from resume.models import CoverLetter, Project, WorkExperience
from shared.schemas import OwnedPrimaryKeyRelatedField
from .project import AdminProjectSerializer
from .work_experience import AdminWorkExperienceSerializer


class AdminCoverLetterSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CoverLetter
        fields = ("user", "introduction", "text")


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
