# Generated by Django 4.1.3 on 2022-11-16 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_stadium'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stadium',
            old_name='Location',
            new_name='location',
        ),
    ]
