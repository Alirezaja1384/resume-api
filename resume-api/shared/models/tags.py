from typing import Iterable, cast
from django.db.models import CharField


DEFAULT_DELIMITER = ","


class TagsField(CharField):
    delimiter: str

    def __init__(self, *, delimiter=DEFAULT_DELIMITER, **kwargs):
        self.delimiter = delimiter

        kwargs.setdefault("default", list)
        super().__init__(**kwargs)

    def to_python(self, value):
        if not value:
            return []

        return value.split(self.delimiter)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def pre_save(self, model_instance, add):
        attr = cast(str | Iterable[str], super().pre_save(model_instance, add))

        if attr is None:
            return None

        if isinstance(attr, str):
            attr = attr.split(self.delimiter)

        attr = [str(t).strip() for t in attr]

        # update the value on the model instance
        setattr(model_instance, self.attname, attr)
        # return the rewritten value
        return attr

    def get_prep_value(self, value):
        if not value:
            return None if value is None else ""

        # pre_save should normalize the value
        if not isinstance(value, list):
            raise ValueError("Unexpected value type.")

        return self.delimiter.join(value)
