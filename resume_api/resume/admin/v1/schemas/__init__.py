from .profile import AdminProfileSerializer, AdminDetailedProfileSerializer
from .cover_letter import AdminCoverLetterSerializer, AdminDetailedCoverLetterSerializer
from .project import AdminProjectSerializer
from .work_experience import AdminWorkExperienceSerializer

__all__ = [
    "AdminProfileSerializer",
    "AdminDetailedProfileSerializer",
    "AdminProjectSerializer",
    "AdminWorkExperienceSerializer",
]
