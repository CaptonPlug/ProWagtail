# Generated by Django 5.0.6 on 2024-06-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_cta_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='cta_external_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
