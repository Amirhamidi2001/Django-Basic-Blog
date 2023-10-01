from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm, NewsletterForm
from django.http.response import HttpResponseRedirect

# Create your views here.


def index_views(request):
    return render(request, "website/index.html")


def about_views(request):
    return render(request, "website/about.html")


def contact_views(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your ticket has been successfully sent"
            )
        else:
            messages.add_message(request, messages.ERROR, "Your ticket was not sent")
    form = ContactForm()
    return render(request, "website/contact.html", {"form": form})


def details_views(request):
    return render(request, "website/details.html")


def portfolio_views(request):
    return render(request, "website/portfolio.html")


def services_views(request):
    return render(request, "website/services.html")


def team_views(request):
    return render(request, "website/team.html")


def newsletter_views(request):
    """
    The newsletter_views function also handles both GET and POST requests.
    If the request method is POST, it creates a NewsletterForm object with the POST data and checks if it is valid.
    """

    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
