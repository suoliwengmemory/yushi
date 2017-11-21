#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "mohen"
__date__ = "2017/11/16 14:45"

import xadmin
from .models import Post,Banner


class PostAdmin(object):

    list_display = ["type", "title", "image", "index", "author", "add_time"]
    search_fields = ["type", "title", "image", "index", "author"]
    list_filter = ["type", "title", "image", "index", "author", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Post, PostAdmin)

class BannerAdmin(object):
    list_display = ["type", "title", "image", "index", "author", "add_time"]
    search_fields = ["type", "title", "image", "index", "author"]
    list_filter = ["type", "title", "image", "index", "author", "add_time"]
    style_fields = {"detail": "ueditor"}
xadmin.site.register(Banner, BannerAdmin)
