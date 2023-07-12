from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import PostListSerializer, PostDetailSerializer
from .models import Post


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.select_related("user").all()
        serialzirer = PostListSerializer(posts, many=True)
        return Response(serialzirer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serialzirer = PostDetailSerializer(post)
        return Response(serialzirer.data, status=status.HTTP_200_OK)
