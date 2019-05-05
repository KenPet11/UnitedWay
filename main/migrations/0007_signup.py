# Generated by Django 2.1.5 on 2019-04-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190402_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_name', models.CharField(max_length=200)),
                ('volunteer_email', models.CharField(max_length=200)),
                ('volunteer_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('event_name', models.CharField(max_length=200)),
            ],
        ),
    ]