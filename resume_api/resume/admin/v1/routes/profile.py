from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions

from resume.models import Profile
from resume.admin.v1 import schemas


class ProfileModelViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = schemas.AdminProfileSerializer
    detailed_serializer_class = schemas.AdminDetailedProfileSerializer
    queryset = Profile.objects.all().select_related("user")

    def get_queryset(self):
        qs: QuerySet[Profile] = super().get_queryset().filter(user=self.request.user)
        if self.action == "retrieve":
            qs = qs.prefetch_related("projects", "work_experiences")

        return qs

    def get_serializer_class(self):
        if self.action == "list":
            return super().get_serializer_class()
        else:
            return self.detailed_serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance: Profile):
        if instance.is_default:
            raise PermissionDenied("Cannot delete default profile")

        return super().perform_destroy(instance)
