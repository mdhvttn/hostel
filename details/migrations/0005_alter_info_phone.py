# Generated by Django 3.2.8 on 2021-10-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_alter_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]
