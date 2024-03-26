from rest_framework.serializers import ModelSerializer
from resume.models import Profile

from .contact_info import ContactInfoSerializer
from .skill import SkillSerializer
from .interest import InterestSerializer
from .project import ProjectSerializer
from .work_experience import WorkExperienceSerializer


class DetailedProfileSerializer(ModelSerializer):
    contact_info = ContactInfoSerializer(many=True)

    skills = SkillSerializer(many=True)

    interests = InterestSerializer(many=True)

    projects = ProjectSerializer(many=True)

    work_experiences = WorkExperienceSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            "full_name",
            "about_me",
            "job_title",
            "image_url",
            "birth_date",
            "employment_status",
            "contact_info",
            "skills",
            "interests",
            "projects",
            "work_experiences",
        )
