from django.urls import path

from .views import home_page, post_page, create_post


app_name = "blog"

urlpatterns = [
    path("posts/", home_page, name="home_page"),
    path("posts/<int:post_id>/", post_page, name="post_page"),
    path("create_post", create_post, name="create_post"),
]
