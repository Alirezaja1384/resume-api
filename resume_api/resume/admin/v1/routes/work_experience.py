from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from resume.models import WorkExperience
from resume.admin.v1 import schemas


class WorkExperienceModelViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = schemas.AdminWorkExperienceSerializer
    queryset = WorkExperience.objects.all()
