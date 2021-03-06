# Generated by Django 3.2.9 on 2021-12-12 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buddy_program_data', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program_status',
            name='program',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='program_status', to='users.program'),
        ),
        migrations.AddField(
            model_name='program_semester',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_semester', to='users.program'),
        ),
        migrations.AddField(
            model_name='form_message',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form_message',
            name='for_form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_message', to='buddy_program_data.program_form'),
        ),
        migrations.AddField(
            model_name='form_message',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application_recipient',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_recipient', to=settings.AUTH_USER_MODEL),
        ),
    ]
