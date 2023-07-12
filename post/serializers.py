from rest_framework import serializers
from .models import Post


class PostListDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    class Meta:
        model = Post
        fields = ("id", "user", "title", "body")


class PostManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body")

