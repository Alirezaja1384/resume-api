from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from resume.models import Project
from resume.admin.v1 import schemas


class ProjectModelViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = schemas.AdminProjectSerializer
    queryset = Project.objects.all()