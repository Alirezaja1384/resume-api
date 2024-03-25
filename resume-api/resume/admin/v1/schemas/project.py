from rest_framework.serializers import ModelSerializer

from resume.models import Project
from shared.schemas import TagsField
from .link import AdminLinkSerializer


class AdminProjectSerializer(ModelSerializer):
    links = AdminLinkSerializer(many=True)

    tags = TagsField()

    class Meta:
        model = Project
        fields = ("id", "name", "description", "tags", "links")
        read_only_fields = ("id",)
