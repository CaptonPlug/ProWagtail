# Generated by Django 5.0.6 on 2024-07-22 17:10

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpages', '0009_alter_author_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('doc', wagtail.documents.blocks.DocumentChooserBlock()), ('page', wagtail.blocks.PageChooserBlock(page_type=['home.HomePage'], required=False)), ('author', wagtail.snippets.blocks.SnippetChooserBlock('blogpages.Author')), ('carousel', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('author', wagtail.blocks.TextBlock())]))]))], blank=True, null=True),
        ),
    ]
