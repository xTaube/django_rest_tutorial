from django.contrib import admin
from django.urls import path, include, re_path
from .views import UserDetailApiView, UserStatusAPIView

urlpatterns = [
    re_path(r'(?P<username>\w+)/status/$', UserStatusAPIView.as_view(), name='status-list'),
    re_path(r'(?P<username>\w+)/$', UserDetailApiView.as_view(), name='detail'),
]
