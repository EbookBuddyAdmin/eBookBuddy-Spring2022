# Generated by Django 3.2.9 on 2021-12-28 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0014_student_match_profile_scheduled_slots'),
        ('reading_sessions', '0006_auto_20211227_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_session_status',
            name='sch_match',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sch_match_status', to='matches.scheduled_match'),
        ),
    ]
