# Generated by Django 5.1.4 on 2024-12-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_studentemail_student_studentmobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentEmail',
            field=models.CharField(max_length=30, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentMobile',
            field=models.CharField(max_length=10, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentPassword',
            field=models.CharField(max_length=50, verbose_name='Password'),
        ),
    ]
