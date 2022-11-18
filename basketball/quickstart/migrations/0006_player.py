# Generated by Django 4.1.3 on 2022-11-17 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0005_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('agent', models.CharField(max_length=100)),
                ('pointsScored', models.IntegerField()),
                ('rebounds', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('turnovers', models.IntegerField()),
                ('inTeam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.team')),
            ],
        ),
    ]