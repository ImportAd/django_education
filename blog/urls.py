from django.urls import path

from .views import post_list

urlpatterns = [
    path("bog/", post_list, name="blog"),
]
