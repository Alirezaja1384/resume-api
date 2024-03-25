from rest_framework.serializers import Serializer
from rest_framework import fields


contact_info_type_choices = [
    "cellphone",
    "email",
    "linkedin",
    "telegram",
    "github",
]


class ContactInfoSerializer(Serializer):
    type = fields.ChoiceField(contact_info_type_choices)
    value = fields.CharField(max_length=255)
