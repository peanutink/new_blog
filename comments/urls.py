#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
