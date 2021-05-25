import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    post_author = models.CharField(max_length=10)
    post_body = models.TextField()

    def __str__(self):
        return self.post_title
    def recently_published(self):
        return self.pub_date >= timezone.now() - datetime.datetime(days=1)

