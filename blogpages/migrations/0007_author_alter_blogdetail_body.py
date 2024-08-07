# Generated by Django 5.0.6 on 2024-07-16 16:17

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpages', '0006_alter_blogdetail_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('doc', wagtail.documents.blocks.DocumentChooserBlock()), ('page', wagtail.blocks.PageChooserBlock(page_type=['home.HomePage'], required=False)), ('carousel', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('author', wagtail.blocks.TextBlock())]))]))], blank=True, null=True),
        ),
    ]
