from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()

class Article(models.Model):
    arXiv_id = models.CharField(max_length=30)
    comments = models.ManyToManyField(Comment)

