from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            "website:index",
            "website:about",
            "website:contact",
            "website:details",
            "website:portfolio",
            "website:services",
            "website:team",
            "website:newsletter",
        ]

    def location(self, item):
        return reverse(item)
