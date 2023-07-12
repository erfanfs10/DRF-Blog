from django.contrib import admin
from .models import Like, Post


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created", "updated")
