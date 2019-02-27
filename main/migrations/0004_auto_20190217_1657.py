# Generated by Django 2.1.5 on 2019-02-17 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190217_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_day',
            field=models.DateField(default=datetime.date.today, help_text='Day of the event', verbose_name='Day of the event'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.TextField(blank=True, default='Notes', help_text='Notes', null=True, verbose_name='Notes'),
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
    ]
