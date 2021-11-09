# Generated by Django 3.2.8 on 2021-10-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(unique=True)),
                ('payment', models.BooleanField(default=False)),
                ('year', models.ManyToManyField(to='details.Year')),
            ],
        ),
    ]
