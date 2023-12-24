# Generated by Django 4.2.6 on 2023-10-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=150)),
                ('car_company', models.CharField(max_length=150)),
                ('car_model', models.CharField(max_length=100)),
                ('car_price', models.BigIntegerField()),
                ('fuel_type', models.CharField(max_length=150)),
            ],
        ),
    ]
