#!/usr/bin/env python
# _*_coding:utf-8 _*_
from django.urls import path
from django.conf.urls import url
from . import views

__title__ = ''
__author__ = "wenyali"
__mtime__ = "2018/5/8"
urlpatterns = [
    url(r'^tasks/$', views.task_list, name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]
