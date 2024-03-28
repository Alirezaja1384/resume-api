from rest_framework.serializers import ModelSerializer

from authentication.v1.schemas import UserSerializer
from authentication.v1.schemas.contact_info import ContactInfoSerializer
from resume.models import Profile

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
            "user",
            "about_me",
            "introduction",
            "job_title",
            "employment_status",
            "skills",
            "interests",
            "projects",
            "work_experiences",
            # <Backward compatibility>
            "full_name",
            "image_url",
            "birth_date",
            "contact_info",
            # </Backward compatibility>
        )
