# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Topics, Post

# Register your models here.


class TopicsAdmin(admin.ModelAdmin):
    model = Topics


class PostsAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(Post, PostsAdmin)
admin.site.register(Topics, TopicsAdmin)