# Generated by Django 2.1.7 on 2020-09-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_busines_admin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='is_clinic_admin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='is_doctor',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='accounts',
            name='is_patient',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
