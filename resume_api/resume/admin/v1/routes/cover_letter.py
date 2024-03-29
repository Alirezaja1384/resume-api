from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions

from resume.models import CoverLetter
from resume.admin.v1 import schemas


class CoverLetterViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = schemas.AdminCoverLetterSerializer
    detailed_serializer_class = schemas.AdminDetailedCoverLetterSerializer
    queryset = CoverLetter.objects.all().select_related("user")

    def get_queryset(self):
        qs: QuerySet[CoverLetter] = (
            super().get_queryset().filter(user=self.request.user)
        )
        if self.action != "list":
            qs = qs.prefetch_related("projects", "work_experiences")

        return qs

    def get_serializer_class(self):
        if self.action == "list":
            return super().get_serializer_class()
        else:
            return self.detailed_serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
