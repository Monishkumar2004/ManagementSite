# Generated by Django 5.1.6 on 2025-02-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_student_admission_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.CharField(blank=True, default='TEMP', max_length=50, null=True, unique=True),
        ),
    ]
