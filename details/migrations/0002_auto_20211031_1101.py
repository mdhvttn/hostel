# Generated by Django 3.2.8 on 2021-10-31 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
