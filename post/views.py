from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q, Prefetch
from .serializers import PostListDetailSerializer, PostManageSerializer
from .models import Post, Save, Tag
from rest_framework.generics import ListAPIView
from account.models import User


class PostListView(ListAPIView):
    serializer_class = PostListDetailSerializer

    def get_queryset(self):
        order_by = self.request.GET.get("q", "created").lower()
        if order_by not in ("created", "view"):
            order_by = "created"
        posts = Post.objects.select_related("user").prefetch_related("tag").all().order_by("-"+order_by)
        return posts


class PostDetailView(APIView):
   
    def get(self, request, pk):
        try:
            post = Post.objects.select_related("user").get(pk=pk)
            post.increase_view()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)  
     
        serializer = PostListDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        order_by = self.request.GET.get("q", "created").lower()
        if order_by not in ("created", "view"):
            order_by = "created"    
        posts = Post.objects.filter(user=self.request.user).select_related("user").prefetch_related("tag").all().order_by("-"+order_by)
        return posts


class PostSearch(APIView):

    def get(self, request):
        q = request.GET.get("q", "")
        posts = Post.objects.filter(Q(title__icontains=q)|
                                    Q(tag__name__icontains=q)).select_related("user").prefetch_related("tag").distinct() # We use distinct() to avoid duplicate results in queryset.
        serializer = PostListDetailSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ManageSave(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        Save.objects.create(user=request.user, post=post)
        return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if Save.objects.filter(user=request.user, post=post).exists():
            save = Save.objects.get(user=request.user, post=post)
            Save.delete(save)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class Mysave(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostListDetailSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(saves__user=self.request.user).select_related("user").prefetch_related(Prefetch("tag", queryset=Tag.objects.all()))
        return queryset