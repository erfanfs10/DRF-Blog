from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import PostListDetailSerializer, PostManageSerializer
from .models import Post
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView


class PostListView(ListAPIView):
    serializer_class = PostListDetailSerializer

    def get_queryset(self):
        posts = Post.objects.select_related("user").all()
        return posts


class PostDetailView(RetrieveAPIView):
    queryset = Post
    serializer_class = PostListDetailSerializer


class PostCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PostManageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PostManageView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostManageSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostManageSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.user != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Post.delete(post)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class MyPostsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostListDetailSerializer

    def get_queryset(self):
        posts = Post.objects.filter(user=self.request.user).select_related("user").all()
        return posts
