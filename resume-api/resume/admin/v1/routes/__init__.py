from rest_framework.routers import SimpleRouter
from .profile import ProfileModelViewSet
from .project import ProjectModelViewSet
from .work_experience import WorkExperienceModelViewSet


router = SimpleRouter()
router.register("profile", ProfileModelViewSet, basename="profile")
router.register("project", ProjectModelViewSet, basename="project")
router.register(
    "work-experience", WorkExperienceModelViewSet, basename="work-experience"
)
