from django.contrib import admin
from django.contrib.admin import register
from .models import User

@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "image", "bio", "created", "is_active")
    list_filter = ("is_active",)
    list_editable = ("is_active",)

