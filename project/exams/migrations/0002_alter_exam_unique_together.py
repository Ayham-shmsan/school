# Generated by Django 5.1.4 on 2024-12-29 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together={('name', 'subject', 'section', 'academic_year')},
        ),
    ]