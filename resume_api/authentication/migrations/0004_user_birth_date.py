# Generated by Django 5.0.3 on 2024-03-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_user_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birth_date",
            field=models.DateTimeField(null=True),
        ),
    ]
