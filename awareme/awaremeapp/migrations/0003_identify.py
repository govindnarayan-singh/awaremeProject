# Generated by Django 3.1.7 on 2021-04-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('awaremeapp', '0002_delete_orgmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.IntegerField(blank=True, max_length=11, null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
            ],
        ),
    ]