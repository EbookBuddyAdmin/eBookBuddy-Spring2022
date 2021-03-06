# Generated by Django 3.2.9 on 2021-12-25 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0010_auto_20211224_1217'),
        ('buddy_program_data', '0017_alter_daily_session_session_end_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Session_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_redirect_on', models.BooleanField(default=False)),
                ('logged_in', models.BooleanField(default=False)),
                ('on_landing_page', models.BooleanField(default=False)),
                ('needs_new_buddy', models.BooleanField(default=False, verbose_name='Needs New Buddy')),
                ('needs_session_match', models.BooleanField(default=False, verbose_name='Needs Match')),
                ('in_room_with_sch_buddy', models.BooleanField(default=False, verbose_name='With Sch Buddy')),
                ('in_room_with_temp_buddy', models.BooleanField(default=False, verbose_name='With Temp Buddy')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('current_active_match_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_type_active', to='matches.match_type', verbose_name='Type Active')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_location', to='buddy_program_data.room')),
                ('scheduled_buddy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sch_buddy', to=settings.AUTH_USER_MODEL)),
                ('scheduled_match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sch_match', to='matches.scheduled_match')),
                ('temp_match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temp_match', to='matches.temporary_match')),
                ('temporary_buddy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp_buddy', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='session_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Session Status',
                'verbose_name_plural': 'User Session Statuses',
                'ordering': ['user'],
            },
        ),
    ]
