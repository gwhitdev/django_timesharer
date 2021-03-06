# Generated by Django 3.2.3 on 2021-05-31 19:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timesharer', '0007_auto_20210527_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 19, 37, 31, 434098, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='opted_in',
            field=models.BooleanField(default=False),
        ),
    ]
