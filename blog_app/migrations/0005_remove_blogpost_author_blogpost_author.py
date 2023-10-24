# Generated by Django 4.2.6 on 2023-10-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_remove_blogpost_author_blogpost_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
