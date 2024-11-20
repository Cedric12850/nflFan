# Generated by Django 5.1.3 on 2024-11-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('town', models.CharField(max_length=60)),
                ('thumbnail', models.ImageField(upload_to='logo')),
            ],
        ),
    ]