# Generated by Django 4.1.3 on 2022-12-12 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0017_alter_season_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]