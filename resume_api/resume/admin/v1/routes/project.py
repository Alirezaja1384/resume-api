from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from resume.models import Project
from resume.admin.v1 import schemas


class ProjectViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = schemas.AdminProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
