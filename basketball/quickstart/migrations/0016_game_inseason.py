# Generated by Django 4.1.3 on 2022-11-29 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0015_remove_team_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='inSeason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.season'),
        ),
    ]