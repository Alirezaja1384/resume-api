from rest_framework.serializers import ModelSerializer

from authentication.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "full_name",
            "birth_date",
            "profile_image",
        )
