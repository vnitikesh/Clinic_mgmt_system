# Generated by Django 2.1.7 on 2020-09-11 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_admin', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Accounts')),
                ('clinic_patient_relation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patients.Patients')),
            ],
        ),
    ]
