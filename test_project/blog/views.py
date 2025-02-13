from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Post


# Create your views here.
def home_page(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {"post": post})


def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = get_object_or_404(User, id=1)
        try:
            post = Post(title=title, content=content, author=author)
            post.full_clean()
        except Exception as e:
            print(e)
            return HttpResponse("<h1>Bad values</h1>")
        else:
            post.save()
            messages.success(
                request, f"Post: {post.title} has been published successfully!"
            )
        return redirect("blog:home_page")

    return render(request, "create_post.html")
