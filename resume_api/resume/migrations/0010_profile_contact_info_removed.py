# Generated by Django 5.0.3 on 2024-03-28 18:49
from typing import Type

from django.contrib.auth.models import AbstractUser
from django.db import migrations
from django.db.models import Model, OuterRef, Subquery, Value
from django.db.models.functions import Coalesce


def set_user_contact_info(apps, schema_editor):
    User: Type[AbstractUser] = apps.get_model("authentication", "User")
    Profile: Type[Model] = apps.get_model("resume", "Profile")

    User.objects.filter(contact_info=[]).update(
        contact_info=Coalesce(
            Subquery(
                Profile.objects.filter(user_id=OuterRef("id"))
                .exclude(contact_info=[])
                .values("contact_info")[:1]
            ),
            Value("[]"),
        )
    )


def set_profile_contact_info(apps, schema_editor):
    User: Type[AbstractUser] = apps.get_model("authentication", "User")
    Profile: Type[Model] = apps.get_model("resume", "Profile")

    Profile.objects.update(
        contact_info=Subquery(
            User.objects.filter(pk=OuterRef("user_id")).values("contact_info")[
                :1
            ]
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0009_profile_birth_date_removed"),
        ("authentication", "0006_user_contact_info"),
    ]

    operations = [
        migrations.RunPython(set_user_contact_info, set_profile_contact_info),
        migrations.RemoveField(
            model_name="profile",
            name="contact_info",
        ),
    ]