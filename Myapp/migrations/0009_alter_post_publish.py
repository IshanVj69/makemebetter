# Generated by Django 4.0.5 on 2022-07-11 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 11, 10, 54, 20, 170525, tzinfo=utc)),
        ),
    ]