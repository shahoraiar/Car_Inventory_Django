# Generated by Django 4.2.3 on 2024-02-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('car_type', models.CharField(choices=[('Electric', 'Electric'), ('Gas', 'Gas')], max_length=8)),
                ('battery_capacity', models.FloatField(blank=True, null=True)),
                ('fuel_efficiency', models.FloatField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
