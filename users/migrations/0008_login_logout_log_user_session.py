# Generated by Django 3.2.9 on 2021-12-25 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_logout_log',
            name='user_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='django_session', to='users.user_session'),
        ),
    ]