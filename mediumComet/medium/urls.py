from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from medium import views

urlpatterns = [
    url(r'^api/v1/topic/((?P<pk>[0-9]+)/)?$', views.TopicsView.as_view()),
    url(r'^api/v1/post/((?P<pk>[0-9]+)/)?$', views.PostView.as_view()),
]
