# Generated by Django 5.1.2 on 2024-12-12 20:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_studentrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrequest',
            name='admin_reply',
            field=models.TextField(blank=True, help_text='Reply provided by the admin.', null=True),
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='replied_by',
            field=models.ForeignKey(blank=True, help_text='Admin who provided the reply.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to=settings.AUTH_USER_MODEL),
        ),
    ]
