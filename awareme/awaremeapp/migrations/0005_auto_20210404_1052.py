# Generated by Django 3.1.7 on 2021-04-04 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0004_auto_20210404_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgmodel',
            old_name='Contactnumber',
            new_name='Contact',
        ),
    ]