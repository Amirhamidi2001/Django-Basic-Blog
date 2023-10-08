from django.urls import path
from .views import *
from .feeds import LatestEntriesFeed

app_name = "blog"

urlpatterns = [
    path("", blog_views, name="blog"),
    path("<int:pid>/", single_views, name="single"),
    path("category/<str:cat_name>/", blog_views, name="category"),
    path("tag/<str:tag_name>/", blog_views, name="tag"),
    path("author/<str:author_username>/", blog_views, name="author"),
    path("search/", blog_search, name="search"),
    path("rss/feeds/", LatestEntriesFeed()),
]
