# Generated by Django 5.1.3 on 2024-11-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_delete_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='owner',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]