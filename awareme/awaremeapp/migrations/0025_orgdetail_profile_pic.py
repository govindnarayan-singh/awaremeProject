# Generated by Django 3.1.7 on 2021-05-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0024_orgdetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgdetail',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
