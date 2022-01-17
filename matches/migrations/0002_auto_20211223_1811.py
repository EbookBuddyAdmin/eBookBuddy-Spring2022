# Generated by Django 3.2.9 on 2021-12-23 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_program_data', '0014_session_meeting_option_slot_letter'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader_match_profile',
            name='available_slots',
        ),
        migrations.AddField(
            model_name='reader_match_profile',
            name='open_slots',
            field=models.ManyToManyField(blank=True, related_name='open', to='buddy_program_data.Reading_Session_Day_Time'),
        ),
    ]
