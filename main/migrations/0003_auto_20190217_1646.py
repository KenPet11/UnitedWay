# Generated by Django 2.1.5 on 2019-02-17 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190217_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_day',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_start_time',
        ),
    ]
