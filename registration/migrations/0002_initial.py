# Generated by Django 3.2.9 on 2021-12-12 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        ('buddy_program_data', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer_registration',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_registration_program', to='users.program'),
        ),
        migrations.AddField(
            model_name='volunteer_registration',
            name='program_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_registration_program_semester', to='buddy_program_data.program_semester'),
        ),
        migrations.AddField(
            model_name='volunteer_registration',
            name='session_choices',
            field=models.ManyToManyField(blank=True, related_name='choices_sessions', to='buddy_program_data.Session_Meeting_Option'),
        ),
        migrations.AddField(
            model_name='volunteer_registration',
            name='social_media_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social', to='buddy_program_data.social_media_source'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='characteristics',
            field=models.ManyToManyField(blank=True, related_name='student_characteristics', to='buddy_program_data.Student_Characteristic'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='current_grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_grade', to='buddy_program_data.grade'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='ethnicity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_ethnicity', to='buddy_program_data.ethnicity'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_gender', to='buddy_program_data.gender'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_info', to='registration.parent_registration'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='primary_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_language', to='buddy_program_data.language'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_program', to='users.program'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='program_semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_registration_program_semester', to='buddy_program_data.program_semester'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='reading_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_level', to='buddy_program_data.reading_description'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='registration_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registration_lang', to='buddy_program_data.language'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_grade', to='buddy_program_data.school'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='secondary_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_language', to='buddy_program_data.language'),
        ),
        migrations.AddField(
            model_name='student_registration',
            name='session_device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device_session', to='buddy_program_data.device_type'),
        ),
        migrations.AddField(
            model_name='parent_registration_ip_info',
            name='registration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_reg_ip', to='registration.parent_registration'),
        ),
        migrations.AddField(
            model_name='parent_registration',
            name='additional_info',
            field=models.ManyToManyField(blank=True, related_name='additional_checks', to='buddy_program_data.Parent_Additional_Information'),
        ),
        migrations.AddField(
            model_name='parent_registration',
            name='device_in_touch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_touch_device', to='buddy_program_data.device_type'),
        ),
        migrations.AddField(
            model_name='parent_registration',
            name='messaging_apps',
            field=models.ManyToManyField(blank=True, related_name='messaging', to='buddy_program_data.Message_App'),
        ),
        migrations.AddField(
            model_name='parent_registration',
            name='preferred_contact_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_language', to='buddy_program_data.language'),
        ),
        migrations.AddField(
            model_name='parent_registration',
            name='registration_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registration_language', to='buddy_program_data.language'),
        ),
        migrations.AddField(
            model_name='parent_registration',
            name='session_choices',
            field=models.ManyToManyField(blank=True, related_name='student_choices_sessions', to='buddy_program_data.Session_Meeting_Option'),
        ),
    ]
