from rest_framework.serializers import ModelSerializer

from authentication.v1.schemas import UserSerializer
from resume.models import CoverLetter
from .project import ProjectSerializer
from .work_experience import WorkExperienceSerializer


class DetailedCoverLetterSerializer(ModelSerializer):
    user = UserSerializer()

    projects = ProjectSerializer(many=True)

    work_experiences = WorkExperienceSerializer(many=True)

    class Meta:
        model = CoverLetter
        fields = (
            "user",
            "introduction",
            "text",
            "projects",
            "work_experiences",
        )
