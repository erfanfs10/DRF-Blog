from django.contrib import admin
from .models import Tag, Post, Save


class TagInline(admin.StackedInline):
    model = Post.tag.through
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created", "view")
    inlines = (TagInline,)


@admin.register(Tag)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Save)
class SaveAdmin(admin.ModelAdmin):
    list_display = ("user", "post")