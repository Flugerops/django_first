from django.urls import path

from .views import my_test_view


urlpatterns = [
    path("test/", my_test_view, name="test_view"),
]
