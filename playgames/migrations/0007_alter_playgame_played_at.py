# Generated by Django 5.1.3 on 2024-12-12 09:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playgames', '0006_alter_week_week_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playgame',
            name='played_at',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
