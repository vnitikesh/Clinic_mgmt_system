# Generated by Django 2.1.7 on 2020-09-11 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='patient_joining',
        ),
    ]
