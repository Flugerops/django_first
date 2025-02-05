from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def home_page(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {"post": post})
