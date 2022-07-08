from __future__ import unicode_literals

from django.db import models


class post(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
# Create your models here.
