from django.db import models
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        get_user_model(),
        related_name='likes',
        null=True,
        blank=True
    )
    views = models.ManyToManyField(
        get_user_model(),
        related_name='views',
        null=True,
        blank=True
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created', 'title')
