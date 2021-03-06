# Generated by Django 3.2.9 on 2021-12-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20211220_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent_registration_note',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='parent_registration_note',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AddField(
            model_name='student_registration_note',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='student_registration_note',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AddField(
            model_name='volunteer_registration_note',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='volunteer_registration_note',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
    ]
