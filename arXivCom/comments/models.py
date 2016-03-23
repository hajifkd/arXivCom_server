from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    arXiv_id = models.CharField(max_length=30, unique=True)

class Comment(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


