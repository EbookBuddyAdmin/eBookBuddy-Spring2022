# Generated by Django 3.2.9 on 2021-12-12 22:17

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import localflavor.us.models
import phonenumber_field.modelfields
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buddy_program_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_first_name', models.CharField(max_length=150)),
                ('parent_last_name', models.CharField(max_length=150)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=16, null=True, region=None)),
                ('county', models.CharField(blank=True, max_length=150, null=True)),
                ('other_device_in_touch', models.CharField(blank=True, max_length=255, null=True)),
                ('internet', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True)),
                ('computer', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True)),
                ('flexible_schedule', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True)),
                ('parent_available', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True)),
                ('parent_can_help', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True)),
                ('help_name', models.CharField(blank=True, max_length=255, null=True)),
                ('help_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=16, null=True, region=None)),
                ('help_relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('consent_liability_initials', models.CharField(blank=True, max_length=255, null=True)),
                ('media_release_initials', models.CharField(blank=True, max_length=255, null=True)),
                ('other_message_app', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
            ],
            options={
                'verbose_name': 'Parent Registration',
                'verbose_name_plural': 'Parent Registrations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Parent_Registration_IP_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_valid', models.BooleanField(default=False)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('ws_connected', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
            options={
                'verbose_name': 'Parent Registration IP Info',
                'verbose_name_plural': 'Parent Registration IP Info',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Registration_Websocket_Error',
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
                'verbose_name': 'Registration Websocket Error',
                'verbose_name_plural': 'Registration Websocket Errors',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_first_name', models.CharField(max_length=150)),
                ('child_last_name', models.CharField(max_length=150)),
                ('dob', models.DateField(blank=True, null=True)),
                ('other_school', models.CharField(blank=True, max_length=255, null=True)),
                ('prior_participation', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30, null=True)),
                ('other_primary_language', models.CharField(blank=True, max_length=255, null=True)),
                ('other_secondary_language', models.CharField(blank=True, max_length=255, null=True)),
                ('relationship_to_child', models.CharField(blank=True, max_length=255, null=True)),
                ('child_comment', models.TextField(blank=True, max_length=3000, null=True)),
                ('other_session_device', models.CharField(blank=True, max_length=255, null=True)),
                ('cropped_profile_image', models.ImageField(blank=True, null=True, upload_to='user_profile_images/student')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='temp_profile_images/student')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
            ],
            options={
                'verbose_name': 'Student Registration',
                'verbose_name_plural': 'Student Registrations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Volunteer_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_type', models.CharField(blank=True, choices=[('New', 'New Volunteer'), ('Returning', 'Returning Volunteer')], max_length=30, null=True, verbose_name='Type')),
                ('dob', models.DateField(blank=True, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='Parent Email')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=16, null=True, region=None)),
                ('in_school', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('current_school', models.CharField(blank=True, max_length=150, null=True)),
                ('previously_paired', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('student_name', models.CharField(blank=True, max_length=255, null=True)),
                ('teamleader_name', models.CharField(blank=True, max_length=255, null=True)),
                ('returning_referred', models.CharField(blank=True, max_length=255, null=True)),
                ('fluent_spanish', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('person_referral', models.CharField(blank=True, max_length=255, null=True)),
                ('computer', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('children_experience', models.TextField(blank=True, max_length=5000, null=True)),
                ('reason', models.TextField(blank=True, max_length=2000, null=True)),
                ('reason_not_listed', models.TextField(blank=True, max_length=1000, null=True)),
                ('volunteer_other_areas', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('ref_name_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('ref_email_1', models.EmailField(blank=True, max_length=80, null=True, verbose_name='Email')),
                ('ref_phone_1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=16, null=True, region=None, verbose_name='Phone Number')),
                ('ref_relationship_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Relationship to you')),
                ('ref_name_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('ref_email_2', models.EmailField(blank=True, max_length=80, null=True, verbose_name='Email')),
                ('ref_phone_2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=16, null=True, region=None, verbose_name='Phone Number')),
                ('ref_relationship_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Relationship to you')),
                ('agree_requirements_initials', models.CharField(blank=True, max_length=255, null=True)),
                ('statements_true_initials', models.CharField(blank=True, max_length=255, null=True)),
                ('remove_volunteers_initials', models.CharField(blank=True, max_length=255, null=True)),
                ('cropped_profile_image', models.ImageField(blank=True, null=True, upload_to=registration.models.volunteer_profile_images)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=registration.models.volunteer_temp_images)),
                ('web_source', models.CharField(blank=True, max_length=255, null=True)),
                ('sponsor_child', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('convicted', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('convicted_text', models.TextField(blank=True, max_length=2000, null=True)),
                ('charges_pending', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('charges_pending_text', models.TextField(blank=True, max_length=2000, null=True)),
                ('refused_participation', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'N/A')], max_length=30, null=True)),
                ('refused_participation_text', models.TextField(blank=True, max_length=2000, null=True)),
                ('full_name_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('county', models.CharField(blank=True, max_length=150, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True, verbose_name='date submitted')),
                ('additional_interests', models.ManyToManyField(blank=True, related_name='interest_additional', to='buddy_program_data.Volunteer_Opportunity')),
                ('current_education_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_class', to='buddy_program_data.current_education_class')),
                ('current_education_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_level', to='buddy_program_data.current_education_level')),
                ('device_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='buddy_program_data.device_type')),
                ('ethnicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vol_ethnicity', to='buddy_program_data.ethnicity')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vol_gender', to='buddy_program_data.gender')),
                ('highest_education_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highest_education', to='buddy_program_data.current_education_level')),
                ('meeting_times', models.ManyToManyField(blank=True, related_name='team_meeting_times', to='buddy_program_data.Team_Meeting_Time')),
                ('opportunity_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hear_about_us', to='buddy_program_data.opportunity_source')),
                ('other_reasons', models.ManyToManyField(blank=True, related_name='reasons_others', to='buddy_program_data.Volunteer_Reason')),
            ],
            options={
                'verbose_name': 'Volunteer Registration',
                'verbose_name_plural': 'Volunteer Registrations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Volunteer_Registration_IP_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_valid', models.BooleanField(default=False)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('ws_connected', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('registration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vol_reg_ip', to='registration.volunteer_registration')),
            ],
            options={
                'verbose_name': 'Volunteer Registration IP Info',
                'verbose_name_plural': 'Volunteer Registration IP Info',
                'ordering': ['id'],
            },
        ),
    ]
