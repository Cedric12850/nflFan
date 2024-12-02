# Generated by Django 5.1.3 on 2024-12-02 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_players_poste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player_position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('abrev', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='players',
            name='poste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='players.player_position'),
        ),
    ]
