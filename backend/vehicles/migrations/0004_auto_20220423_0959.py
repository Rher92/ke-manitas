# Generated by Django 3.2.11 on 2022-04-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20220423_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvehicle',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
