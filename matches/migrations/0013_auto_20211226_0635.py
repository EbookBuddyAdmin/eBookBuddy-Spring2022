# Generated by Django 3.2.9 on 2021-12-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0012_match_attendance_record_match_status_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match_attendance_record',
            old_name='volunteer_in_breakout_alone',
            new_name='reader_in_breakout_alone',
        ),
        migrations.RenameField(
            model_name='match_attendance_record',
            old_name='volunteer_in_breakout_w_student',
            new_name='reader_in_breakout_w_student',
        ),
        migrations.RenameField(
            model_name='match_attendance_record',
            old_name='volunteer_time_in',
            new_name='reader_time_in',
        ),
        migrations.RenameField(
            model_name='match_attendance_record',
            old_name='volunteer_time_out',
            new_name='reader_time_out',
        ),
        migrations.RemoveField(
            model_name='match_attendance_record',
            name='volunteer_present',
        ),
        migrations.RemoveField(
            model_name='match_attendance_record',
            name='volunteer_reassigned',
        ),
        migrations.AddField(
            model_name='match_attendance_record',
            name='reader_present',
            field=models.BooleanField(default=False, verbose_name='R-Present'),
        ),
        migrations.AddField(
            model_name='match_attendance_record',
            name='reader_reassigned',
            field=models.BooleanField(default=False, verbose_name='R-R'),
        ),
    ]