from rest_framework.routers import SimpleRouter
from .profile import ProfileViewSet
from .cover_letter import CoverLetterViewSet
from .project import ProjectViewSet
from .work_experience import WorkExperienceViewSet


router = SimpleRouter()
router.register("profile", ProfileViewSet, basename="profile")
router.register("cover-letter", CoverLetterViewSet, basename="cover-letter")
router.register("project", ProjectViewSet, basename="project")
router.register(
    "work-experience",
    WorkExperienceViewSet,
    basename="work-experience",
)
