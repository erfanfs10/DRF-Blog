from rest_framework import serializers
from .models import Post


class PostListDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = ("id", "user", "title", "body", "view", "tags")


class PostManageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "body")

