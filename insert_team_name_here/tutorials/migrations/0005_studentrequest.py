# Generated by Django 5.1.2 on 2024-12-12 17:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_coursetype_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('unallocated', 'Unallocated'), ('allocated', 'Allocated')], default='unallocated', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('allocated_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='allocated_requests', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
