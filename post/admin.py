from django.contrib import admin
from .models import Tag, Post


class TagInline(admin.StackedInline):
    model = Post.tags.through
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created", "updated")
    inlines = (TagInline,)


@admin.register(Tag)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("name",)
