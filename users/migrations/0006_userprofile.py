# Generated by Django 4.2.7 on 2024-03-20 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=users.models.CustomUser)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]