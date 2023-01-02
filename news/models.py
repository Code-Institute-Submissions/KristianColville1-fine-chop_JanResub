from django.db import models
from django.utils import timezone
from profiles.models import Profile
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
import os
from django.core.mail import send_mail
from django.conf import settings


class SubscribedUsers(models.Model):
    """
    SubscribedUsers Model
    """
    name = models.CharField(max_length=100, default='no username')
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    class Meta:
        verbose_name_plural = 'Subscribed Users'

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.TextField()

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def save(self):
        subscribers = SubscribedUsers.objects.all()
        for sub in subscribers:
            send_mail(self.subject, self.contents, settings.DEFAULT_FROM_EMAIL,
                      [sub.email])


class ArticleSeries(models.Model):
    """
    Newsletter series. If the newsletter is part of a collection.
    """

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    slug = models.SlugField("Series slug",
                            null=False,
                            blank=False,
                            unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    author = models.ForeignKey(Profile,
                               default=1,
                               on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg',
                              upload_to=image_upload_to,
                              max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']


class Article(models.Model):
    """
    Newsletter to be posted as article* on website.
    """

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug),
                                slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("Article slug",
                                    null=False,
                                    blank=False,
                                    unique=True)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries,
                               default="",
                               verbose_name="Series",
                               on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(Profile,
                               default=1,
                               on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg',
                              upload_to=image_upload_to,
                              max_length=255)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']
