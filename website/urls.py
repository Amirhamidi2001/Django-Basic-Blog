from django.urls import path
from .views import *

app_name = "website"

urlpatterns = [
    path("", index_views, name="index"),
    path("about/", about_views, name="about"),
    path("contact/", contact_views, name="contact"),
    path("details/", details_views, name="details"),
    path("portfolio/", portfolio_views, name="portfolio"),
    path("services", services_views, name="services"),
    path("team/", team_views, name="team"),
]
