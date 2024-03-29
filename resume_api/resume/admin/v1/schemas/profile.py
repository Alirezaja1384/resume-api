from rest_framework.serializers import ModelSerializer

from authentication.v1.schemas import UserSerializer, ContactInfoSerializer
from resume.models import Profile
from resume.models import Project, WorkExperience
from shared.schemas import OwnedPrimaryKeyRelatedField

from .skill import AdminSkillSerializer
from .interest import AdminInterestSerializer
from .project import AdminProjectSerializer
from .work_experience import AdminWorkExperienceSerializer


class AdminProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    contact_info = ContactInfoSerializer(
        many=True, read_only=True
    )  # Backward compatibility

    skills = AdminSkillSerializer(many=True)

    interests = AdminInterestSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "introduction",
            "about_me",
            "job_title",
            "employment_status",
            "skills",
            "interests",
            "is_default",
            # <Backward compatibility>
            "full_name",
            "image_url",
            "birth_date",
            "contact_info",
            # </Backward compatibility>
        )

        read_only_fields = ("id",)


class AdminDetailedProfileSerializer(AdminProfileSerializer):
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

    class Meta(AdminProfileSerializer.Meta):
        fields = AdminProfileSerializer.Meta.fields + (
            "projects",
            "work_experiences",
            "project_ids",
            "work_experience_ids",
        )
