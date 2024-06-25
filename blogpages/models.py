from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from django.core.exceptions import ValidationError
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

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
    body = RichTextField(blank=True, features=['h2', 'image'])

    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('tags'),
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
