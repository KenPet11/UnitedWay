# Generated by Django 2.1.5 on 2019-04-29 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_signup_add_to_cal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='add_to_cal',
        ),
    ]
