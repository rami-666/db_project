# Generated by Django 4.1.3 on 2022-11-18 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_coach_team_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('forTeam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.team')),
            ],
        ),
    ]
