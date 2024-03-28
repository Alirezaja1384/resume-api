from rest_framework.serializers import ModelSerializer

from authentication.models import User

from .contact_info import ContactInfoSerializer


class UserSerializer(ModelSerializer):
    contact_info = ContactInfoSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "full_name",
            "birth_date",
            "profile_image",
            "contact_info",
        )
