# Generated by Django 3.2.9 on 2022-01-14 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buddy_program_data', '0020_day_with_orientation_meeting_day_with_team_meeting_mega_team_team_team_meeting'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Team_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_role', models.CharField(blank=True, choices=[('Coordinator', 'Coordinator'), ('Team Leader', 'Team Leader'), ('Member', 'Member')], max_length=30, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('mega', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_mega', to='buddy_program_data.mega_team')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_team', to='buddy_program_data.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Team Info',
                'verbose_name_plural': 'Users Team Info',
            },
        ),
    ]
