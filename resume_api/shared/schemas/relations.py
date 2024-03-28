from rest_framework.serializers import PrimaryKeyRelatedField


class OwnedPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    owner_field: str

    def __init__(self, **kwargs):
        self.owner_field = kwargs.pop("owner_field", "user")
        super().__init__(**kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(**{self.owner_field: self.context.get("request").user})
