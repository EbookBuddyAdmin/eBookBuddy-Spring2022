# Generated by Django 3.2.9 on 2021-12-28 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_program_data', '0017_alter_daily_session_session_end_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server_schedule',
            name='times',
        ),
        migrations.AddField(
            model_name='server_time',
            name='server_schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='buddy_program_data.server_schedule'),
        ),
        migrations.AlterField(
            model_name='server_time',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]