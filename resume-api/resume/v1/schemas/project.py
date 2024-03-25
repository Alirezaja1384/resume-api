from rest_framework.serializers import ModelSerializer

from resume.models import Project
from shared.schemas import TagsField
from .link import LinkSerializer


class ProjectSerializer(ModelSerializer):
    links = LinkSerializer(many=True)

    tags = TagsField()

    class Meta:
        model = Project
        fields = ("name", "description", "tags", "links")
