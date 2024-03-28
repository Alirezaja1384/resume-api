from rest_framework.serializers import Serializer
from rest_framework import fields

from authentication.models import ContactInfoType

contact_info_type_choices: list[ContactInfoType] = [
    "cellphone",
    "email",
    "linkedin",
    "telegram",
    "github",
]


class ContactInfoSerializer(Serializer):
    type = fields.ChoiceField(contact_info_type_choices)
    value = fields.CharField(max_length=255)
