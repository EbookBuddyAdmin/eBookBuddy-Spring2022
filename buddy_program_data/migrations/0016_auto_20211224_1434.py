# Generated by Django 3.2.9 on 2021-12-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_program_data', '0015_session_meeting_option_session_day_times'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server_time',
            name='offset',
        ),
        migrations.AddField(
            model_name='server_schedule',
            name='offset',
            field=models.IntegerField(blank=True, help_text='-240 DST, -300 no DST', null=True),
        ),
    ]
