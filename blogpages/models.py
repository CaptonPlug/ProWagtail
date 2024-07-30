from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from django.core.exceptions import ValidationError
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.fields import StreamField
from wagtail.blocks import TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from blocks import blocks as custom_blocks

class BlogIndex(Page):
    template = 'blogpages/blog_index.html'
    max_count = 1
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blogpages.BlogDetail"]
    
    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['blogpages'] = BlogDetail.objects.live().public()
        return context
    
class BlogPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'blogpages.BlogDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class BlogDetail(Page):
    parent_page_types = ["blogpages.BlogIndex"]
    subpage_types = []
    
    subtitle = models.CharField(max_length=100, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return self.name

    body = StreamField(
        [
            ('info', custom_blocks.InfoBlocks()),
            ('faq', custom_blocks.FAQListBlock()),
            ('text', custom_blocks.TextBlock()),
            ('image', custom_blocks.ImageBlock()),
            ('doc', DocumentChooserBlock()),
            ('page', blocks.PageChooserBlock(
                required=False,
                page_type='home.HomePage'
            )),
            ('author', SnippetChooserBlock('blogpages.Author')),
            ('carousel', custom_blocks.CarouselBlock()),
            ('call_to_action_1', custom_blocks.CallToAction1()),
        ],

        block_counts={
            #'text': {'min_num': 1},
            'image': {'max_num': 1},
        },
        use_json_field=True,
        blank=True,
        null=True,
    )
    
    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
       # FieldPanel('subtitle'),
        #FieldPanel('tags'),
    ]

    def clean(self):
        super().clean()

        errors = {}

        if 'post' in self.title.lower():
            errors['title'] = "Title cannot have this inappropriate word"

        if 'post' in self.subtitle.lower():
            errors['subtitle'] = "Subtitle cannot have this inappropriate word"

        if 'post' in self.slug.lower():
            errors['slug'] = "Slug cannot have this inappropriate word"

        if errors:
            raise ValidationError(errors)


# Create your models here.
