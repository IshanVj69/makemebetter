# Generated by Django 4.0.5 on 2022-07-09 06:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 9, 6, 6, 28, 541561, tzinfo=utc)),
        ),
    ]