from rest_framework.routers import SimpleRouter
from .profile import ProfileRetrieveAPIView
from .cover_letter import CoverLetterViewSet

router = SimpleRouter()
router.register("cover-letter", CoverLetterViewSet, "cover-letter")

__all__ = ["ProfileRetrieveAPIView", "router"]
