from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    Serializer,
)

from resume.models import Profile
from resume.models import Project, WorkExperience

from .contact_info import AdminContactInfoSerializer
from .skill import AdminSkillSerializer
from .interest import AdminInterestSerializer
from .project import AdminProjectSerializer
from .work_experience import AdminWorkExperienceSerializer


class AdminProfileSerializer(ModelSerializer):
    contact_info = AdminContactInfoSerializer(many=True)

    skills = AdminSkillSerializer(many=True)

    interests = AdminInterestSerializer(many=True)

    project_ids = PrimaryKeyRelatedField(
        source="projects",
        many=True,
        write_only=True,
        queryset=Project.objects.all(),
    )

    work_experience_ids = PrimaryKeyRelatedField(
        source="work_experiences",
        many=True,
        write_only=True,
        queryset=WorkExperience.objects.all(),
    )

    class Meta:
        model = Profile
        fields = (
            "id",
            "full_name",
            "about_me",
            "job_title",
            "image_url",
            "birth_date",
            "employment_status",
            "contact_info",
            "skills",
            "interests",
            "project_ids",
            "work_experience_ids",
            "is_default",
        )

        read_only_fields = ("id",)


class AdminDetailedProfileSerializer(AdminProfileSerializer):
    projects = AdminProjectSerializer(many=True, read_only=True)
    work_experiences = AdminWorkExperienceSerializer(many=True, read_only=True)

    class Meta(AdminProfileSerializer.Meta):
        fields = AdminProfileSerializer.Meta.fields + (
            "projects",
            "work_experiences",
        )


class AdminSetDefaultProfileActionBody(Serializer):
    id = PrimaryKeyRelatedField(queryset=Profile.objects.all())
