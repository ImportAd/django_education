from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="blog.html",
        context={"posts": posts},
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request=request,
        template_name="post_detail.html",
        context={"post": post},
    )
