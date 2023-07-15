from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostManageView,
                    MyPostsView, PostSearch,
                    ManageSave, Mysave, ManageTag)


urlpatterns = [
    path("list/", PostListView.as_view(), name="post-list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("manage/<int:pk>/", PostManageView.as_view(), name="manage-post"),
    path("myposts/", MyPostsView.as_view(), name="myposts"),
    path("search/", PostSearch.as_view(), name="post-search"),
    path("save/<int:pk>/", ManageSave.as_view(), name="manage-save"),
    path("mysaves/", Mysave.as_view(), name="mysaves"),
    path("tag/<int:pk>/", ManageTag.as_view(), name="manage-tag")
]