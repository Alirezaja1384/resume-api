from datetime import date

from rest_framework.fields import URLField, CharField, DateField
from rest_framework.serializers import ModelSerializer

from authentication.v1.schemas import UserSerializer
from resume.models import Profile

from .contact_info import ContactInfoSerializer
from .skill import SkillSerializer
from .interest import InterestSerializer
from .project import ProjectSerializer
from .work_experience import WorkExperienceSerializer


class DetailedProfileSerializer(ModelSerializer):
    user = UserSerializer()

    contact_info = ContactInfoSerializer(many=True)

    skills = SkillSerializer(many=True)

    interests = InterestSerializer(many=True)

    projects = ProjectSerializer(many=True)

    work_experiences = WorkExperienceSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            # <Backward compatibility>
            "full_name",
            "image_url",
            "birth_date",
            # </Backward compatibility>
            "user",
            "about_me",
            "introduction",
            "job_title",
            "employment_status",
            "contact_info",
            "skills",
            "interests",
            "projects",
            "work_experiences",
        )
