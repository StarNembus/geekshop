# Generated by Django 3.2.8 on 2021-11-07 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211103_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 14, 26, 13, 777841, tzinfo=utc)),
        ),
    ]