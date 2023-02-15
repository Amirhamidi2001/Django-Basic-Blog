from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", blog_views, name="blog"),
    path("single/", single_views, name="single"),
]
