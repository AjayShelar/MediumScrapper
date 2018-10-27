# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q

# Create your models here.


class Topics(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name) + '  =>  ' + str(self.url)


class Post(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    topic = models.ForeignKey(
        Topics, related_name='topic_posts', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + '  =>  ' + str(self.author)

    @staticmethod
    def get_topic_posts_qs(topic):
        return Post.objects.filter(Q(topic=topic).all())
