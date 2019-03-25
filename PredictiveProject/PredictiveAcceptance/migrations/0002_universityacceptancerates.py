# Generated by Django 2.1.7 on 2019-03-25 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PredictiveAcceptance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityAcceptanceRates',
            fields=[
                ('student_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='PredictiveAcceptance.PredictiveUsers')),
                ('uor_accep_rate', models.IntegerField(blank=True, null=True)),
                ('uoa_accep_rate', models.IntegerField(blank=True, null=True)),
                ('ubc_accep_rate', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'university_acceptance_rates',
                'managed': False,
            },
        ),
    ]
