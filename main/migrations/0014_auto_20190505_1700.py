# Generated by Django 2.1.5 on 2019-05-05 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190505_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='e_contact_email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact Email'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='e_contact_phone',
            field=models.CharField(blank=True, max_length=17, verbose_name='Contact Phone'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='e_coordinator',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cordinator'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='e_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Event Link'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='e_location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='e_organization',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Organization'),
        ),
    ]