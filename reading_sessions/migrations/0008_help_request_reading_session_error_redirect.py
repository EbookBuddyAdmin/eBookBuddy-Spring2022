# Generated by Django 3.2.9 on 2021-12-30 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buddy_program_data', '0018_auto_20211228_0458'),
        ('reading_sessions', '0007_alter_match_session_status_sch_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading_Session_Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(blank=True, max_length=255, null=True)),
                ('function_name', models.CharField(blank=True, max_length=255, null=True)),
                ('location_in_function', models.CharField(blank=True, max_length=255, null=True)),
                ('occurred_for_user', models.CharField(blank=True, max_length=255, null=True)),
                ('error_text', models.TextField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'Reading Session Error',
                'verbose_name_plural': 'Reading Session Errors',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_url', models.URLField(blank=True, max_length=500, null=True)),
                ('auto_send', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
                ('to_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='buddy_program_data.room')),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redirect_to', to=settings.AUTH_USER_MODEL)),
                ('user_to_redirect', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='redirect', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Redirect',
                'verbose_name_plural': 'Redirects',
            },
        ),
        migrations.CreateModel(
            name='Help_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_url', models.URLField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('user_message', models.TextField(blank=True)),
                ('done', models.BooleanField(default=False)),
                ('visited_time', models.DateTimeField(blank=True, null=True, verbose_name='visited time')),
                ('from_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_needing_help', to='buddy_program_data.room')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to=settings.AUTH_USER_MODEL)),
                ('visited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Help Request',
                'verbose_name_plural': 'Help Requests',
            },
        ),
    ]
