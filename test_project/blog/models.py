from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=240)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def get_absolute_url(self):
        return reverse("blog:post_page", args=[self.id])

    def __repr__(self):
        return f"{self.title}"


class Comment(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __repr__(self):
        return f"{self.content}"
