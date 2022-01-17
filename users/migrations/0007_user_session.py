# Generated by Django 3.2.9 on 2021-12-25 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('users', '0006_login_logout_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Session',
                'verbose_name_plural': 'User Sessions',
                'ordering': ['id'],
            },
        ),
    ]
