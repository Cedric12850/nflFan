# Generated by Django 5.1.3 on 2024-12-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playgames', '0003_alter_playgame_played_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playgame',
            name='score_local',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='playgame',
            name='score_visitor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
