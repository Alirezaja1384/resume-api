from rest_framework.serializers import ListSerializer, ValidationError
from rest_framework.fields import CharField


def tag_validator(delim=","):
    def validate(value):
        if delim in value:
            raise ValidationError(f'"{delim}" is not allowed in tags')

    return validate


def _tags_field(delimiter=",", default=list, **kwargs):
    kwargs["validators"] = [
        tag_validator(delim=delimiter),
        *kwargs.get("validators", []),
    ]

    return ListSerializer(child=CharField(**kwargs), default=default)


TagsField = _tags_field
