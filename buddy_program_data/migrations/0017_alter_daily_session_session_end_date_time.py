# Generated by Django 3.2.9 on 2021-12-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_program_data', '0016_auto_20211224_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_session',
            name='session_end_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date/Time'),
        ),
    ]
