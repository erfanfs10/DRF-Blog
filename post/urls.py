from django.urls import path
from .views import PostListView, PostDetailView


urlpatterns = [
    path("post_list/", PostListView.as_view(), name="post-list"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    
]