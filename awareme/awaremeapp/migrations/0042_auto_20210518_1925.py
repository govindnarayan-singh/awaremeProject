# Generated by Django 3.1.7 on 2021-05-18 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awaremeapp', '0041_donation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='ngo',
        ),
        migrations.AddField(
            model_name='donation',
            name='ngo',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]