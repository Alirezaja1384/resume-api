from rest_framework.serializers import Serializer
from rest_framework import fields

from resume.models.contact_info import ContactInfoType

contact_info_type_choices: list[ContactInfoType] = [
    "cellphone",
    "email",
    "linkedin",
    "telegram",
    "github",
]


class AdminContactInfoSerializer(Serializer):
    type = fields.ChoiceField(contact_info_type_choices)
    value = fields.CharField(max_length=255)
