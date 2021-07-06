from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel

from wagtail_live.models import LivePageMixin


class LiveBlogPage(LivePageMixin, Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hero_text = RichTextField()

    content_panels = Page.content_panels + [ 
        ImageChooserPanel('hero_image'),
        FieldPanel('hero_text'),
    ] + LivePageMixin.panels