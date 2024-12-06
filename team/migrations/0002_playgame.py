# Generated by Django 5.1.3 on 2024-12-06 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_local', models.IntegerField(default=0)),
                ('score_visitor', models.IntegerField(default=0)),
                ('team_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_playGames', to='team.teams')),
                ('team_visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_playGames', to='team.teams')),
            ],
        ),
    ]