# Generated by Django 3.1.7 on 2021-04-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0003_identify'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('aim', models.TextField(blank=True, null=True)),
                ('Contactnumber', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Identify',
        ),
    ]
