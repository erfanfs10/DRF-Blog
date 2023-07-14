from rest_framework import serializers
from .models import Post


class PostListDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    tag = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = ("id", "user", "title", "body", "view", "created", "tag")


class PostManageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "body")

