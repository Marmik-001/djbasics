# Generated by Django 5.1.4 on 2024-12-12 07:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='facultyRegistrationDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='RegistrationDate'),
        ),
    ]