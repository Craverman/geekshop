# Generated by Django 3.2.10 on 2022-02-09 15:30

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0005_create_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 11, 15, 30, 30, 10029, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]
