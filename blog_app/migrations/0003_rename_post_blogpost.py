# Generated by Django 4.2.6 on 2023-10-20 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
    ]
