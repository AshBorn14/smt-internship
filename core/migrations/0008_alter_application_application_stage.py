# Generated by Django 4.1.7 on 2023-09-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_application_application_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_stage',
            field=models.CharField(choices=[('Submission', 'Submission'), ('Review', 'Review'), ('Verification', 'Verification'), ('Onboarding', 'Onboarding')], default='Submission', max_length=80),
        ),
    ]
