# Generated by Django 5.0.3 on 2024-03-27 11:52

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
