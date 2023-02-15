from django.shortcuts import render

# Create your views here.


def index_views(request):
    return render(request, "website/index.html")


def about_views(request):
    return render(request, "website/about.html")


def contact_views(request):
    return render(request, "website/contact.html")


def details_views(request):
    return render(request, "website/details.html")


def portfolio_views(request):
    return render(request, "website/portfolio.html")


def services_views(request):
    return render(request, "website/services.html")


def team_views(request):
    return render(request, "website/team.html")
