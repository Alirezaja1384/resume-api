from rest_framework import fields
from rest_framework.serializers import Serializer


class SkillSerializer(Serializer):
    name = fields.CharField(max_length=255)
    level = fields.IntegerField()
    max_level = fields.IntegerField()
