# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Topics(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    post = models.ForeignKey(
        'Post', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + '  =>  ' + str(self.url)


class Post(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    details = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title) + '  =>  ' + str(self.author)
