from django.contrib import admin
from .models import Post, PostType, PostDomain
# Register your models here.

admin.site.register(Post)
admin.site.register(PostDomain)
admin.site.register(PostType)
