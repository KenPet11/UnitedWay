# Generated by Django 2.1.5 on 2019-02-17 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.AddField(
            model_name='event',
            name='event_day',
            field=models.DateField(default=datetime.date.today, help_text='Day of the event', verbose_name='Day of the event'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(default=datetime.time, verbose_name='ending time'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_time',
            field=models.TimeField(default=datetime.time, verbose_name='starting time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(blank=True, help_text='Notes', null=True, verbose_name='Notes'),
        ),
    ]
