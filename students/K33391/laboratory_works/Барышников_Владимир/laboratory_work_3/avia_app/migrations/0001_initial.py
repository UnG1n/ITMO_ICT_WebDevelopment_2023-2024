# Generated by Django 4.2.8 on 2024-01-26 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=50)),
                ('seats', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('carrier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('age', models.IntegerField()),
                ('education', models.CharField(max_length=100)),
                ('experience', models.IntegerField()),
                ('passport_data', models.CharField(max_length=20)),
                ('is_airport_employee', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=20)),
                ('distance', models.IntegerField()),
                ('departure_point', models.CharField(max_length=50)),
                ('destination_point', models.CharField(max_length=50)),
                ('departure_datetime', models.DateTimeField()),
                ('arrival_datetime', models.DateTimeField()),
                ('sold_tickets', models.IntegerField()),
                ('aircraft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avia_app.aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('position', models.CharField(max_length=50)),
                ('aircraft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avia_app.aircraft')),
            ],
        ),
    ]
