# Generated by Django 2.2.24 on 2021-12-19 17:47

import datetime
<lesson_15

master
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
lesson_15
        ("authnapp", "0006_auto_20211212_1306"),

        ('authnapp', '0006_auto_20211212_1306'),
 master
    ]

    operations = [
        migrations.AlterField(
lesson_15
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 21, 17, 47, 48, 183245, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 17, 47, 48, 183245, tzinfo=utc), verbose_name='актуальность ключа'),
master
        ),
    ]
