from rest_framework import fields
from rest_framework.serializers import Serializer


class LinkSerializer(Serializer):
    title = fields.CharField(max_length=255)
    url = fields.URLField()
