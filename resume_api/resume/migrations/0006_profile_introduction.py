# Generated by Django 5.0.3 on 2024-03-26 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_default_ordering_ascending'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='introduction',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
