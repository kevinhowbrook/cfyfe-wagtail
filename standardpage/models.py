from django.db import models
    
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Orderable, Page


class StandardPage(Page):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)
    background_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL
        )
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('background_image'),
    ]

