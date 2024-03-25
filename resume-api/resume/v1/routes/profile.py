from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from resume.v1 import schemas
from resume.models import Profile


class ProfileRetrieveAPIView(RetrieveAPIView):
    model = Profile
    serializer_class = schemas.DetailedProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        try:
            return self.model.objects.get_default()
        except ObjectDoesNotExist as exc:
            raise NotFound(*exc.args) from exc
