from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

from django.utils import timezone


class Article(models.Model):
    CATEGORY_CHOICES = [
        ("Transfery", "Transfery"),
        ("Mecze", "Mecze"),
        ("Puchary", "Puchary"),
    ]

    title = models.CharField(max_length=200, null=True)
    creator = models.ForeignKey(User, related_name="articles", on_delete=models.CASCADE)
    category = models.CharField(max_length=50 ,choices=CATEGORY_CHOICES)
    content = CKEditor5Field('Content', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/')
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

