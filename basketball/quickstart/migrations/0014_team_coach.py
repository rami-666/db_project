# Generated by Django 4.1.3 on 2022-11-29 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0013_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.coach'),
        ),
    ]