# Generated by Django 3.1.7 on 2021-04-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0020_auto_20210426_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgfeed',
            name='start_datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]