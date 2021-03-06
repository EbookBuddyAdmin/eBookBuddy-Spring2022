# Generated by Django 3.2.9 on 2021-12-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20211219_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_registration',
            name='charges_pending',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='computer',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='convicted',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='fluent_spanish',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='in_school',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='previously_paired',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='refused_participation',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='sponsor_child',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_registration',
            name='volunteer_other_areas',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True),
        ),
    ]
