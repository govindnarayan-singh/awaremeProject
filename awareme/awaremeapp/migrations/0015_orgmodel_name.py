# Generated by Django 3.1.7 on 2021-04-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0014_remove_orgmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgmodel',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
