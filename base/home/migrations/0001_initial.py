# Generated by Django 5.1 on 2024-08-14 18:56

import django.db.models.deletion
import home.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDietryData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMedicalData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hemoglobin_level', models.DecimalField(decimal_places=2, max_digits=3)),
                ('iron_levels', models.DecimalField(decimal_places=2, max_digits=3)),
                ('rbc_count', models.CharField(max_length=10, null=True)),
                ('medication', models.TextField(blank=True, null=True)),
                ('reports', models.FileField(upload_to=home.models.user_medical_data_upload_to)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPersonalData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_img', models.ImageField(upload_to='profile_img/')),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=3)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3)),
                ('height', models.CharField(blank=True, max_length=4, null=True)),
                ('health_history', models.TextField(blank=True, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
