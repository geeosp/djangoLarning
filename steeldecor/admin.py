# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import django.contrib

# Register your models here.
from steeldecor.models import Post

admin.site.register(Post)