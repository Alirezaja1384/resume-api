from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from resume.models import CoverLetter
from resume.v1.schemas import DetailedCoverLetterSerializer


class CoverLetterViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = DetailedCoverLetterSerializer
    queryset = (
        CoverLetter.objects.all()
        .select_related("user")
        .prefetch_related("projects", "work_experiences")
    )
