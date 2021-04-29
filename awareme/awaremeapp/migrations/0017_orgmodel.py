# Generated by Django 3.1.7 on 2021-04-05 07:12

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('awaremeapp', '0016_delete_orgmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('Contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('portfolio', models.URLField(blank=True, null=True)),
            ],
        ),
    ]