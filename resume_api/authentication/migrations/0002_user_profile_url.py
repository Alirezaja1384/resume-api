# Generated by Django 5.0.3 on 2024-03-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_url',
            field=models.URLField(null=True),
        ),
    ]
