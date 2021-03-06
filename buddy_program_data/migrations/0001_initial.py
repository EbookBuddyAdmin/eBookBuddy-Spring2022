# Generated by Django 3.2.9 on 2021-12-12 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Answer Type',
                'verbose_name_plural': 'Answer Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Application_Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_student', models.BooleanField(default=True, verbose_name='Student Registration')),
                ('receive_vol', models.BooleanField(default=True, verbose_name='Volunteer Registration')),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
            ],
            options={
                'verbose_name': 'Application Recipient',
                'verbose_name_plural': 'Application Recipients',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Current_Education_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('span_name', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Current Education Class',
                'verbose_name_plural': 'Current Education Classes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Current_Education_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('span_name', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Current Education Level',
                'verbose_name_plural': 'Current Education Levels',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('span_name', models.CharField(blank=True, max_length=100)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('short_name', models.CharField(blank=True, max_length=3, null=True)),
                ('letter', models.CharField(blank=True, max_length=3, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Day',
                'verbose_name_plural': 'Days',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Device_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('for_users', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Device Type',
                'verbose_name_plural': 'Device Types',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_option', models.CharField(max_length=100, unique=True)),
                ('span_option', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ethnicity',
                'verbose_name_plural': 'Ethnicities',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Form_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('message_content', models.TextField(blank=True, max_length=5000, null=True)),
                ('span_content', models.TextField(blank=True, max_length=5000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
            ],
            options={
                'verbose_name': 'Form Message',
                'verbose_name_plural': 'Form Messages',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('eng_gender', models.CharField(blank=True, max_length=100, null=True)),
                ('span_gender', models.CharField(blank=True, max_length=100, null=True)),
                ('for_users', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'ordering': ['letter'],
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=150)),
                ('span_name', models.CharField(blank=True, max_length=150, null=True)),
                ('abbr', models.CharField(blank=True, max_length=3, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=150)),
                ('span_name', models.CharField(max_length=150)),
                ('iso', models.CharField(blank=True, max_length=2, null=True)),
                ('active', models.BooleanField(default=True)),
                ('display_form_language', models.BooleanField(default=False)),
                ('display_primary', models.BooleanField(default=False)),
                ('display_secondary', models.BooleanField(default=False)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Message_App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Message App',
                'verbose_name_plural': 'Message Apps',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Opportunity_Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Opportunity Source',
                'verbose_name_plural': 'Opportunity Sources',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Parent_Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('eng_text', models.TextField(blank=True, max_length=1500, null=True)),
                ('span_text', models.TextField(blank=True, max_length=1500, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Parent Additional Information',
                'verbose_name_plural': 'Parent Additional Information',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Program_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Program Form',
                'verbose_name_plural': 'Program Forms',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Program_Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('active_semester', models.BooleanField(default=False)),
                ('accepting_students', models.BooleanField(default=False)),
                ('accepting_volunteers', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Program Semester',
                'verbose_name_plural': 'Program Semesters',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Program_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updating', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Program Status',
                'verbose_name_plural': 'Program Status',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reading_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('eng_text', models.CharField(blank=True, max_length=100, null=True)),
                ('span_text', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Reading Description',
                'verbose_name_plural': 'Reading Descriptions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('letter', models.CharField(blank=True, max_length=1)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Room Type',
                'verbose_name_plural': 'Room Types',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('display_in_list', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'School',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Session_Day_Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('span_name', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('span_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('days', models.ManyToManyField(blank=True, related_name='session_options', to='buddy_program_data.Day')),
            ],
            options={
                'verbose_name': 'Session Day Option',
                'verbose_name_plural': 'Session Day Options',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Session_Time_Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=5, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Session Time Option',
                'verbose_name_plural': 'Session Time Options',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Social_Media_Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Social Media Source',
                'verbose_name_plural': 'Social Media Sources',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Student_Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('eng_text', models.TextField(blank=True, max_length=1500, null=True)),
                ('span_text', models.TextField(blank=True, max_length=1500, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Student Characteristic',
                'verbose_name_plural': 'Student Characteristics',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Volunteer_Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Volunteer Opportunity',
                'verbose_name_plural': 'Volunteer Opportunities',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Volunteer_Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Volunteer Reason',
                'verbose_name_plural': 'Volunteer Reasons',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Web_Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Web Source',
                'verbose_name_plural': 'Web Sources',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Team_Meeting_Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_time', models.TimeField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=5, null=True)),
                ('active', models.BooleanField(default=True)),
                ('meeting_day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_meeting_day', to='buddy_program_data.day')),
            ],
            options={
                'verbose_name': 'Team Meeting Time',
                'verbose_name_plural': 'Team Meeting Times',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Session_Meeting_Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('day_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session_day', to='buddy_program_data.session_day_option')),
                ('time_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session_time', to='buddy_program_data.session_time_option')),
            ],
            options={
                'verbose_name': 'Session Meeting Option',
                'verbose_name_plural': 'Session Meeting Options',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('room_url', models.URLField(blank=True, max_length=500, null=True)),
                ('show_in_session_list', models.BooleanField(default=True, verbose_name='show in session')),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_room', to='buddy_program_data.room_type', verbose_name='Room Type')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.CharField(blank=True, max_length=10, null=True)),
                ('required', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Depends', 'Depends on App Factors')], max_length=30, null=True)),
                ('eng_text', models.TextField(max_length=1500)),
                ('span_text', models.TextField(blank=True, max_length=1500, null=True)),
                ('field_name', models.CharField(max_length=150)),
                ('answer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_type', to='buddy_program_data.answer_type')),
                ('for_form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_question', to='buddy_program_data.program_form')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
    ]
