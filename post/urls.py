from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostManageView,
                    MyPostsView)


urlpatterns = [
    path("post-list/", PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post-create/", PostCreateView.as_view(), name="post-create"),
    path("post-manage/<int:pk>/", PostManageView.as_view(), name="post-manage"),
    path("myposts/", MyPostsView.as_view(), name="mypost"),
]