from rest_framework.serializers import ModelSerializer, Serializer

from authentication.v1.schemas import UserSerializer
from resume.models import Profile
from resume.models import Project, WorkExperience
from shared.schemas import OwnedPrimaryKeyRelatedField

from .contact_info import AdminContactInfoSerializer
from .skill import AdminSkillSerializer
from .interest import AdminInterestSerializer
from .project import AdminProjectSerializer
from .work_experience import AdminWorkExperienceSerializer


class AdminProfileSerializer(ModelSerializer):
    user = UserSerializer()

    contact_info = AdminContactInfoSerializer(many=True)

    skills = AdminSkillSerializer(many=True)

    interests = AdminInterestSerializer(many=True)

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

    class Meta:
        model = Profile
        fields = (
            "id",
            # <Backward compatibility>
            "full_name",
            "image_url",
            "birth_date",
            # </Backward compatibility>
            "user",
            "introduction",
            "about_me",
            "job_title",
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
