# Generated by Django 3.2.3 on 2021-05-31 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timesharer', '0009_alter_organisation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]