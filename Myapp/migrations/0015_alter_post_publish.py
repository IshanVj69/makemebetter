# Generated by Django 4.0.5 on 2022-07-16 02:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0014_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 16, 2, 25, 49, 390897, tzinfo=utc)),
        ),
    ]
