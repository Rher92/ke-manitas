# Generated by Django 3.2.11 on 2022-04-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_auto_20220425_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvehicleworkday',
            name='close',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicleworkday',
            name='close',
            field=models.BooleanField(default=False),
        ),
    ]
