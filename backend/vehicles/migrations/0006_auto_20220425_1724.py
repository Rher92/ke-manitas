# Generated by Django 3.2.11 on 2022-04-25 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_auto_20220423_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehicleworkday',
            name='km_finish',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalvehicleworkday',
            name='km_init',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleworkday',
            name='km_finish',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleworkday',
            name='km_init',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleworkdayfiles',
            name='vehicle_workday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workday_file', related_query_name='workday_file', to='vehicles.vehicleworkday'),
        ),
        migrations.AlterField(
            model_name='vehicleworkdayfiles',
            name='vehicle_workday_expenses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='workday_file', related_query_name='workday_file', to='vehicles.expensesvehicleworkday'),
        ),
    ]
