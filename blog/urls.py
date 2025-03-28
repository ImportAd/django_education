from django.urls import path

from .views import post_list, post_detail

urlpatterns = [
    path("bog/", post_list, name="blog"),
    path("post/<int:pk>", post_detail, name="post_detail"),
]
