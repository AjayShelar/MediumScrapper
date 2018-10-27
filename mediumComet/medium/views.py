# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_auth.registration.views import LoginView

from .serializers import *


class LoginViewCustom(LoginView):
    authentication_classes = ()


# Create your views here.
class TopicsView(ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView):

    permission_classes = (IsAdminUser, )
    serializer_class = TopicsSerializer

    def get(self, request, *args, **kwargs):
        if not kwargs.get('pk', None):
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)


class PostView(ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView):

    permission_classes = (IsAdminUser, )
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        if not kwargs.get('pk', None):
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.GET.get('topic', None):
            topic = Topics.objects.get(id=self.request.GET.get('topic'))
            return Post.get_topic_posts_qs(topic)
        return Post.objects.all()