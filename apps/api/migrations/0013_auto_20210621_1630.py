# Generated by Django 2.2.24 on 2021-06-21 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210621_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 21, 16, 30, 30, 805279, tzinfo=utc)),
        ),
    ]
