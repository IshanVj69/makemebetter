# Generated by Django 4.0.5 on 2022-08-13 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0010_bcd_abc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bcd',
            name='posti',
        ),
        migrations.RemoveField(
            model_name='bcd',
            name='user',
        ),
        migrations.DeleteModel(
            name='abc',
        ),
        migrations.DeleteModel(
            name='bcd',
        ),
    ]