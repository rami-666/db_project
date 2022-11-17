# Generated by Django 4.1.3 on 2022-11-17 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('gameNumber', models.IntegerField()),
                ('highlights', models.CharField(max_length=1000)),
                ('homeScore', models.IntegerField()),
                ('homeRebounds', models.IntegerField()),
                ('homeSteals', models.IntegerField()),
                ('homeTurnovers', models.IntegerField()),
                ('homeTimeouts', models.IntegerField()),
                ('homeFouls', models.IntegerField()),
                ('homeShotAttempts', models.IntegerField()),
                ('awayScore', models.IntegerField()),
                ('awayRebounds', models.IntegerField()),
                ('awaySteals', models.IntegerField()),
                ('awayTurnovers', models.IntegerField()),
                ('awayTimeouts', models.IntegerField()),
                ('awayFouls', models.IntegerField()),
                ('awayShotAttempts', models.IntegerField()),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='away', to='quickstart.team')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='home', to='quickstart.team')),
                ('inSeries', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.series')),
                ('mvp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quickstart.player')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='winner', to='quickstart.team')),
            ],
        ),
    ]
