# Generated by Django 5.0.6 on 2024-06-25 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpages', '0002_blogpagetags_blogdetail_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpagetags',
            old_name='content_objects',
            new_name='content_object',
        ),
    ]
