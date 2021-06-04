# Generated by Django 3.2.4 on 2021-06-04 13:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.CharField(max_length=9, unique=True, validators=[django.core.validators.MinLengthValidator(9)])),
                ('privateName', models.CharField(max_length=20)),
                ('familyName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catchBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotChairs.employees')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotChairs.organizations')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotChairs.organizations'),
        ),
        migrations.CreateModel(
            name='EmployeePlacesHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReservationTime', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotChairs.employees')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotChairs.places')),
            ],
        ),
        migrations.AddConstraint(
            model_name='places',
            constraint=models.UniqueConstraint(fields=('name', 'organization'), name='Unique place'),
        ),
    ]
