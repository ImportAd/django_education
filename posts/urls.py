from django.urls import path

# from .views import post_list
from .views import PostList

urlpatterns = [
    # path("post/", post_list, name="post"),
    path("post/", PostList.as_view(), name="post")
]
