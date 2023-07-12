from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    class Meta:
        model = Post
        fields = ("id", "user", "title", "body")


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    class Meta:
        model = Post
        fields = ("user", "title", "body")
